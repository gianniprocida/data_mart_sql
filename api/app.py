#!/usr/bin/env python
from flask import jsonify
from flask import Flask, render_template, request
from kafka import KafkaProducer,KafkaConsumer
from menu import Filter, Filter_by_price, Filter_by_location, Filter_by_rating
from myproducer import connect_kafka_producer,publish_message
import json
import time
import datetime
from menu import getConn,check_connection
import os

app = Flask(__name__)



@app.route('/')
def display_menu():
    return render_template('menu.html')

@app.route('/filter/rating', methods=['GET', 'POST'])
def filter_by_rating_route():
    if request.method == 'POST':
        rating = request.form['rating']
        print("I am here")
        print(rating)
        by_rating = Filter_by_rating()
        rows= by_rating.filter(rating)
        dict_data = []
        for a,b,c,d,f in rows:
           dict_data.append({'a':a,'b':b,'c':c,'d':d,'f':f})
       
        print(dict_data)
          # Perform filtering logic based on rating
          # Return the filtered results
        return jsonify(dict_data)
    return render_template('filter_rating.html')

@app.route('/filter/price', methods=['GET', 'POST'])
def filter_by_price_route():
    if request.method == 'POST':
        min_price = request.form['min_price']
        max_price = request.form['max_price']
        by_price = Filter_by_price()
        rows = by_price.filter(min_price,max_price)
        print(rows)
        # Perform filtering logic based on price range
        # Return the filtered results
        return render_template('filter_results.html',rows=rows)
    return render_template('filter_price.html')



@app.route('/update/users',methods=['GET','POST'])
def update_users():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone_number']
        dob_str = request.form['DoB']
        gender = request.form['gender']
        country = request.form['country']
        user_type = request.form['user_type']
        

        #Validate DoB as a date format
        try:
            dob = datetime.datetime.strptime(dob_str, '%Y-%m-%d')
        except ValueError:
            return 'Invalid date format for DoB',400
        
        #Validate gender
        if gender not in ["Male","Female"]:
            return 'Invalid gender value',400
        
        # Validate user_typr
        if user_type not in ["guest","host"]:
            return 'Invalid user_type'


        row = {
        'first_name': first_name,
        'last_name': last_name,
        'phone_number':phone,
        'email': email,
        'DoB':dob_str,
        'gender':gender,
        'country':country,
        'user_type':user_type
       }
        
        kafka_host = os.environ("kafka_HOST")
        sock_obj = check_connection("kafka-broker-1",9092)
        if sock_obj:
        
            kafka_producer = connect_kafka_producer()
       
           
            #Produce data to the Kafka broker
            if kafka_producer is not None:
                publish_message(kafka_producer,'myusers','test',row)
                print("Producing data to the Kafka broker....")
                kafka_producer.close()
        
                time.sleep(5)

                print("We successfully produced some data...")
                print(" ")


                consumer = KafkaConsumer('myusers', auto_offset_reset='earliest',
                                bootstrap_servers=['kafka-broker-1:9092'], api_version=(0, 10), consumer_timeout_ms=1000)
              
        
                mysql_host=os.environ.get('mysql_HOST')

                sock_obj = check_connection(mysql_host,3306)

                if sock_obj:
                    cnx = getConn()
                    cur = cnx.cursor()

                    if cnx:
                
                        #Query the max id in the Users table
                        cur.execute("""select max(id) from Users""")
                        res = cur.fetchone()
                        max_id = res[0] + 1
                
                        print("Ready to consume data...")
                        for msg in consumer:
                    
                            mymsg = msg.value.decode('utf-8')
                            json_data = json.loads(mymsg)
                            fn = json_data['first_name']
                            ln = json_data['last_name']
                            email = json_data['email']
                            phone = json_data['phone_number']
                            dob = json_data['DoB']
                            gender = json_data['gender']
                            country = json_data['country']
                            user_type = json_data['user_type']
                            print(" ")
                            time.sleep(5)
                            print("Ready to load data to mysql database...")


                            cur.execute("""INSERT INTO Users (id, first_name, last_name, email, phone_number, DoB, gender, country, user_type)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", (max_id, fn, ln, email, phone, dob, gender, country, user_type))

                            cnx.commit() 
                        consumer.close()
                        print(" ")
                        print("Let's see if the record was added to the table")
                        query = "SELECT * FROM Users ORDER BY id DESC LIMIT 1"

                        cur.execute(query)

                        res = cur.fetchone()
                        print(res)

                    else:
                        print("Can't connect to mysql container. Exit...")

                else:
                    print("Can't connect to mysql container. Exit...")
            else:
                print("Can't connect to the Kafka-broker. Exit...")
        else:
            print("Can't connect to Kafka container. Exit..")
        # db_file = 'my_database.db'

        # # Create a table if it doesn't exist

        # # Connect to SQLite database
        # conn = sqlite3.connect(db_file)
        # cursor = conn.cursor()
        # cursor.execute('''CREATE TABLE IF NOT EXISTS my_table
        #         (id INTEGER PRIMARY KEY, attr1 TEXT,attr2 TEXT, attr3 TEXT,
        #                attr4 TEXT,attr5 TEXT,attr6 TEXT,attr7 TEXT)''')
        # conn.commit()



        # print("Kafka:",kafka_producer)
        # print(message)
    #     print(message)
    #     topic = 'mytest'
    #     _producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))
    #     print(" ")
    #     print(_producer)
    #     key_bytes = bytes('myk', encoding='utf-8')
    #     _producer.send(topic,key=key_bytes,value=message.encode('utf-8'))
    #     _producer.flush()
      
    #     if _producer is not None:
    #         print("it s not okay")
    #         _producer.close()

    #     # kafka_producer.flush()

    #     # print(type(first_name))

      

    #    # if kafka_producer is not None:
    #     #     kafka_producer.close()

    #     consumer = KafkaConsumer(topic, auto_offset_reset='earliest',
    #                         bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=1000)
    
    #     for msg in consumer:
    #       print(msg.value)
    #     consumer.close()
    # sleep(5)


    return render_template('update_Users.html') 

@app.route('/update/reservations',methods=['GET','POST'])
def update_reservations():
    if request.method == 'POST':
        print("welcome")

    return render_template('update_Users.html') 


@app.route('/quit')
def quit():
    return "Goodbye!"
#app.run(debug=True)
app.run(host="0.0.0.0")
