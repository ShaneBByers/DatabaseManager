from DatabaseDataManager import DatabaseDataManager
from DatabaseEntity import DBEntity


def connect(logger_name, db_host, db_username, db_password, db_name, db_classes_file_path=None):
    return DatabaseDataManager(logger_name,
                               db_host,
                               db_username,
                               db_password,
                               db_name,
                               db_classes_file_path)


def entity(new_entity):
    return DBEntity(new_entity)
