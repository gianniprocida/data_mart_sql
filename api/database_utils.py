import mysql.connector

def getConn(host,user,password):
    cnx = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        db='data_mart_airbnb'
    )
    return cnx