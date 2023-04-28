import mysql.connector
from sqlalchemy import create_engine, Date, Enum
import pandas as pd
import sqlalchemy


def getConn():
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Chimica90$"
    )

    return cnx


engine = create_engine("""mysql+mysqlconnector://{user}:{password}@{host}/{db}""".
                       format(user="root", host="localhost", password="Chimica90$", db="data_mart_airbnb"))


mydata = {
    'Users.csv': {'id': sqlalchemy.Integer, 'first_name': sqlalchemy.String(50), 'last_name': sqlalchemy.String(50), 'email': sqlalchemy.String(50), 'phone_number': sqlalchemy.String(50),
                  'DoB': Date(), 'gender': Enum("Male", "Female"), 'country': sqlalchemy.String(50), 'user_type': Enum("host", "guest"), 'num_of_reviews': sqlalchemy.Integer},

    'Addresses.csv': {'id': sqlalchemy.Integer, 'street_name': sqlalchemy.String(100), 'house_number': sqlalchemy.Integer, 'city': sqlalchemy.String(50), 'country': sqlalchemy.String(50), 'zip_code': sqlalchemy.Integer},

    'Listings.csv': {'id': sqlalchemy.Integer, 'host_id': sqlalchemy.Integer, 'title': sqlalchemy.String(100),
                     'property_type': Enum('apartment','house','villa'), 'room_type': Enum('private room', 'shared room', 'entire home/apt'), 'accommodates': sqlalchemy.Integer,
                     'bedrooms': sqlalchemy.Integer, 'bathrooms': sqlalchemy.Integer,
                     'price_per_night': sqlalchemy.Float, 'address_id': sqlalchemy.Integer},

    'Reviews.csv': {'id': sqlalchemy.Integer, 'listing_id': sqlalchemy.Integer, 'user_id': sqlalchemy.Integer,
                    'comment': sqlalchemy.String(100), 'review_date': Date(), 'rating': sqlalchemy.Integer, 'host_response': sqlalchemy.String(100)},

    'Hosts.csv': {'id': sqlalchemy.Integer, 'first_name': sqlalchemy.String(100), 'last_name': sqlalchemy.String(100),
                    'email': sqlalchemy.String(100), 'phone_number':sqlalchemy.String(100)},
    'Amenities.csv':{'id':sqlalchemy.Integer,'listing_id':sqlalchemy.Integer,'name':sqlalchemy.String(50),'description':sqlalchemy.String(100)}

}
cnx = getConn()

cur = cnx.cursor()


for csv_file in mydata:
    df = pd.read_csv(csv_file)
    df = df.reset_index(drop=True)
    table_name = csv_file.split('.')[0]
    df.to_sql(con=engine, name=table_name, if_exists="append", index=False,
              dtype=mydata[csv_file])

