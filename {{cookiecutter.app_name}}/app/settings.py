# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""
import os

from dotenv import load_dotenv

appdir = os.path.abspath(os.path.dirname(__file__))
projectdir = os.path.abspath(os.path.join(appdir, '..'))
load_dotenv(os.path.join(appdir, '.env'))

ENV = os.environ.get('FLASK_ENV')
DEBUG = ENV == 'development'
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(projectdir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
BCRYPT_LOG_ROUNDS = int(os.environ.get('BCRYPT_LOG_ROUNDS') or 13)
DEBUG_TB_ENABLED = DEBUG
DEBUG_TB_INTERCEPT_REDIRECTS = False
CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
WEBPACK_MANIFEST_PATH = 'webpack/manifest.json'
