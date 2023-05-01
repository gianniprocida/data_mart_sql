from faker import Faker
import random
import os
import csv 
import datetime

def generate_fake_reservations():
    combined = f"id,guest_id,listing_id,check_in_date,check_out_date,total_cost\n"
    mylisting_id = [0,1,2,3,3]
    myguest_id = [0,1,3,4,2]
    myguest_id = [12,14,16,2,1,12]
    with open("Reservations.csv","w") as f:
      f.write(combined)

    for i in range(5):
      id = i

      fake = Faker()
    
      guest_id = myguest_id.pop()
    
      listing_id = mylisting_id.pop()  
      
      check_in_date = fake.date_between(start_date='-5y', end_date='today')
 
      check_out_date = fake.date_between(start_date='-5y', end_date='today')

      total_cost = random.randint(2000, 10000)

      combined = f"{id},{guest_id},{listing_id},{check_in_date},{check_out_date},{total_cost}\n"
   
      with open("Reservations.csv","a") as f:
        f.write(combined)


def generate_fake_payments():
    combined = f"id,reservation_id,payer_id,payee_id,payment_method,payment_date,amount\n"
    myreservation_id = [1,3,5,7,8,2]
    mypayer_id = [12,14,16,2,1,12]
    mypayee_id = [1,2,3,4,4,7]
    start_date = datetime.date(2020, 1, 1)
    end_date = datetime.date(2023, 5, 1)
    delta = end_date - start_date
    

    with open("Payments.csv","w") as f:
      f.write(combined)

    for i in range(5):
      id = i + 1

      fake = Faker()
    
      payer_id = mypayer_id.pop()
    
      payee_id = mypayee_id.pop() 

      reservation_id = myreservation_id.pop()
      
      payment_method = random.choice(['Visa', 'Mastercard', 'American Express'])
  
      random_date = start_date + datetime.timedelta(days=random.randint(0, delta.days))

      payment_date = random_date.strftime('%Y-%m-%d')


      amount = random.randint(2000, 10000)
      
      combined = f"{id},{reservation_id},{payer_id},{payee_id},{payment_method},{payment_date},{amount}\n"
   
      with open("Payments.csv","a") as f:
        f.write(combined)
  


def generate_fake_messages():
    combined = f"id,sender_id,recipient_id,content,date_sent\n"
    mysender_id = [12,12,12,12,12]
    myrecipient_id = [2,2,2,2,2]
    mycontent = ["\"Hi,I'm interested in your listing.Can you tell me more about it?\"",
                 "\"Sure, what would you like to know?\"","\"Is the room available from May 10\"",
                 "\"Yes, it's available. Would you like to make a reservation?\"",
                 "\"Thanks for the information. Can you tell me more about the amenities?\""]
    
    with open("Messages.csv","w") as f:
      f.write(combined)

    for i in range(5):
      id = i

      fake = Faker()
       
      sender_id = mysender_id.pop()

      recipient_id = myrecipient_id.pop()
    
      content = mycontent.pop()
      
      date_sent = fake.date_between(start_date='-5y', end_date='today')

   

      combined = f"{id},{sender_id},{recipient_id},{content},{date_sent}\n"
   
      with open("Messages.csv","a") as f:
        f.write(combined)

def generate_fake_amenities():
    combined = f"id,name,listing_id,description\n"
    mynames = ["Wi-Fi","Kitchen","Pool","Free parking","Air conditioning","Rooftop pool","Private beach access",
               "Fitness center","Sauna and steam room","On-site restaurant or cafe","Spa services"]
    mydescriptions = ["High-speed internet access throughout the property",
    "Fully equipped kitchen",
    "Private outdoor pool for guest use only",
    "Designated parking spot on property for guest use",
    "Central air conditioning system in all rooms",
    "Enjoy a refreshing dip in our rooftop pool with a stunning view of the city",
    "Escape to our private beach and soak up the sun with a tropical cocktail in hand",
    "Stay fit and healthy during your stay with our fully-equipped fitness center",
    "Relax and unwind in our sauna and steam room after a long day of sightseeing",
    "Savor delicious local cuisine without leaving the comfort of your hotel",
"Pamper yourself with a relaxing massage or facial at our on-site spa",
    ]
    mylistingid = [2,1,3,4,5,7,6,8,9,11,10]
    with open("Amenities.csv","w") as f:
      f.write(combined)
  
    for i in range(11):
       id = i + 1
       name = mynames.pop()
       listing_id = mylistingid.pop()
       description = mydescriptions.pop()
       combined = f"{id},{name},{listing_id},{description}\n"
       print(combined)
       with open("Amenities.csv","a") as f:
         f.write(combined)

      


if __name__=='__main__':
   #Run the script to generate Host.csv,Addresses.csv,Listings.csv,Reviews.csv, and Users.csv

    try:
       os.remove("Amenities.csv")
       os.remove("Reservations.csv")
       os.remove("Payments.csv")
       os.remove("Messages.csv")
    except FileNotFoundError as e:
       print(f"{e} already deleted")
    finally:
       generate_fake_payments()
       generate_fake_messages()
       generate_fake_amenities()
       generate_fake_reservations()