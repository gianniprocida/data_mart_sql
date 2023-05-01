use data_mart_airbnb;



alter table Listings add constraint foreign key (address_id) references Listing_addresses(id);

alter table Listings add constraint foreign key (host_id) references Users(id);

alter table Reviews add constraint foreign key (listing_id) references Listings(id);

alter table Reviews add constraint foreign key (user_id) references Users(id);

alter table Amenities add constraint foreign key (listing_id) references Listings(id);

alter table Messages add constraint users_id_fk_sender_id foreign key (sender_id) references Users(id);

alter table Messages add constraint users_id_fk_recipient_id foreign key (recipient_id) references Users(id);

alter table Payments add constraint users_id_fk_payer_id foreign key (payer_id) references Users(id);

alter table Payments add constraint users_id_fk_payee_id foreign key (payee_id) references Users(id);

