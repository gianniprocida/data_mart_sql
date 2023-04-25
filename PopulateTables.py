from faker import Faker
import mysql.connector
from sqlalchemy import create_engine
import pandas as pd
from myfun import generate_fake_addresses,generate_fake_listings
import os

def getConn():
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Chimica90$"
    )
   
    return cnx

generate_fake_listings()

generate_fake_addresses()

# Create an engine to connect to the database that is a string representing the database connection
#engine = create_engine("""mysql+mysqlconnector://{user}:{password}@{host}/{db}""".format(user="root",host="localhost",password="Chimica90$",db="data_mart_airbnb"))

df1 = pd.read_csv("Addresses.csv")

cnx = getConn()

cur = cnx.cursor()

cur.execute("use data_mart_airbnb")

    

for row in df1.itertuples():
  cur.execute("""insert into Addresses (id,street,house_number,zip,
  city,country) values (%s,%s,%s,%s,%s,%s)""",
  (row.id,row.street_name,row.house_number,row.zip_code,row.city,row.state))

os.remove("Addresses.csv")

df2 = pd.read_csv("Listings.csv")

    

for row in df2.itertuples():
  cur.execute("""insert into Listings (id,title,property_type,room_type,accommodates,bedrooms,bathrooms,price_per_night,address_id) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
  (row.id,row.title,row.property_type,row.room_type,row.accommodates,row.bedrooms,row.bathrooms,row.price_per_night,row.address_id))

os.remove("Listings.csv")

cnx.commit()

cnx.close()