import os
from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

SECRET_KEY = os.environ['SECRET_KEY']