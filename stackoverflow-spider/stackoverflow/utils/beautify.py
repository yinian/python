#!/usr/bin/env python
# -*- coding: utf-8 -*-
##
import os
import json

import pymysql
from pyecharts import options as opts
from pyecharts.charts import Line

linkList = []
voteList = []

def get_Line_Chart_data():
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="root",
        db="stackoverflow_spider",
        charset="utf8")

    cur = conn.cursor()
    try:
        sql_link = """
                select s_links from stackoverflow_info order by s_votes desc
        """
        cur.execute(sql_link)
        links = cur.fetchall()
        for name in links:
            linkList.append(name[0])
        sql_vote = """
            select s_votes from stackoverflow_info order by s_votes desc
        """
        cur.execute(sql_vote)
        votes = cur.fetchall()
        for vote in votes:
            voteList.append(vote[0])
    except:
        print("未查询到数据")
        conn.rollback()
    finally:
        conn.close()

def drawLineCharts():
    # bar = Bar("我的第一个图表", "这里是副标题")
    # bar.add("服装",linkList,voteList,is_more_utils=True)
    # bar.show_config()
    line = (
        Line()
            .set_global_opts(
            tooltip_opts=opts.TooltipOpts(is_show=False),
            xaxis_opts=opts.AxisOpts(type_="value"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        )
            .add_xaxis(xaxis_data=linkList)
            .add_yaxis(
            series_name="votes折线图",
            y_axis=voteList,
            symbol="emptyCircle",
            is_symbol_show=True,
            is_smooth=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
    )
    line.render("smoothed_line_chart.html")

if __name__=='__main__':
    get_Line_Chart_data()
    drawLineCharts()


