"""
    module that will login to the various demonstration databases consistently
"""

import configparser
from pathlib import Path
import pymongo
import redis
from neo4j.v1 import GraphDatabase, basic_auth
import urllib
import dns

import utilities

log = utilities.configure_logger('default', '../logs/login_databases_dev.log')
#config_file = Path(__file__).parent.parent / '.config/config.ini'
config_file = Path('z:/uofw/Python220/nosql_repo/.config/config1.ini')
config = configparser.ConfigParser()


def login_mongodb_cloud():
    """
        connect to mongodb and login
    """

    log.info('Here is where we use the connect to mongodb.')
    log.info('Note use of f string to embed the user & password (from the tuple).')
    try:
        config.read(config_file)
        user = config["mongodb_cloud"]["user"]
        pw = config["mongodb_cloud"]["pw"]

    except Exception as e:
        print(f'error: {e}')
        
    client = pymongo.MongoClient(f'mongodb+srv://{user}:{pw}@cluster0-d6haw.mongodb.net/test?retryWrites=true')
    
    return client


def login_redis_cloud():
    """
        connect to redis and login
    """
    try:
        
        config.read(config_file)
        host = config["redis_cloud"]["host"]
        port = config["redis_cloud"]["port"]
        pw = config["redis_cloud"]["pw"]
        


    except Exception as e:
        print(f'error: {e}')

    log.info('Here is where we use the connect to redis.')

    try:
        
        r = redis.Redis(host=host, port=port, password=pw)
        

    except Exception as e:
        print(f'error: {e}')

    return r


def login_neo4j_cloud():
    """
        connect to neo4j and login

    """

    log.info('Here is where we use the connect to neo4j.')
    log.info('')

    config.read(config_file)
    log.info('Read the config_file')

    graphenedb_user = config["neo4j_cloud"]["user"]
    log.info('Read the user name')
    graphenedb_pass = config["neo4j_cloud"]["pw"]
    log.info('Read the pw')
    graphenedb_url = 'bolt://hobby-bnehfidmdoangbkeoomlekbl.dbs.graphenedb.com:24786'
    driver = GraphDatabase.driver(graphenedb_url, 
            auth=basic_auth(graphenedb_user, graphenedb_pass))

    return driver

#if __name__ == '__main__':
    #login_mongodb_cloud()
    #login_redis_cloud()
    #login_neo4j_cloud()