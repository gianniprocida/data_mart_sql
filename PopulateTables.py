from faker import Faker
import mysql.connector
from sqlalchemy import create_engine
import pandas as pd
from myfun import *
import os

def getConn():
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Chimica90$"
    )
   
    return cnx




cnx = getConn()

cur = cnx.cursor()

cur.execute("use data_mart_airbnb")


# Load Hosts.csv file into the corresponding table
df1 = pd.read_csv("Hosts.csv")

for row in df1.itertuples():
  cur.execute("""insert into Hosts (id,first_name,last_name,email,phone_number) values (%s,%s,%s,%s,%s)""",
  (row.id,row.first_name,row.last_name,row.email,row.phone_number))



# Load Addresses.csv file into the corresponding table
df2 = pd.read_csv("Addresses.csv")


for row in df2.itertuples():
  cur.execute("""insert into Addresses (id,street,house_number,zip,
  city,country) values (%s,%s,%s,%s,%s,%s)""",
  (row.id,row.street_name,row.house_number,row.zip_code,row.city,row.state))


# Load Users.csv file into the corresponding table
df3 = pd.read_csv("Users.csv")


for row in df3.itertuples():
  cur.execute("""insert into Users (id,first_name,last_name,email,phone_number,DoB,gender,country,user_type,num_of_reviews) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
  (row.id,row.first_name,row.last_name,row.email,row.phone_number,row.DoB,row.gender,row.country,row.user_type,row.num_of_reviews))


# Load Listings.csv into the corresponding table
df3 = pd.read_csv("Listings.csv")

for row in df3.itertuples():
  cur.execute("""insert into Listings (id,host_id,title,property_type,room_type,accommodates,bedrooms,bathrooms,price_per_night,address_id) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
  (row.id,row.host_id,row.title,row.property_type,row.room_type,row.accommodates,row.bedrooms,row.bathrooms,row.price_per_night,row.address_id))


# Load Reviews.csv into the corresponding table

df4 = pd.read_csv("Reviews.csv")


ombined = f"id,listing_id,user_id,description,review_date,rating,host_response\n"

for row in df4.itertuples():
  cur.execute("""insert into Reviews (id,listing_id,user_id,description,review_date,rating,host_response) values (%s,%s,%s,%s,%s,%s,%s)""",
  (row.id,row.listing_id,row.user_id,row.description,row.review_date,row.rating,row.host_response))


# Using a for loop to insert CSV files into the corresponding tables will not scale well for larger databases.


cnx.commit()

cnx.close()