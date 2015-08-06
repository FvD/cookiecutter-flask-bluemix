# -*- coding: utf-8 -*-
import os
import json

os_env = os.environ


class Config(object):
    SECRET_KEY = os_env.get('{{cookiecutter.app_name | upper}}_SECRET', 'secret-key')  # TODO: Change me
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    ASSETS_DEBUG = False
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.


class ProdConfig(Config):
    """Production configuration."""
    ENV = 'prod'
    DEBUG = False
    # Example connection to ElephantSQL database. Don't forget to bind a 
    # database service to your app. 
    if 'VCAP_SERVICES' in os.environ:
        postgres_service = json.loads(os.environ['VCAP_SERVICES'])['elephantsql'][0]
        uri = postgres_service["credentials"]["uri"]
        uri_strings = uri.split("/")
        connection_string = uri_strings[2]
        db_name = uri_strings[3]
        SQLALCHEMY_DATABASE_URI = "postgresql://%s/%s" % (connection_string,
                                                                   db_name)
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar


class DevConfig(Config):
    """Development configuration."""
    ENV = 'dev'
    DEBUG = True
    DB_NAME = 'dev.db'
    # Put the db file in project root
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
    DEBUG_TB_ENABLED = True
    ASSETS_DEBUG = True  # Don't bundle/minify static assets
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    BCRYPT_LOG_ROUNDS = 1  # For faster tests
    WTF_CSRF_ENABLED = False  # Allows form testing
