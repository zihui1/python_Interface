# -*- coding:utf-8 -*-

import cx_Oracle,json
import pandas as pd


class ORACLE(object):
    def __init__(self, host, db, user, pwd):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        if not self.db:
            raise (NameError, "没有设置数据库信息")
        # self.dsn = cx_Oracle.makedsn(host=self.host, port=1521, sid=self.sid)
        # self.conn = cx_Oracle.connect(user=self.user, password=self.pwd, dsn=self.dsn)
        self.conn = cx_Oracle.connect(self.user + '/' + self.pwd + '@' + self.host + '/' + self.db)
        cursor = self.conn.cursor()
        if not cursor:
            raise (NameError, "连接数据库失败")
        else:
            return cursor

    def ExecQuery(self, sql):
        cursor = self.__GetConnect()
        list = []
        cursor.execute(sql)
        result = cursor.fetchall()
        col_name = cursor.description
        for row in result:
            dict = {}
            for col in range(len(col_name)):
                key = col_name[col][0]
                value = row[col]
                dict[key] = value
            list.append(dict)
        js = json.dumps(list, ensure_ascii=False, indent=2, separators=(',', ':'))
        # 查询完毕后必须关闭连接
        self.conn.close()
        return js

    def ExecQueryToDataFrame(self, sql):
        cursor = self.__GetConnect()
        cursor.execute(sql)
        # 调出数据
        resList = cursor.fetchall()
        # cols为字段信息 例如((''))
        cols = cursor.description
        # 查询完毕后必须关闭连接
        self.conn.close()

        # 将数据转换为DataFrame
        col = []
        for i in cols:
            col.append(i[0])
        data = list(map(list, resList))
        data = pd.DataFrame(data, columns=col)

        return data

    def ExecNonQuery(self, sql):
        cursor = self.__GetConnect()
        cursor.execute(sql)
        self.conn.commit()
        self.conn.close()

if __name__  == "__main__":
    sql = "select * from IM_USER where user_id = 305"
    re = ORACLE(user = "wfb",pwd = "qwer1234",host='192.168.31.234',db = 'uenpay')
    rr = re.ExecQuery(sql)

    print(rr)