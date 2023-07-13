#!/usr/bin/env python
from flask import jsonify
from flask import Flask, render_template, request
from kafka import KafkaProducer,KafkaConsumer
from menu import Filter, Filter_by_price, Filter_by_location, Filter_by_rating
from myproducer import connect_kafka_producer,publish_message
import json
from menu import getConn

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
        DoB = request.form['DoB']
        gender = request.form['gender']
        country = request.form['country']
        user_type = request.form['user_type']
        print(first_name,last_name,DoB,gender,country)
        

        row = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'DoB':DoB,
        'gender':gender,
        'country':country,
        'user_type':user_type
       }

       

        kafka_producer = connect_kafka_producer()

        if kafka_producer is not None:
            print(kafka_producer)
            publish_message(kafka_producer,'myusers','hello',row)
            print(row)
            kafka_producer.close()

       # consumer = KafkaConsumer('myusers', auto_offset_reset='earliest',
        #                      bootstrap_servers=['localhost:9092'], api_version=(0, 10), consumer_timeout_ms=1000)
        id = 24
        for msg in consumer:
          
          mymsg = msg.value.decode('utf-8')
          
          fn = mymsg['first_name']
          ln = mymsg['last_name']
          email = mymsg['email']
          DB = mymsg['DoB']
          gender = mymsg['gender']
          country = mymsg['country']
          user_type = mymsg['user_type']
          print(fn,ln,email,DB)
          cnx = getConn()
          cur = cnx.cursor()

          cur.execute("""insert into Users (id,first_name,last_name,email,phone_number,DoB,gender,country,user_type) values (?,?,?,?,?,?,?,?)""",(id,fn,ln,email,DB,gender,country,user_type))
          cnx.commit()
        consumer.close()
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
app.run(debug=True)
#app.run(host="0.0.0.0")
