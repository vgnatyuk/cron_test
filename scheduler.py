import os

from crontab import CronTab

from config import SOURCE_FOLDER, DESTINATION_FOLDER, UPDATE_RATE_MINUTE


cron = CronTab(user=True)

file_path = os.path.abspath('picture_handler.py')
path_from = os.path.abspath(SOURCE_FOLDER)
path_to = os.path.abspath(DESTINATION_FOLDER)

job = cron.new(command=f'python3 {file_path} {path_from} {path_to}')
job.minute.every(UPDATE_RATE_MINUTE)
cron.write()
