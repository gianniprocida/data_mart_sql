from faker import Faker
import random
import os
def generate_fake_addresses():
    combined = f"id,street_name,house_number,city,state,zip_code\n"

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
      state = fake.country()

      # Generate a fake zip code
      zip_code = fake.zipcode()


      combined = f"{id},{street_name},{house_number},{city},{state},{zip_code}\n"
      print(combined)
      with open("Addresses.csv","a") as f:
        f.write(combined)
  
      


def generate_fake_listings():
    combined = f"id,title,property_type,room_type,accommodates,bedrooms,bathrooms,price_per_night,address_id\n"
    

    fake = Faker()

    with open("Listings.csv","w") as f:
      f.write(combined)
    mylist = [1,2,3,4,5]
    for i in range(5):
       id = i
       title = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
       property_type = random.choice(['apartment', 'house', 'villa'])
       room_type = random.choice(['private room', 'shared room', 'entire home/apt'])
       accommodates = random.randint(1, 10)
       bedrooms = random.randint(1, 6)
       bathrooms = random.randint(1, 3)
       price_per_night = random.randint(50, 500)
       address_id = mylist.pop()
    



       combined = f"{id},{title},{property_type},{room_type},{accommodates},{bedrooms},{bathrooms},{price_per_night},{address_id}\n"
       print(combined)
       with open("Listings.csv","a") as f:
         f.write(combined)
  

