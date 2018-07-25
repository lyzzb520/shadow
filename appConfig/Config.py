import os

dbDir = os.path.abspath(__file__)
dbDir = os.path.dirname(dbDir)
dbDir = 'sqlite:///%s/mine.db' % (dbDir)


# print(dbDir)


class Base:
    SQLALCHEMY_DATABASE_URI = dbDir
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_TEARDOWN = True
