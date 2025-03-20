# app-server/log_generator.py
import logging
import os
import schedule
import time
import random

# Configure logging
log_dir = '/app/logs'
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, 'app.log')

logging.basicConfig(
    filename=log_file, 
    level=logging.INFO, 
    format='%(asctime)s - %(message)s'
)

def generate_log():
    """Generate a simple log entry"""
    log_messages = [
        "User login attempt",
        "Database query executed",
        "API endpoint accessed",
        "System health check",
        "Configuration update"
    ]
    message = random.choice(log_messages)
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}")  # Console output
    logging.info(message)  # File output

def main():
    # Generate log every minute
    schedule.every(5).seconds.do(generate_log)

    print("Log generator started")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
