from time import sleep
from celery import Celery
from celery.utils.log import get_task_logger
from src.config.settings import settings

# Initialize celery
celery = Celery('tasks', broker=settings.CELERY_BROKER_URL)

# Create logger - enable to display messages on task logger
celery_log = get_task_logger(__name__)
