import mysql.connector

def getConn(host,user,pw,db):
    cnx = mysql.connector.connect(
        host=host,
        user=user,
        password=pw,
        db=db
    )
    return cnx