from faker import Faker
import random
import os
import csv 

def generate_fake_addresses():
    combined = f"id,street_name,house_number,city,country,zip_code\n"

    with open("Addresses.csv","w") as f:
      f.write(combined)

    for i in range(10):
      id = i
      fake = Faker()
      # Generate a fake street address
      street_name = fake.street_name()

      # Generate house number
 
      house_number = fake.building_number()

      # Generate a fake city
      city = fake.city()

      # Generate a fake state
      country = fake.country()

      # Generate a fake zip code
      zip_code = fake.zipcode()


      combined = f"{id},{street_name},{house_number},{city},{country},{zip_code}\n"
      print(combined)
      print(combined)
      with open("Addresses.csv","a") as f:
        f.write(combined)
  
      


def generate_fake_listings():
    combined = f"id,host_id,title,property_type,room_type,accommodates,bedrooms,bathrooms,price_per_night,address_id\n"
    myaddress_id = [1,2,3,4,5]
    myhost_id = [4,0,2,2,1]
    mytitle = ['Grand Hotel','The Ritz-Carlton''Hotel de Paris','The Four Seasons',\
               'Hilton Hotels & Resorts','The Waldorf Astoria']
    # The Plaza Hotel
    # The Mandarin Oriental
    # The Peninsula
    # Park Hyatt

    fake = Faker()

    with open("Listings.csv","w") as f:
      f.write(combined)
  

    for i in range(5):
       id = i
       host_id = myhost_id.pop()
       title = mytitle.pop()
       property_type = random.choice(['apartment', 'house', 'villa'])
       room_type = random.choice(['private room', 'shared room', 'entire home/apt'])
       accommodates = random.randint(1, 10)
       bedrooms = random.randint(1, 6)
       bathrooms = random.randint(1, 3)
       price_per_night = random.randint(50, 500)
       address_id = myaddress_id.pop()
    



       combined = f"{id},{host_id},{title},{property_type},{room_type},{accommodates},{bedrooms},{bathrooms},{price_per_night},{address_id}\n"
       print(combined)
       with open("Listings.csv","a") as f:
         f.write(combined)
  

def generate_fake_host():
    combined = f"id,first_name,last_name,email,phone_number\n"


    fake = Faker()

    with open("Hosts.csv","w") as f:
      f.write(combined)
  
    for i in range(5):
       id = i
       first_name = fake.first_name()
       last_name = fake.last_name()
       email = fake.email()
       phone_number = fake.phone_number()

       combined = f"{id},{first_name},{last_name},{email},{phone_number}\n"
       print(combined)
       with open("Hosts.csv","a") as f:
         f.write(combined)


def generate_fake_reviews():
    combined = f"id,listing_id,user_id,text,review_date,rating,host_response\n"
    mylisting_id = [0,1,2,3,3]
    myuser_id = [1,2,3,3,3]
    fake = Faker()

    with open("Reviews.csv","w") as f:
      f.write(combined)
  
    for i in range(5):
       id = i
       listing_id = mylisting_id.pop()
       user_id = myuser_id.pop()
       text = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
       review_date = fake.date_between(start_date='-5y', end_date='today')
       rating = random.randint(1,6)
       host_response = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
       combined = f"{id},{listing_id},{user_id},{text},{review_date},{rating},{host_response}\n"
       print(combined)
       with open("Reviews.csv","a") as f:
         f.write(combined)
  


def generate_fake_users():
    combined = f"id,first_name,last_name,email,phone_number,DoB,gender,country,user_type,num_of_reviews\n"
    mylisting_id = [0,1,2,3,3]
    myuser_id = [1,2,3,3,3]
    fake = Faker()

    with open("Users.csv","w") as f:
      f.write(combined)
  
    for i in range(5):
       id = i
       first_name = fake.first_name()
       last_name = fake.last_name()
       email = fake.email()
       phone_number = fake.phone_number()
       fake_dob = fake.date_of_birth(minimum_age=18, maximum_age=100)
       DoB = fake_dob.strftime('%Y-%m-%d')
       gender = random.choice(['Female', 'Male'])
       country = fake.country()
       user_type = random.choice(['guest', 'host'])
       num_of_reviews = random.randint(1,6)

       combined = f"{id},{first_name},{last_name},{email},{phone_number},{DoB},{gender},{country},{user_type},{num_of_reviews}\n"
       print(combined)
       with open("Users.csv","a") as f:
         f.write(combined)

def generate_fake_amenities():
    combined = f"id,name,listing_id,description\n"
    mynames = ["Wi-Fi","Kitchen","Pool","Free parking","Air conditioning"]
    mydescriptions = ["High-speed internet access throughout the property",
    "Fully equipped kitchen","Private outdoor pool for guest use only",
    "Designated parking spot on property for guest use","Central air conditioning system in all rooms"]

    myid = [4,3,2,1,0]
    mylistingid = [0,1,2,3,4]
    with open("Amenities.csv","w") as f:
      f.write(combined)
  
    for i in range(len(myid)):
       id = myid.pop()
       name = mynames.pop()
       listing_id = mylistingid.pop()
       description = mydescriptions.pop()
       combined = f"{id},{name},{listing_id},{description}\n"
       print(combined)
       with open("Amenities.csv","a") as f:
         f.write(combined)


if __name__=='__main__':
   #Run the script to generate Host.csv,Addresses.csv,Listings.csv,Reviews.csv, and Users.csv
   os.remove("Amenities.csv")
   os.remove("Reviews.csv")
   os.remove("Addresses.csv")
   os.remove("Users.csv")
   os.remove("Hosts.csv")
   os.remove("Listings.csv")
   generate_fake_host()
   generate_fake_addresses()
   generate_fake_listings()
   generate_fake_reviews()
   generate_fake_users()
   generate_fake_amenities()