 # -*- coding: gbk -*-

import pymysql


class UtilDb(object):
    con = None

    @classmethod
    def __get_con(cls):
        if cls.con is None:
            cls.con = pymysql.connect(
                host="10.182.73.7",
                port=3306, user='bpd_acttest',
                password='BpdTest1234',
                database='',
                charset='utf-8')
        return cls.con

    @classmethod
    def __close_con(cls):
        if cls.con is not None:
            cls.con.close()
            cls.con = None

    @classmethod
    def selcet_db_one(cls, sql):
        cursor = None
        res = None
        try:
            cls.con = cls.__get_con()
            # 获取游标
            cursor = cls.con.cursor()
            # sql
            cursor.execute(sql)
            # 获取第一条结果
            res = cursor.fetchone()
        except Exception as err:
            print('查询sql错误：', str(err))
        finally:
            cursor.close()
            cls.__close_con()
            return res

    @classmethod
    def fix_db(cls, sql):
        cursor = None
        try:
            cls.con = cls.__get_con()
            # 获取游标
            cursor = cls.con.cursor()
            # sql
            cursor.execute(sql)
            cls.con.commit()
        except Exception as err:
            cls.con.rollback()
            print('增删改sql错误：', str(err))
        finally:
            cursor.close()
            cls.__close_con()
