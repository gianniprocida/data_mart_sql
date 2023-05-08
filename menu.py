from PopulateTables import getConn
import sys
import datetime
import pandas as pd

class Menu:
    def __init__(self,user_name):
        self.choices = {"1": self.filter_by_rating,
                        "2":self.filter_by_price,
                        "3":self.filter_by_amenity,
                        "4":self.filter_by_location,
                        "5":self.book,
                        "6":self.quit}
        self.user_name = user_name
        self.cnx = getConn()

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
    def run(self):
        while True:
            self.display_menu()
            choice = input()
            action = self.choices.get(choice)
            if action and choice in {"1","2","3","4"}:
                inp = input("Enter your choice: ")
                action(inp)
            else:
                action()
    def filter_by_rating(self,rating):
        cur = self.cnx.cursor()
        cur.execute("use data_mart_airbnb")
        query1 = f"""select title,price_per_night from Listings
        where id in (select listing_id from Reviews where rating > "{rating}") limit 4;"""
        cur.execute(query1)
        rows = cur.fetchall()
        for item in rows:
         print("Hotel: {0}, Price_per_night: {1}".format(item[0],float(item[1])))
        print(" ")
        query2 = """select street_name,house_number,city,country,zip_code from Listing_addresses where id in (select address_id from Listings a inner join Reviews b on a.id = b.listing_id where rating > %s);"""
        cur.execute(query2,(rating,))
        rows = cur.fetchall()
        for item in rows:
            print("Street name: {0}, House number: {1}, City: {2}, Country: {3}, Zip code: {4}".format(item[0],
                                                                                                   int(item[1]),item[2],item[3],item[4]))
        print(" ")
    def filter_by_price(self,price):
        cur = self.cnx.cursor()
        cur.execute("use data_mart_airbnb")
        query1 = f"""select title,price_per_night from Listings where price_per_night < %s 
         order by price_per_night limit 4;"""
        cur.execute(query1,(price,))
        rows = cur.fetchall()
        for item in rows:
          print("Hotel: {0}, Price_per_night: {1}".format(item[0],float(item[1])))
        print(" ")
        query2 = f"""select street_name,house_number,city,country,zip_code from Listing_addresses a 
        inner join Listings b on a.id = b.address_id
          where b.price_per_night < %s order by b.price_per_night limit 4;"""
        for item in rows:
            print("Street name: {0}, House number: {1}, City: {2}, Country: {3}, Zip code: {4}".format(item[0],
                                                                                              int(item[1]),item[2],item[3],item[4]))
        print(" ")
        cur.execute(query2,(price,))
    def filter_by_amenity(self,amenity):
        cur = self.cnx.cursor()
        cur.execute("use data_mart_airbnb")

        query1 = f"""select title,price_per_night from Listings where id = 
        (select b.id from Amenities a inner join Listings b on a.listing_id = b.id where name like '%{amenity}%');"""

        cur.execute(query1)
        rows = cur.fetchall()

        for item in rows:
            print("Hotel: {0}, Price_per_night: {1}".format(item[0],float(item[1])))
        print(" ")
         
        query2 = f"""select street_name,house_number,city,country from Listing_addresses 
        where id = (select address_id from Listings where id = 
        (select b.id from Amenities a inner join Listings b on a.listing_id = b.id where name like '%{amenity}%'));"""
      
        cur.execute(query2)
        rows = cur.fetchall()
        for item in rows:
            print("Street name: {0}, House number: {1}, City: {2}, Country: {3}".format(item[0],int(item[1]),item[2],item[3]))
        print(" ")
    def filter_by_location(self,location):
        cur = self.cnx.cursor()
        cur.execute("use data_mart_airbnb")

        query1 = f"""select title,price_per_night from Listings a
        inner join Listing_addresses b on a.address_id = b.id
        where city like '%{location}%' limit 4""" 

        cur.execute(query1)
        rows = cur.fetchall()

        for item in rows:
            print("Hotel: {0}, Price_per_night: {1}".format(item[0],float(item[1])))
        print(" ")
         
        query2 = f"""select street_name,house_number,city,country from Listing_addresses 
        where id = (select address_id from Listings where id = 
        (select a.id from Listings a inner join Listing_addresses b on a.address_id = b.id where city like '%{location}%'));"""
      
        cur.execute(query2)
        rows = cur.fetchall()
        for item in rows:
            print("Street name: {0}, House number: {1}, City: {2}, Country: {3}".format(item[0],int(item[1]),item[2],item[3]))
        print(" ")

    def book(self):
        cur = self.cnx.cursor()
        cur.execute("use data_mart_airbnb")

        query1 = f"""select title,property_type,room_type,price_per_night from Listings"""
        cur.execute(query1) 
        rows = cur.fetchall()
        listings = set()
        for l,_,_,_ in rows:
            listings.add(l)

        print("Available listings: ")
        for item in rows:
            print("Hotel: {0}, Property type: {1}, Room type: {2}, Price per night: {3} ".format(item[0],item[1],item[2],float(item[3])))
        print(" ")
         
        print("Book a reservation of your choice")
        l = input("Enter your choice: ")
        check_in,check_out= input("Enter check_in date, and check_out date separated by spaces: ").split()
        check_in_obj = datetime.datetime.strptime(check_in, '%Y-%m-%d').date()
        check_out_obj = datetime.datetime.strptime(check_out, '%Y-%m-%d').date()
        length_of_period = len(pd.date_range(start=check_in_obj, end=check_out_obj, freq="D"))

        while True:
            try:
               if l in listings:
                   print("ok")
                   cur.execute(f"""select price_per_night*{length_of_period} as tot from Listings where title = '{l}'""")
                   row = cur.fetchone()
                   print(row)
                   total_cost = float(row[0])
                   print(total_cost)
                   print("Total amount: ",total_cost)
                   cur.execute(f"""select id from Listings where title = '{l}'""")
                   row = cur.fetchone()
                   listing_id = row[0]
                   break
               else:
                   raise ValueError
            except ValueError:
                print("Your choice is not available ")
                l = input("Enter your choice").split()
        choice = input("Please type 'y' to proceed with your order or 'n' to exit: ")
        if choice == "y":
            query = """select id from Users where last_name=%s"""
            cur.execute(query,(self.user_name,))
            guest_id = cur.fetchone()[0]
            id = 10 # just for an example
            query = """insert into Reservations (id,guest_id,listing_id,check_in_date,check_out_date,total_cost) 
            values (%s,%s,%s,%s,%s,%s)"""
            print((id,guest_id,listing_id,check_in,check_out,total_cost))
            cur.execute(query,(id,guest_id,listing_id,check_in,check_out,total_cost)) 
            self.cnx.commit()
            print("I'm here")
        else:
            print("Exit...")

    def quit(self):
        sys.exit(0)
        
