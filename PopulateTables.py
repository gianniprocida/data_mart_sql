import mysql.connector
from sqlalchemy import create_engine, Date, Enum
import pandas as pd
import sqlalchemy


def getConn():
    cnx = mysql.connector.connect(
        host="localhost",
        user="gprocida",
        password="HelloWorld"
    )

    return cnx


engine = create_engine("""mysql+mysqlconnector://{user}:{password}@{host}/{db}""".
                       format(user="gprocida", host="localhost", password="HelloWorld", db="data_mart_airbnb"))


mydata = {
    'Users.csv': {'id': sqlalchemy.Integer, 'first_name': sqlalchemy.String(100), 'last_name': sqlalchemy.String(100), 'email': sqlalchemy.String(100), 'phone_number': sqlalchemy.String(100),
                  'DoB': Date(), 'gender': Enum("Male", "Female"), 'country': sqlalchemy.String(100), 'user_type': Enum("host", "guest")},

    'Listing_addresses.csv': {'id': sqlalchemy.Integer, 'street_name': sqlalchemy.String(200), 'house_number': sqlalchemy.Integer, 'city': sqlalchemy.String(100), 'country': sqlalchemy.String(100), 'zip_code': sqlalchemy.Integer},

    'User_addresses.csv': {'id': sqlalchemy.Integer, 'street_name': sqlalchemy.String(200), 'house_number': sqlalchemy.Integer, 'city': sqlalchemy.String(100), 'country': sqlalchemy.String(100), 'zip_code': sqlalchemy.Integer},

    'Listings.csv': {'id': sqlalchemy.Integer, 'host_id': sqlalchemy.Integer, 'title': sqlalchemy.String(200),
                     'property_type': Enum('apartment', 'house', 'villa'), 'room_type': Enum('private room', 'shared room', 'entire home/apt'), 'accommodates': sqlalchemy.Integer,
                     'bedrooms': sqlalchemy.Integer, 'bathrooms': sqlalchemy.Integer,
                     'price_per_night': sqlalchemy.Float, 'address_id': sqlalchemy.Integer},

    'Reviews.csv': {'id': sqlalchemy.Integer, 'listing_id': sqlalchemy.Integer, 'user_id': sqlalchemy.Integer,
                    'content': sqlalchemy.String(200), 'review_date': Date(), 'rating': sqlalchemy.Integer, 'host_response': sqlalchemy.String(100)},

    'Amenities.csv': {'id': sqlalchemy.Integer, 'listing_id': sqlalchemy.Integer, 'name': sqlalchemy.String(100), 'description': sqlalchemy.String(200)},

    'Messages.csv': {'id': sqlalchemy.Integer, 'sender_id': sqlalchemy.Integer, 'recipient_id': sqlalchemy.Integer, 'content': sqlalchemy.String(300),
                     'date_sent': Date()},

    'Payments.csv': {'id': sqlalchemy.Integer, 'reservation_id': sqlalchemy.Integer, 'payer_id': sqlalchemy.Integer, 'payment_method': sqlalchemy.String(100),
                     'payment_date': Date(),'amount':sqlalchemy.Float},

    'Reservations.csv': {'id': sqlalchemy.Integer, 'guest_id': sqlalchemy.Integer, 'listing_id': sqlalchemy.Integer, 'check_in_date': Date(),
                         'check_out_date': Date(), 'total_cost': sqlalchemy.Integer}

}
cnx = getConn()

cur = cnx.cursor()


for csv_file in mydata:
    df = pd.read_csv(csv_file)
    df = df.reset_index(drop=True)
    table_name = csv_file.split('.')[0]
    df.to_sql(con=engine, name=table_name, if_exists="append", index=False,
              dtype=mydata[csv_file])
