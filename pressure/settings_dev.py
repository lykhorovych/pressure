import os
from pressure.settings import *
from dotenv import load_dotenv

load_dotenv(BASE_DIR / '.env.dev')

DEBUG = os.getenv('DEBUG') == True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'postgres'),  # Назва бази даних
        'USER': os.getenv('POSTGRES_USER' ,'postgres'),  # Ім'я користувача
        'PASSWORD': os.getenv('POSTGRES_PASSWORD' ,'example'),  # Пароль
        'HOST': os.getenv('POSTGRES_HOST' ,'db'),  # Якщо PostgreSQL на локальній машині
        'PORT': '5432',  # Порт за замовчуванням для PostgreSQL
    }
}

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS').split(" ")
