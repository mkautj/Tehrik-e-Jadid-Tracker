# tjtracker.py
import firebase_admin
from firebase_admin import credentials, firestore, messaging
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

# Test log message
logging.debug("Logging is configured correctly.")

# Initialize Firebase
try:
    cred = credentials.Certificate("serviceAccountKey.json")  # Update path
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    logging.info("Firebase initialized successfully.")
except Exception as e:
    logging.error(f"Error initializing Firebase: {e}")

class RoleScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            user_role = self.get_user_role()  # Fetch from Firebase/Auth
            logging.info(f"User role: {user_role}")
            if user_role == 'qiadat':
                self.current = 'form_i_screen'
            elif user_role == 'regional':
                self.current = 'form_ii_screen'
            elif user_role == 'admin':
                self.current = 'analytics_screen'
            Clock.schedule_interval(self.send_monthly_reminder, 2592000)  # Schedule monthly reminders
        except Exception as e:
            logging.error(f"Error in RoleScreenManager initialization: {e}")

    def get_user_role(self):
        # Implement logic to fetch user role from Firebase/Auth
        return 'qiadat'  # Placeholder

    def send_monthly_reminder(self, dt):
        try:
            message = messaging.Message(
                notification=messaging.Notification(
                    title='Monthly Report Reminder',
                    body='Please update and submit your monthly report.'
                ),
                topic='monthly_reports'
            )
            messaging.send(message)
            logging.info("Monthly reminder sent successfully.")
        except Exception as e:
            logging.error(f"Error sending monthly reminder: {e}")

# Define screens
class FormIScreen(Screen):
    pass

class FormIIScreen(Screen):
    pass

class AnalyticsScreen(Screen):
    pass

# Add screens to the ScreenManager
role_screen_manager = RoleScreenManager()
role_screen_manager.add_widget(FormIScreen(name='form_i_screen'))
role_screen_manager.add_widget(FormIIScreen(name='form_ii_screen'))
role_screen_manager.add_widget(AnalyticsScreen(name='analytics_screen'))