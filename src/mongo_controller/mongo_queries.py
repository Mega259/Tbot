from pymongo import MongoClient
from utils import GetProfileConfigurationData
from utils import LoggerController

# setup logging
_logger = LoggerController.getLogger('scheduler')


def getConnectionData(profile):
    """
    get the connection data from the correspondent file
    :params profile: String with the values: 'dev', 'docker-pre' or 'docker'
    :returns: A dictionary with a host, username, password, auth_db and the port
    """
    _logger.info("Getting connection data for pymongo")
    data = GetProfileConfigurationData.profileData(profile)
    return {"host": data["host"], "platform_username": data["platform_username"], "platform_password": data["platform_password"], "auth_db": data["auth_db"], "port": data["port"]}


def getMongoClient(connection_data):
    """
    returns a mongoClient with the connection_data provided
    :params connection_data: A dictionary with a host, username, password, auth_db and the port
    :returns: an initialiced MongoClient object
    """
    _logger.info("Getting MongoClient")
    response = MongoClient(host=connection_data['host'], port=connection_data['port'], username=connection_data['platform_username'],
                           password=connection_data['platform_password'], authSource=connection_data['auth_db'])
    return response


def findOne(mongo_client, collection, query):
    """
    It performs a query in the collection provided
    :params mongo_client: An initialiced MongoClient object
    :params collection: The name of the collection we want to search
    :params query: The query we want to perform in the collection
    :returns: The query result in dict
    """
    _logger.info("Finding_one " + str(query))
    return mongo_client.onesaitplatform_rtdb[collection].find_one(query)


def insertOne(mongo_client, collection, data, key=""):
    """
    It performs an insertOne with the data provided in the collection. The key is an optional parameter for corner cases
    :params mongo_client: An initialiced MongoClient object
    :params collection: The name of the collection we want to search
    :params data: The JSON object we want to insert
    :params key: Sometimes, you want to insert an {"key": data}, and it's not safe to do it outside(it crash)
    :returns: the result of the query
    """
    _logger.info("Inserting one")
    if key == "":
        return mongo_client.onesaitplatform_rtdb[collection].insert_one({data})
    else:
        return mongo_client.onesaitplatform_rtdb[collection].insert_one({key: data})


def updateOne(mongo_client, collection, filter_query, data, key=""):
    """
    It performs an updateOne with the data provided in the collection, in the first result the the filter gives.
    The key is an optional parameter for corner cases
    :params mongo_client: An initialiced MongoClient object
    :params collection: The name of the collection we want to search
    :params data: The JSON object we want to insert
    :params key: Sometimes, you want to insert an {"key": data}, and it's not safe to do it outside(it crash)
    :returns: the result of the query
    """
    _logger.info("updating one")
    if key == "":
        return mongo_client.onesaitplatform_rtdb[collection].update_one(filter_query, data)
    else:
        return mongo_client.onesaitplatform_rtdb[collection].update_one({filter_query}, {'$set': {key: data}})


def findAll(mongo_client, collection, query):
    """
    It performs a query in the collection provided
    :params mongo_client: An initialiced MongoClient object
    :params collection: The name of the collection we want to search
    :params query: The query we want to perform in the collection
    :returns: The query result in dict
    """
    _logger.info("Finding a lot " + str(query))
    return mongo_client.onesaitplatform_rtdb[collection].find(query)