if __name__=='__main__':
    cnx = getConn()
    cur = cnx.cursor()
    cur.execute("use data_mart_airbnb")
    user_name = input("Enter your name: ")
    query = """select id from Users where last_name=%s"""
    cur.execute(query,(user_name,))
    row = cur.fetchone()
    if not row:
        print("User not in the database")
    else:
        print(f"Welcome {user_name}")
        Menu(user_name).run()

   
#    Menu("hello").run()
# #    l,d = input("Enter your choice and specify the number of days you would like to stay separated by spaces:").split()
   

#      a = Menu("Bennett")
     
#      c = a.cnx.cursor()
#      c.execute("use data_mart_airbnb")
#      rating = 5
#      query2 = """select street_name,house_number,city,country,zip_code from Listing_addresses where id in (select address_id from Listings a inner join Reviews b on a.id = b.listing_id where rating > %s);"""
#      c.execute(query2,(rating,))
#      rows = c.fetchall()
#      print(rows)
     
#     check_in,check_out= input("Enter check_in date, and check_out date separated by spaces:").split()
#     check_in_obj = datetime.datetime.strptime(check_in, '%Y-%m-%d').date()
#     check_out_obj = datetime.datetime.strptime(check_out, '%Y-%m-%d').date()
#     length_of_period = len(pd.date_range(start=check_in_obj, end=check_out_obj, freq="D"))

#     print(length_of_period)
#     l = "Marriot Hotel" 
#    # c.execute(f"""select * from Listings""")
#     query=f"""select price_per_night*{length_of_period} from Listings where title = '{l}'"""

#     c.execute(query)
#    a = (10, 12, 13, '2023-05-01', '2023-05-05', 2250.0) 
    
#     rows = c.fetchall()

   
# 2023-05-01 2023-05-05
    
