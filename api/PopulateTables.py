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


def populateTables():
    engine = create_engine("""mysql+mysqlconnector://{user}:{password}@{host}/{db}""".
                           format(user="root", host="localhost", password="Chimica90$", db="datamart_airbnb"))

    for csv_file in mydata:
        df = pd.read_csv(csv_file)
        df = df.reset_index(drop=True)
        table_name = csv_file.split('.')[0]
        df.to_sql(con=engine, name=table_name, if_exists="append", index=False,
                  dtype=mydata[csv_file])


if __name__ == '__main__':

    mydata = {
        'Users.csv': {'id': sqlalchemy.Integer, 'first_name': sqlalchemy.String(100), 'last_name': sqlalchemy.String(100), 'username': sqlalchemy.String(200), 'email': sqlalchemy.String(100), 'phone_number': sqlalchemy.String(100),
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

        'Payments.csv': {'id': sqlalchemy.Integer, 'payment_method': sqlalchemy.String(100),
                         'payment_date': Date(), 'amount': sqlalchemy.Float},

        'Reservations.csv': {'id': sqlalchemy.Integer, 'guest_id': sqlalchemy.Integer, 'listing_id': sqlalchemy.Integer, 'check_in_date': Date(),
                             'check_out_date': Date(), 'total_cost': sqlalchemy.Integer},

        'ListingsAmenities.csv': {'id': sqlalchemy.Integer, 'listing_id': sqlalchemy.Integer, 'amenitiy_id': sqlalchemy.Integer},

        'PaymentsReservations.csv': {'id': sqlalchemy.Integer, 'payment_id': sqlalchemy.Integer, 'reservation_id': sqlalchemy.Integer},

        'Availabilities.csv': {'id': sqlalchemy.Integer, 'listing_id': sqlalchemy.Integer, 'start_date': Date(), 'end_date': Date(),
                               'created_at': Date(), 'updated_at': Date()},

        'ListingsAvailabilities.csv': {'id': sqlalchemy.Integer, 'listing_id': sqlalchemy.Integer, 'availability_id': sqlalchemy.Integer}
    }

    populateTables()
