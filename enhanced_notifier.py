import json
import time
import logging
from datetime import datetime
from plyer import notification

def load_reminders(file_path):
    with open(file_path, 'r') as file:
        reminders = json.load(file)
    return reminders

def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Duration in seconds
    )
    logging.info(f"Notification shown - Title: '{title}', Message: '{message}'")

def schedule_notifications(reminders):
    while True:
        now = datetime.now().strftime("%H:%M")
        for reminder in reminders:
            if reminder['time'] == now:
                show_notification(reminder['title'], reminder['message'])
                time.sleep(60)  # Sleep for 60 seconds to avoid multiple notifications at the same minute
        time.sleep(30)  # Check every 30 seconds

if __name__ == "__main__":
    logging.basicConfig(filename='notifier.log', level=logging.INFO,
                        format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    reminders = load_reminders('reminders.json')
    logging.info("Reminders loaded successfully.")

    try:
        schedule_notifications(reminders)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
