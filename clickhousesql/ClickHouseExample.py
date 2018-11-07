#!/opt/anaconda2/bin/python2.7
# -*- coding: utf8 -*-

'''
Created on 2018年10月11日

@author: wzt
设计思路:
1：this clickhouse example code
'''

from clickhouse_driver.client import Client

client=Client(host='172.20.10.8',database='default',user='default',password='hadoop',compression='zstd')

client.execute('SHOW TABLES')

client.execute('DROP TABLE IF EXISTS monchickey.test_py27')

client.execute('CREATE TABLE monchickey.test_py27 (x Int32) ENGINE = Memory')

client.execute(
    'INSERT INTO monchickey.test_py27 (x) VALUES',
    [{'x': 1}, {'x': 2}, {'x': 3}, {'x': 100}]
)
client.execute('INSERT INTO monchickey.test_py27 (x) VALUES', [[200]])

print(client.execute('SELECT sum(x) FROM monchickey.test_py27'))