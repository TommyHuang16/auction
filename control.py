
#連線DB
from dbConfig import conn, cur

def getAuctionList():
    #拍賣首頁
    sql="select id, name,price from auctionlist order by id asc ;"
    cur.execute(sql)
    records = cur.fetchall()
    return records