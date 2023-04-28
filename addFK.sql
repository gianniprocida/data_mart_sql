use data_mart_airbnb;



alter table Listings add constraint foreign key (address_id) references Addresses(id);

alter table Listings add constraint foreign key (host_id) references Hosts(id);

alter table Reviews add constraint foreign key (listing_id) references Listings(id);

alter table Amenities add constraint foreign key (listing_id) references Listings(id);
