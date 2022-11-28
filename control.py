
#連線DB
from dbConfig import conn, cur

def getAuctionList():
    #拍賣首頁
    sql="SELECT `id`, `name`, `price`, `uName`,`expireTime` FROM `auctionlist` order by id asc;"
    cur.execute(sql)
    records = cur.fetchall()
    return records
    
def getUserInfo(uid):
    #個人資料
    sql="SELECT `uid`,`uName` FROM `user` where uid = %s"
    cur.execute(sql,(uid,))
    records = cur.fetchall()
    return records

def getHistoryInfo(uid):
    #歷史資料
    sql="SELECT `id`,`price` FROM `auctioninfo` where uid = %s"
    cur.execute(sql,(uid,))
    records = cur.fetchall()
    return records       
    
def bidding(uid,id,bidding):
    #競標
    sql="UPDATE `auctionlist` SET `price`=%s,`uName`= (select uName from user where uid = %s) WHERE id = %s and price < %s;"
    cur.execute(sql,(bidding,uid,id,bidding))
    conn.commit()
    return True

def addAuctionInfo(uid,id,bidding):
    #新增紀錄
    sql="insert into auctioninfo (uid,id,price) values (%s,%s,%s);"
    cur.execute(sql,(uid,id,bidding))
    conn.commit()
    return True    
    
def addNewGood(name,price):
    #新增拍賣品
    sql="insert into auctionlist (name,price) values (%s,%s);"
    cur.execute(sql,(name,price))
    conn.commit()
    return True    

