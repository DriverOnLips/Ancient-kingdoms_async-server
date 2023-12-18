# tasks.py

from celery import shared_task
import random
import time

@shared_task
def get_random_number(min_value, max_value):
    time.sleep(random.randint(5, 10))  # имитация задержки
    return random.randint(min_value, max_value)
