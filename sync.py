# sync.py
import sqlite3
import firebase_admin
from firebase_admin import credentials, firestore
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

# Initialize Firestore DB
try:
    cred = credentials.Certificate('path/to/your/serviceAccountKey.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    logging.info("Firestore initialized successfully.")
except Exception as e:
    logging.error(f"Error initializing Firestore: {e}")

def sync_data():
    try:
        conn = sqlite3.connect('tehrik_jadid.db')
        c = conn.cursor()
        
        # Fetch unsynced Form I entries
        c.execute('SELECT * FROM form_i WHERE synced = 0')
        unsynced_form_i = c.fetchall()
        
        for entry in unsynced_form_i:
            data = {
                'financial_year': entry[1],
                'month': entry[2],
                'book_no': entry[6],
                # ... other fields
            }
            # Push to Firestore
            db.collection('form_i').add(data)
            # Mark as synced
            c.execute('UPDATE form_i SET synced = 1 WHERE id = ?', (entry[0],))
        
        # Fetch unsynced Form II entries
        c.execute('SELECT * FROM form_ii WHERE synced = 0')
        unsynced_form_ii = c.fetchall()
        
        for entry in unsynced_form_ii:
            data = {
                'financial_year': entry[1],
                'month': entry[2],
                'book_no': entry[6],
                # ... other fields
            }
            # Push to Firestore
            db.collection('form_ii').add(data)
            # Mark as synced
            c.execute('UPDATE form_ii SET synced = 1 WHERE id = ?', (entry[0],))
        
        conn.commit()
        conn.close()
        logging.info("Data synced successfully.")
    except Exception as e:
        logging.error(f"Error syncing data: {e}")