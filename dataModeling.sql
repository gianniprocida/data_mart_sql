use data_mart_airbnb;

create table if not exists Addresses (id int not null,street varchar(100),house_number int not null,zip int not null,
city varchar(50), country varchar(50), primary key(id));

create table if not exists Hosts (id int not null,first_name varchar(50),last_name varchar(50),email varchar(50),phone_number varchar(50),primary key(id));

create table if not exists Listings (id int not null, host_id int not null,title varchar(100),property_type varchar(100),
room_type varchar(100),accommodates int not null, bedrooms int not null, bathrooms int not null,
price_per_night decimal(8,4), address_id int not null, primary key(id),
constraint fk_address foreign key (address_id) references Addresses(id),
constraint fk_host foreign key(host_id) references Hosts(id));

create table if not exists Reviews (id int not null,listing_id int not null,user_id int not null, description varchar(150),
review_date date,rating int not null,host_response varchar(100),primary key(id),
constraint fk_listing foreign key(listing_id) references Listings(id));

create table if not exists Users (id int not null,first_name varchar(50),last_name varchar(50),email varchar(50),phone_number varchar(50),
DoB date,Gender enum('Male','Female'),country varchar(50),user_type enum('host','guest'),num_of_reviews int not null,primary key(id));


create table if not exists wewe (id int not null,first_name varchar(50),last_name varchar(50),email varchar(50),phone_number varchar(50),primary key(id));

/*
0	1	Protect left bar pattern amount.	house	private room	5	2	1	301	5
*
insert into Listings (id,host_id,title,property_type,room_type,accommodates,bedrooms,bathrooms,price_per_night,address_id) values (0,1,"Protect","House","Private",5,2,1,5);
/*
