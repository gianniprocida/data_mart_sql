use data_mart_airbnb;


alter table Addresses add primary key (id);

alter table Hosts add primary key (id);

alter table Listings add primary key (id);

alter table Users add primary key (id);

alter table Reviews add primary key (id);

alter table Amenities add primary key (id);
