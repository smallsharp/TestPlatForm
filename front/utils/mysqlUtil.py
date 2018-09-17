import pymysql as ps
from pymysql import cursors


class MysqlCommand:

    def __init__(self, host, user, password, database, charset):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.db = None
        self.curs = None
        self.open()
    # 数据库连接
    def open(self):
        # 执行返回数据类型为字典：cursorclass =cursors.DictCursor
        self.db = ps.connect(host=self.host, user=self.user, password=self.password,database=self.database, charset=self.charset,cursorclass =cursors.DictCursor)
        self.curs = self.db.cursor()
    # 数据库关闭
    def close(self):
        self.curs.close()
        self.db.close()
    # 数据增删改
    def runCud(self, sql, params):
        try:
            self.curs.execute(sql, params)
            self.db.commit()
            return 1
        except :
            print('cud出现错误')
            self.db.rollback()
            return 0

    # 数据查询,获取结果集
    def runQuery(self, sql, params):
        try:
            self.curs.execute(sql, params)
            result = self.curs.fetchall()
            return result
        except Exception as e:
            print(e)

if __name__ == '__main__':
    db1 = MysqlCommand(host='127.0.0.1', user='root', password='root', database='test', charset='utf8')

    sql = "select * from testcase where suiteId=%s and id=%s"

    results = db1.runQuery(sql, (2, 4))

    db1.close()

    for result in results:
        print(result)
        # print(result.get('id'))