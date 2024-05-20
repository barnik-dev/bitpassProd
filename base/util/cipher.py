from cryptography.fernet import Fernet
from pathlib import Path

import environ

# ROOT DIRECTORY OF PROJECT
BASE_DIR = Path(__file__).resolve().parent.parent

# ENVIRONMENT VARIABLE
env = environ.Env()
environ.Env.read_env("BASE_DIR / 'bitpass/env'")


FERNET_KEY = eval(env('FERNET_KEY'))

cipher_suite = Fernet(FERNET_KEY)

def encrypt_data(data):
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data):
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data