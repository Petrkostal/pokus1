import sqlite3

connection = sqlite3.connect('data_colect')
cur = connection.cursor()
cur.execute("drop table OHC_data")
cur.execute("""create table OHC_data(
           id integer primary key autoincrement
            ,symbol text not null
            ,last_price real not null
            ,last_time datetime not null
             )""")

for i in range(5):
    cur.execute(f'insert into OHC_data (symbol, last_price, last_time) values(\'BTCUSDT{i}\', 1115, "2025-01-02 15:10:05")')
cur.execute('select * from OHC_data')
for row in cur.fetchall():
    print (row)

"""
https://api.binance.com/api/v3/exchangeInfo?symbol=BNBBTC
https://www.binance.com/api/v3/ticker/price
"""