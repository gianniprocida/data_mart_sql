use data_mart_airbnb;
 /*
 create table listings (id int not null, host_id int, description varchar(100), location
*/
create table if not exists Addresses (id int not null,street varchar(100),house_number int not null,zip int not null,
city varchar(50), country varchar(50), primary key(id));

create table if not exists Listings (id int not null, title varchar(100),property_type varchar(100),
room_type varchar(100),accommodates int not null, bedrooms int not null, bathrooms int not null,
price_per_night decimal(8,4), address_id int not null, primary key(id),
constraint fk_address foreign key (address_id) references Addresses(id))
