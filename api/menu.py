import sys
import datetime
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine, Date, Enum
import pandas as pd
import os,socket


def check_connection(host,port):
    try:
        socket_obj = socket.create_connection((host,port),timeout=5)
        print(f"Connection to the {host} container was successfully established")
        return socket_obj
    except Exception as e:
        print(f"Connection failed: {e}")



def getConn():
    host = os.environ.get('DB_HOST')
    user = os.environ.get('DB_USER')
    password = os.environ.get('DB_PASSWORD')
    cnx = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        db='data_mart_airbnb'
    )
    return cnx


class Filter():
    def __init__(self):
       self.cnx = getConn()
       self.cur = self.cnx.cursor()
       self.cur.execute("use data_mart_airbnb")
    def filter(self):
        pass


class Filter_by_rating(Filter):
    def filter(self,rating):
        query = """select title,price_per_night from Listings
        where id in (select listing_id from Reviews where rating > %s) limit 4;"""
        self.cur.execute(query,(rating,))
        rows = self.cur.fetchall()
        for item in rows:
         print("Hotel: {0}, Price_per_night: {1}".format(item[0],float(item[1])))
        print(" ")
        query2 = """select street_name,house_number,city,country,zip_code from Listing_addresses where id in (select address_id from Listings a inner join Reviews b on a.id = b.listing_id where rating > %s);"""
        self.cur.execute(query2,(rating,))
        rows = self.cur.fetchall()
       
        return rows
class Filter_by_price(Filter):
   def filter(self,min_price,max_price):
      
        query1 = """select title,price_per_night from Listings where price_per_night between %s and %s limit 4""" 

        self.cur.execute(query1,(min_price,max_price))

        rows = self.cur.fetchall()

        for item in rows:
            print("Hotel: {0}, Price_per_night: {1}".format(item[0],float(item[1])))
        print(" ")

        query2 = """select street_name,house_number,city,country,zip_code from Listing_addresses a 
        inner join Listings b on a.id = b.address_id where b.price_per_night between %s and %s order by b.price_per_night limit 4;"""
        self.cur.execute(query2,(min_price,max_price))
        rows = self.cur.fetchall()
        return rows
     
class Filter_by_location(Filter):
   def filter(self,location):
        
        query1 = f"""select title,price_per_night from Listings a
        inner join Listing_addresses b on a.address_id = b.id
        where city like '%{location}%' limit 4""" 

        self.cur.execute(query1)
        rows = self.cur.fetchall()

        for item in rows:
            print("Hotel: {0}, Price_per_night: {1}".format(item[0],float(item[1])))
        print(" ")
         
        query2 = f"""select street_name,house_number,city,country from Listing_addresses 
        where id = (select address_id from Listings where id = 
        (select a.id from Listings a inner join Listing_addresses b on a.address_id = b.id where city like '%{location}%'));"""
      
        self.cur.execute(query2)
        rows = self.cur.fetchall()
        for item in rows:
            print("Street name: {0}, House number: {1}, City: {2}, Country: {3}".format(item[0],int(item[1]),item[2],item[3]))
        print(" ")

class Filter_by_amenity(Filter):
    def filter(self,amenity):
        
        query1 = f"""select title,price_per_night from Listings where id = 
        (select b.id from Amenities a inner join Listings b on a.listing_id = b.id where name like '%{amenity}%');"""

        self.cur.execute(query1)
        rows = self.cur.fetchall()

        for item in rows:
            print("Hotel: {0}, Price_per_night: {1}".format(item[0],float(item[1])))
        print(" ")
         
        query2 = f"""select street_name,house_number,city,country from Listing_addresses 
        where id = (select address_id from Listings where id = 
        (select b.id from Amenities a inner join Listings b on a.listing_id = b.id where name like '%{amenity}%'));"""
      
        self.cur.execute(query2)
        rows = self.cur.fetchall()
        for item in rows:
            print("Street name: {0}, House number: {1}, City: {2}, Country: {3}".format(item[0],int(item[1]),item[2],item[3]))
        print(" ")

