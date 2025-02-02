# analytics.py
import matplotlib.pyplot as plt
import sqlite3
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

def plot_contributions(user_role):
    try:
        conn = sqlite3.connect('tehrik_jadid.db')
        c = conn.cursor()
        c.execute('SELECT month, SUM(amount_paid) FROM form_i GROUP BY month')
        data = c.fetchall()
        
        months = [row[0] for row in data]
        amounts = [row[1] for row in data]
        
        plt.bar(months, amounts)
        plt.savefig('contributions.png')  # Display in app via Kivy Image
        logging.info("Contributions plot saved successfully.")
    except Exception as e:
        logging.error(f"Error plotting contributions: {e}")