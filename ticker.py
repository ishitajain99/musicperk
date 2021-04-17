from datetime import datetime
import mysql.connector as SQL
import pandas as pd

conn = SQL.connect(user="root", passwd="", host="localhost",
                       database="musicperk")
cur = conn.cursor()

df = pd.read_excel("HINDALCO_1D.xlsx",engine='openpyxl')
date_time = df['datetime']
close = df['close']
high = df['high']
low = df['low']
open = df['open']
volume = df['volume']
instrument = df['instrument']
query = '''
    INSERT INTO ticker_symbol (date,close,high,low,open,volume,instrument)
    value(%s,%s,%s,%s,%s,%s,%s);
'''
for d,c,h,l,o,v,i in zip(date_time,close,high,low,open,volume,instrument):
    date,time=str(d).split(" ")
    yyyy,mm,dd = date.split('-')
    h,m,s = time.split(':')
    d = datetime(int(yyyy),int(mm),int(dd),int(h),int(m),int(s))
    cur.execute(query,(d,c,h,l,o,v,i))
conn.commit()
