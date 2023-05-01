from faker import Faker
import random
import os
import csv 

def generate_fake_listing_addresses():
    combined = f"id,street_name,house_number,city,country,zip_code\n"

    with open("Listing_addresses.csv","w") as f:
      f.write(combined)

    for i in range(13):
      id = i+1
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
      with open("Listing_addresses.csv","a") as f:
        f.write(combined)




def generate_fake_user_addresses():
    combined = f"id,street_name,house_number,city,country,zip_code\n"

    with open("User_addresses.csv","w") as f:
      f.write(combined)

    for i in range(20):
      id = i+1
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
      with open("User_addresses.csv","a") as f:
        f.write(combined)

  

def generate_fake_listings():
    combined = f"id,host_id,title,property_type,room_type,accommodates,bedrooms,bathrooms,price_per_night,address_id\n"
    myaddress_id = [1,2,3,4,5,6,7,8,9,10,11]
    myhost_id = [4,3,2,1,5,6,7,8,9,11,10]
    mytitle = ['Grand Hotel','Serenity Spa & Resort','Hotel de Paris','The Four Seasons',\
               'Hilton Hotels & Resorts','The Waldorf Astoria','The Plaza Hotel','The Mandarin Oriental',\
                'The Peninsula','Park Hyatt','Hilltop Hideaway']
   
    with open("Listings.csv","w") as f:
      f.write(combined)
  

    for i in range(11):
       fake = Faker()
       id = i + 1
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
  

def generate_fake_hosts():
    # cannor use hosts table
    combined = f"id,first_name,last_name,email,phone_number\n"

    with open("Hosts.csv","w") as f:
      f.write(combined)
  
    for i in range(13):
       id = i + 1
       fake = Faker()
       first_name = fake.first_name()
       last_name = fake.last_name()
       email = fake.email()
       phone_number = fake.phone_number()

       combined = f"{id},{first_name},{last_name},{email},{phone_number}\n"
       print(combined)
       with open("Hosts.csv","a") as f:
         f.write(combined)


def generate_fake_reviews():
    combined = f"id,listing_id,user_id,content,review_date,rating,host_response\n"
    mylisting_id = [5,1,2,3,3,4,4,10,11,8]
    myuser_id = [12,13,14,15,16,17,18,19,20,21]
    fake = Faker()

    with open("Reviews.csv","w") as f:
      f.write(combined)
  
    for i in range(9):
       id = i+1
       listing_id = mylisting_id.pop()
       user_id = myuser_id.pop()
       content = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
       review_date = fake.date_between(start_date='-5y', end_date='today')
       rating = random.randint(1,6)
       host_response = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
       combined = f"{id},{listing_id},{user_id},{content},{review_date},{rating},{host_response}\n"
       print(combined)
       with open("Reviews.csv","a") as f:
         f.write(combined)
  


def generate_fake_users():
    combined = f"id,first_name,last_name,email,phone_number,DoB,gender,country,user_type\n"
    fake = Faker()
    guest_list =["guest"]*10
    host_list = ["host"]*11
    tot = guest_list + host_list
    with open("Users.csv","w") as f:
      f.write(combined)
  
    for i in range(21):
       id = i+1
       first_name = fake.first_name()
       last_name = fake.last_name()
       email = fake.email()
       phone_number = fake.phone_number()
       fake_dob = fake.date_of_birth(minimum_age=18, maximum_age=100)
       DoB = fake_dob.strftime('%Y-%m-%d')
       gender = random.choice(['Female', 'Male'])
       country = fake.country()
       user_type = tot.pop()

       combined = f"{id},{first_name},{last_name},{email},{phone_number},{DoB},{gender},{country},{user_type}\n"
       print(combined)
       with open("Users.csv","a") as f:
         f.write(combined)



if __name__=='__main__':
   #Run the script to generate Host.csv,Addresses.csv,Listings.csv,Reviews.csv, and Users.csv
   try:
      os.remove("Listing_addresses.csv")
      os.remove("Reviews.csv")
      os.remove("Users.csv")
      os.remove("Listings.csv")
      os.remove("User_addresses.csv")
   except FileNotFoundError as e:
      print(f"{e} already deleted")
   finally:
      generate_fake_listing_addresses()
      generate_fake_listings()
      generate_fake_reviews()
      generate_fake_users()
      generate_fake_user_addresses()