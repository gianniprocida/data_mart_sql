use data_mart_airbnb;


create table if not exists Addresses (id int not null,street_name varchar(100),house_number int not null,city varchar(50),
country varchar(50), zip_code int not null);

create table if not exists Hosts (id int not null,first_name varchar(50),last_name varchar(50),email varchar(50),phone_number varchar(50));

create table if not exists Users (id int not null,first_name varchar(50),last_name varchar(50),email varchar(50),phone_number varchar(50),
DoB date,gender enum('Male','Female'),country varchar(50),user_type enum('host','guest'),num_of_reviews int not null);


create table if not exists Listings (id int not null, host_id int not null,title varchar(100),property_type varchar(100),
room_type varchar(100),accommodates int not null, bedrooms int not null, bathrooms int not null,
price_per_night decimal(8,4), address_id int not null);

create table if not exists Reviews (id int not null,listing_id int not null,user_id int not null, text varchar(150),
review_date date,rating int not null,host_response varchar(100));

create table if not exists Amenities (id int not null,listing_id int not null,name varchar(50),
description varchar(100));

