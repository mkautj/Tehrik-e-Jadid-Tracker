# tjtracker.py
import firebase_admin
from firebase_admin import credentials, firestore, messaging
from kivy.uix.screenmanager import ScreenManager
from kivy.clock import Clock
import kivy
from kivy.app import App
import logging

# Configure logging with file output
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info('Application starting...')

# Test log message
logging.debug("Logging is configured correctly in main.py.")

# Initialize Firebase
cred = credentials.Certificate("path/to/service-account-key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

class RoleScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        user_role = self.get_user_role()  # Fetch from Firebase/Auth
        if user_role == 'qiadat':
            self.current = 'form_i_screen'
        elif user_role == 'regional':
            self.current = 'form_ii_screen'
        elif user_role == 'admin':
            self.current = 'analytics_screen'
        Clock.schedule_interval(self.send_monthly_reminder, 2592000)  # Schedule monthly reminders

    def send_monthly_reminder(self, dt):
        message = messaging.Message(
            notification=messaging.Notification(
                title='Monthly Report Reminder',
                body='Please update and submit your monthly report.'
            ),
            topic='monthly_reports'
        )
        messaging.send(message)

role_screen_manager = RoleScreenManager()

class TehrikEJadidApp(App):
    def build(self):
        logger.info('Building application...')
        try:
            from tjtracker import role_screen_manager
            logger.info('Screen manager loaded successfully')
            return role_screen_manager
        except Exception as e:
            logger.error(f'Error loading screen manager: {e}')
            raise

if __name__ == '__main__':
    logger.info('Starting application...')
    TehrikEJadidApp().run()