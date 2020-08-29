import pymysql as mql


def create_connect():
    conn = mql.connect(
            host='localhost',
            user='root',
            password='redhat',
            db='helloTest',
            charset='utf8',
       # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。

              )