# coding:utf8
import MySQLdb
import sys


class TransferMoney(object):
    def __init__(self, conn):
        self.conn = conn

    def check_acct_available(self, acctid):
        cursor = self.conn.cursor()
        print "check_acct_available %s" % acctid
        try:
            sql = "select * from account where acctid=%s" % acctid
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("账号%s不存在" % acctid)
        finally:
            cursor.close()

    def has_enough_money(self, acctid, money):
        cursor = self.conn.cursor()
        print "has_enough_money %s" % acctid
        try:
            sql = "select * from account where acctid=%s and money>%s" % (acctid, money)
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("账号%s没有足够的钱" % acctid)
        finally:
            cursor.close()

    def reduce_money(self, acctid, money):
        cursor = self.conn.cursor()
        print "acctid:%s reduce_money %s" % (acctid, money)
        try:
            sql = "update account set money=money-%s where acctid=%s" % (money, acctid)
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception("账号%s减款失败" % acctid)
        finally:
            cursor.close()

    def add_money(self, acctid, money):
        cursor = self.conn.cursor()
        print "acctid:%s add_money %s" % (acctid, money)
        try:
            sql = "update account set money=money+%s where acctid=%s" % (money, acctid)
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception("账号%s加款失败" % acctid)
        finally:
            cursor.close()

    def transfer(self, source_accid, target_accid, money):
        try:
            self.check_acct_available(source_accid)
            self.check_acct_available(target_accid)
            self.has_enough_money(source_accid, money)
            self.reduce_money(source_accid, money)
            self.add_money(target_accid, money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e


if __name__ == "__main__":
    source_accid = 11
    target_accid = 12
    money = 100
    conn = MySQLdb.connect(
        host='127.0.0.1',
        port=3306,
        db='python_mysql',
        user='root',
        passwd='root',
        charset='utf8')
    trans_money = TransferMoney(conn)
    try:
        trans_money.transfer(source_accid, target_accid, money)
    except Exception as e:
        print e
    finally:
        conn.close()
