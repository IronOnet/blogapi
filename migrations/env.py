from __future__ import with_statement 
from alembic import context  
from sqlalchemy import engine_from_config, pool 
from logging.config import fileConfig 
import logging 

# Alembic Config object, which provides 
# access to the values within the .ini file 
# in use 
config = context.config 

# Interpret the config file for python logging 
# This line set up the logger 
fileConfig(config.config_file_name) 
logger = logging.getLogger('alembic.env')

from flask import current_app 
config.set_main_option('sqlalchemy.url', 
                    current_app.config.get)