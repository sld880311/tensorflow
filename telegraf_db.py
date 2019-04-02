#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Theodore Sun
# datetime:2019/1/7 8:57
# software: PyCharm

from influxdb import InfluxDBClient
import six


class TelegrafCommonDb(object):
    """
    execute telegraf influxdb
    """
    def __init__(self):
        self.client = self.get_influxdb_client()

    def get_influxdb_client(self):
        client = InfluxDBClient(host="127.0.0.1",
                                port=38086,
                                username="root",
                                password="root",
                                database="telegraf"
                                )
        return client

    def read_influxdb_data(self, sql):
        results = list()
        try:
            res = self.client.query(sql)
            print(res)
            if res.raw.get('series', None) is None:
                print("do not read any data in influxdb:%s", sql)
            else:
                print(res.raw)
                # print(res.raw.get('series')[0]['values'])
                results = res.raw['series'][0]['values']
        except Exception as e:
            return results, six.text_type(e)
        return results, None


telegraf_db = TelegrafCommonDb()
telegraf_db_client = telegraf_db.client
# print(telegraf_db_client)
sql1 = "select * from cpu where time > now() - 5111m limit 2"
sql2 = "select * from (" \
       "       SELECT " \
       "            mean(usage_idle) as usage_idle_mean," \
       "            max(usage_idle) as usage_idle_max," \
       "            min(usage_idle) as usage_idle_min," \
       "            mean(usage_system) as usage_system_mean," \
       "            max(usage_system) as usage_system_max ," \
       "            min(usage_system) as usage_system_min " \
       "FROM \"cpu\" group by cpu)"

sql3 = "SELECT " \
       "    mean(usage_idle) as usage_idle_mean," \
       "    max(usage_idle) as usage_idle_max," \
       "    min(usage_idle) as usage_idle_min," \
       "    mean(usage_system) as usage_system_mean," \
       "    max(usage_system) as usage_system_max ," \
       "    min(usage_system) as usage_system_min " \
       "FROM \"cpu\" group by cpu"
sql4 = "SELECT " \
       "    mean(used)," \
       "    max(used)," \
       "    min(used)," \
       "    count(used) " \
       "FROM \"mem\" " \
       "group by *"
sql5 = "SELECT mean(used) FROM \"disk\" group by * limit 1"
res = telegraf_db.read_influxdb_data(sql2)
# print(res[0])
