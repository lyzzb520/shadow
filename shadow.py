from appConfig.App import app, db
import os
dbDir = os.path.dirname(__file__)
dbDir = '%s%sappConfig%smine.db' % (dbDir, os.sep, os.sep)
if not os.path.exists(dbDir):
    # 创建数据库并创建表
    db.create_all()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
