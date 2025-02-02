# forms.py
import sqlite3
from kivy.uix.screenmanager import Screen
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

class FormIInputScreen(Screen):
    def save_to_local(self):
        try:
            conn = sqlite3.connect('tehrik_jadid.db')
            c = conn.cursor()
            c.execute('''INSERT INTO form_i 
                        (financial_year, month, book_no, total_promises, amount_paid, balance, receipt_no, son_of, qiadat_secretary, synced) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0)''',
                        (self.ids.financial_year.text, 
                         self.ids.month.text, 
                         self.ids.book_no.text,
                         self.ids.total_promises.text,
                         self.ids.amount_paid.text,
                         self.ids.balance.text,
                         self.ids.receipt_no.text,
                         self.ids.son_of.text,
                         self.ids.qiadat_secretary.text))
            conn.commit()
            conn.close()
            logging.info("Form I data saved locally.")
        except Exception as e:
            logging.error(f"Error saving Form I data: {e}")