class Listing():
    def __init__(self,user_name):
        self.cnx = getConn()
        self.cur = self.cnx.cursor()
        self.cur.execute("use data_mart_airbnb")
        self.user_name = user_name

    @classmethod
    def create_instance(cls,arg):
        if cls.is_valid(arg):
            instance = cls(arg)
            return instance
        else:
            raise ValueError
        
    @staticmethod
    def is_valid(arg):
        cnx = getConn()
        cur = cnx.cursor()
        cur.execute("use data_mart_airbnb")
        query = """select last_name from Users where user_type='host'"""
        cur.execute(query)
        allowed_names = set()
        rows = cur.fetchall()
        for l_n in rows:
            allowed_names.add(l_n[0])
        return arg in allowed_names
    
    def add(self,data1,data2):
        print("Add a listing into Listings table.")
        print("First,add the address into Listing_addresses table")
        userStreet_name = input("Enter street name: ")
        userHouse_number = input("Enter street name: ")
        userCity = input("Enter street name: ")
        userCountry = input("Enter street name: ")
        userZip_code = input("Enter the zip code: ")
        query = """select house_number from Listing_addresses"""
        self.cur.execute(query)
        house_numbers = set()
        rows = self.cur.fetchall()
        for h_n in rows:
            house_numbers.add(h_n[0])
        
        while True:
            try:
                if userHouse_number not in house_numbers:
                    print("ok..ready to add")
                    query = """insert into Listing_addresses (house_number,street_name,city,country,zip_code) 
                    values (%s,%s,%s,%s,%s)"""
                    self.cur.execute(query,(userHouse_number,userStreet_name,userCity,userCountry,userZip_code))
                    self.cnx.commit()
                    print("ready to add new listing")
                    query = """select id from Users where username = %s"""
                    self.cur.execute(query,(self.user_name))
                    user_id = self.cur.fetchone()[0]
                    userTitle = input("Enter title: ")
                    userProperty_type = input("Enter property type: ")
                    userRoom_type = input("Enter room type: ")
                    userAccomodates = input("Enter the number of accomodates: ")
                    userBedrooms = input("Enter the number of bedrooms: ")
                    userBathrooms = input("Enter number of bathrooms: ")
                    userPrice = input("Enter the price: ")
                    query = """insert into Listings (user_id,title,property_type,room_type,accomodates,bedrooms,bathrooms,price_per_night,house_number) 
                    values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                    self.cur.execute(query,(user_id,userTitle,userProperty_type,userRoom_type,
                                            userAccomodates,userBedrooms,userBathrooms,userPrice,userHouse_number))
                    self.cnx.commit()

                else:
                    raise ValueError("Address already in the system")

            except ValueError:
                print("hello")
            


class Reservation():
    def __init__(self,user_name):
        self.cnx = getConn()
        self.cur = self.cnx.cursor()
        self.cur.execute("use data_mart_airbnb")
        self.user_name = user_name
    def book(self):
        print("Book a reservation of your choice.")
        query = """select title,property_type,room_type,price_per_night from Listings"""
        self.cur.execute(query)
        rows = self.cur.fetchall()
        titles = set()
        for title,_,_,_ in rows:
            titles.add(title[0])

        mytitle = input("Enter your choice: ")
        check_in,check_out= input("Enter check_in date, and check_out date separated by spaces: ").split()
        check_in_obj = datetime.datetime.strptime(check_in, '%Y-%m-%d').date()
        check_out_obj = datetime.datetime.strptime(check_out, '%Y-%m-%d').date()
        length_of_period = len(pd.date_range(start=check_in_obj, end=check_out_obj, freq="D"))

        while True:
            try: 
                if mytitle in titles:
                    query = f"""select price_per_night*{length_of_period} from Listings where title = '{mytitle}'"""
                    self.cur.execute(query)
                    row = self.cur.fetchone()
                    total_cost = float(row[0])
                    print("Total amount: ",total_cost)
                    query = """select id from Listings where title = %s"""
                    self.cur.execute(query,(total_cost,))
                    row = self.cur.fetchone()
                    listing_id = row[0]
                    break
                else:
                    raise ValueError
                    
            except ValueError:
                print("Your choice is not available ")
                mytitle = input("Enter your choice: ")
        choice = input("Please type 'y' to proceed with your order or 'n' to exit: ")
        if choice == "y":
            query = """select id from Users where user_name=%s"""
            self.cur.execute(query,(self.user_name,))
            guest_id = self.cur.fetchone()[0]
            id = 10 # just for an example
            query = """insert into Reservations (id,guest_id,listing_id,check_in_date,check_out_date,total_cost) 
            values (%s,%s,%s,%s,%s,%s)"""
            print((id,guest_id,listing_id,check_in,check_out,total_cost))
            self.cur.execute(query,(id,guest_id,listing_id,check_in,check_out,total_cost)) 
            self.cnx.commit()
            print("I'm here")
        else:
            print("Exit...")


class Menu:
    def __init__(self,user_name):
        self.user_name = user_name
        self.choices = {"1":Filter_by_rating(),"2":Filter_by_price(),
                        "3":Filter_by_location(),"4":Filter_by_amenity(),
                        "5":Reservation(user_name),"6":self.quit}
    
    def display_menu(self):
        print("""Database for Airbnb usage
           Options available for users

           1. Filter by rating
           2. Filter by price
           3. Filter by amenity
           4. Filter by location
           5. Book a reservation 
           6. Quit
           """)
    
    def quit(self):
        sys.exit(0)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            action = self.choices.get(choice)
            if action and choice in {"1","2","3","4"}:
                if choice == "1":
                    rating = input("Enter your rating: ")
                    action.filter(rating)
                elif choice == "2":
                    min_price,max_price = input("Enter your range: ")
                    action.filter(min_price,max_price)
                elif choice == "3":
                    amenity = input("Enter")
                    action.filter(amenity)
                elif choice == "4":
                    location = input("Enter your city")
                    action.filter(location)
            else:

                if action and choice in {"5","6"}:
                   action = self.choices.get(choice)
                   if choice == "5":
                    action.book()
                else:
                    action()

                    

if __name__=='__main__':
#    myf = Filter_by_rating()
#    print("Rating greater than 4")
#    myf.filter(4)
#    print(" ")
#    print(" Price between 200 and 400")
#    my = Filter_by_price()
#    my.filter(200,400)
#    print(" ")
#    print(" Ghent ")
#    myf = Filter_by_location()
#    myf.filter("Ghent")
   myl = Listing.create_instance('Trevino')


# class Menu:
#     def __init__(self,user_name):
#         self.choices = {}
#         # self.choices = {"1": self.filter_by_rating,
#         #                 "2":self.filter_by_price,
#         #                 "3":self.filter_by_amenity,
#         #                 "4":self.filter_by_location,
#         #                 "5":self.book,
#         #                 "6":self.quit}
#         # self.user_name = user_name

#     def display_menu(self):
#         print("""Database for Airbnb usage
#            Options available for users

#            1. Filter by rating
#            2. Filter by price
#            3. Filter by amenity
#            4. Filter by location
#            5. Book a reservation 
#            6. Quit
#            """)
    
#     def run(self):
#         while True:
#             self.display_menu()
#             choice = input()
#             action = self.choices.get(choice)
#             if action and choice in {"1","2","3","4"}:
#                 inp = input("Enter your choice:")
#                 if choice == "1":

