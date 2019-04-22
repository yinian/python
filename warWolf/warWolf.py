#-*- coding: utf-8 -*-

import json
import re
import requests
import pandas as pd
from datetime import date, timedelta

def getHtml(jsonData):
    data = json.loads(jsonData)
    return data['ticketList'].encode('utf-8').replace('\n', '').replace(' ','')

def parseHtml(html):
    reg = r"<ul.+?><liclass='c1'><b>(.+?)</b>.+?</li>"
    reg += r"<liclass=\"c2\"><b>(.+?)</b>.+?</li>"
    reg += r"<liclass=\"c3\">(.+?)%</li>"
    reg += r"<liclass=\"c4\">(.+?)%</li>"
    reg += r"<liclass=\"c5\"><spanstyle=\"margin-right:-.1rem\">(.+?)%</span>"

    pattern = re.compile(reg)
    movieList = re.findall(pattern, html)

    return movieList


def getDataByDate(date):    
    url = 'https://piaofang.maoyan.com/dayoffice?date=%s&cnt=10' % date

    headers={
        "authority": "piaofang.maoyan.com",
        "method": "GET",
        "path": "/dayoffice?date=%s&cnt=10" % date,
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.8",
        "referer": "https://piaofang.maoyan.com/?date=%s" % date,
        "uid": "e4e5902fc42ad5e198b207d76af1d82e7056cb82",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
    req = requests.get(url, headers=headers)
    return req.content

def buildDataFrame(movieList, date):
    index = [date for i in range(len(movieList))]
    df = pd.DataFrame(movieList, columns=['name', 'box', 'boxRatio', 'playRatio', 'attendance'], index=index)
    df['box'] = df['box'].astype('float64')
    df['boxRatio'] = df['boxRatio'].astype('float64')
    df['playRatio'] = df['playRatio'].astype('float64')
    df['attendance'] = df['attendance'].astype('float64')
    return df

def buildDates(start, days):
    day = timedelta(days=1)
    for i in range(days):
        yield start + day*i

def getData(Y, M, D, days):    
    start = date(Y, M, D)
    df = pd.DataFrame()
    for d in buildDates(start, days):
        day = str(d)
        data = getDataByDate(day)
        html = getHtml(data)
        movieList = parseHtml(html)
        temp = buildDataFrame(movieList, day)
        df = df.append(temp)
    return df

def writeToCSV(df, path):
    df.to_csv(path)

if __name__ == "__main__":
    df = getData(2017, 10, 1, 3)
    print df
    writeToCSV(df, 'data\out.csv')