
#連線DB
from dbConfig import conn, cur

def getAuctionList():
    #拍賣首頁
    sql="SELECT `id`, `name`, `price`, `uName`,`expireTime` FROM `auctionlist` order by id asc;"
    cur.execute(sql)
    records = cur.fetchall()
    return records
    
def getUserInfo(uName):
    #個人資料
    sql="SELECT `uid`,`uName` FROM `user` where uName = %s"
    cur.execute(sql,(uName,))
    records = cur.fetchall()
    return records
    
def getBidInfo(id):
    #個人資料
    sql="SELECT `id`,`price`,`uName` FROM `auctioninfo` where id = %s order by aid asc;"
    cur.execute(sql,(id,))
    records = cur.fetchall()
    return records

def getHistoryInfo(uName):
    #歷史資料
    sql="SELECT `id`,`price` FROM `auctioninfo` where uid = (select uid from user where uName = %s) "
    cur.execute(sql,(uName,))
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
    sql="insert into auctioninfo (uid,id,price,uName) values (%s,%s,%s,(select uName from user where uid= %s));"
    cur.execute(sql,(uid,id,bidding,uid))
    conn.commit()
    return True    
    
def addNewGood(name,price):
    #新增拍賣品
    sql="insert into auctionlist (name,price,expireTime) values (%s,%s,now()+interval 10 minute);"
    cur.execute(sql,(name,price))
    conn.commit()
    return True 

def addUser(name):
    #新增拍賣品
    sql="insert into user (uName) values (%s);"
    cur.execute(sql,(name,))
    conn.commit()
    return True      

