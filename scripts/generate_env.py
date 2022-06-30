import os
from django.core.management.utils import get_random_secret_key

def generate_secret_key(filepath):
    secret_key_file = open(filepath, "w")
    secret_key = f'SECRET_KEY={get_random_secret_key()}'
    secret_key_file.write(secret_key)
    secret_key_file.close()

SETTINGS_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
generate_secret_key(os.path.join(SETTINGS_DIR, '.env'))