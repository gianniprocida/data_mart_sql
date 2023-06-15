-- MySQL dump 10.13  Distrib 5.7.41, for Linux (x86_64)
--
-- Host: localhost    Database: data_mart_airbnb
-- ------------------------------------------------------
-- Server version	5.7.41-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Amenities`
--
use data_mart_airbnb;


DROP TABLE IF EXISTS `Amenities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Amenities` (
  `id` int(11) NOT NULL,
  `listing_id` int(11) NOT NULL,
  `name` varchar(150) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `listing_id` (`listing_id`),
  CONSTRAINT `Amenities_ibfk_1` FOREIGN KEY (`listing_id`) REFERENCES `Listings` (`id`),
  CONSTRAINT `Amenities_ibfk_2` FOREIGN KEY (`listing_id`) REFERENCES `Listings` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Amenities`
--

LOCK TABLES `Amenities` WRITE;
/*!40000 ALTER TABLE `Amenities` DISABLE KEYS */;
INSERT INTO `Amenities` VALUES (1,10,'Spa services','Pamper yourself with a relaxing massage or facial at our on-site spa'),(2,11,'On-site restaurant or cafe','Savor delicious local cuisine without leaving the comfort of your hotel'),(3,9,'Sauna and steam room','Relax and unwind in our sauna and steam room after a long day of sightseeing'),(4,8,'Fitness center','Stay fit and healthy during your stay with our fully-equipped fitness center'),(5,6,'Private beach access','Escape to our private beach and soak up the sun with a tropical cocktail in hand'),(6,7,'Rooftop pool','Enjoy a refreshing dip in our rooftop pool with a stunning view of the city'),(7,5,'Air conditioning','Central air conditioning system in all rooms'),(8,4,'Free parking','Designated parking spot on property for guest use'),(9,3,'Pool','Private outdoor pool for guest use only'),(10,1,'Kitchen','Fully equipped kitchen'),(11,2,'Wi-Fi','High-speed internet access throughout the property');
/*!40000 ALTER TABLE `Amenities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Listing_addresses`
--

DROP TABLE IF EXISTS `Listing_addresses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Listing_addresses` (
  `id` int(11) NOT NULL,
  `street_name` varchar(100) DEFAULT NULL,
  `house_number` int(11) NOT NULL,
  `city` varchar(50) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `zip_code` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Listing_addresses`
--

LOCK TABLES `Listing_addresses` WRITE;
/*!40000 ALTER TABLE `Listing_addresses` DISABLE KEYS */;
INSERT INTO `Listing_addresses` VALUES (1,'Davenport Fields',131,'Bakerland','Guatemala',95925),(2,'Smith Light',99454,'New Tracyview','Colombia',54577),(3,'John Springs',79701,'Batestown','Namibia',83448),(4,'Edwards Union',2165,'West Emily','Turks and Caicos Islands',20270),(5,'Courtney Center',3176,'Alexandriaport','Liechtenstein',74363),(6,'John Heights',598,'Smithborough','Jersey',54920),(7,'Kathleen Lodge',5073,'Matthewland','Saudi Arabia',48509),(8,'Brown Heights',55012,'East Bryan','Taiwan',96010),(9,'Carly Ridge',21,'Smallhaven','Lebanon',78457),(10,'Sean Run',39818,'South Chloeport','Greenland',88025),(11,'Schultz Island',505,'Briannaside','Palestinian Territory',52276),(12,'Thomas Camp',478,'Lake Tanya','Antigua and Barbuda',47041),(13,'Davis Way',27173,'Ramosview','Belgium',13643);
/*!40000 ALTER TABLE `Listing_addresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Listings`
--

DROP TABLE IF EXISTS `Listings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Listings` (
  `id` int(11) NOT NULL,
  `host_id` int(11) NOT NULL,
  `title` varchar(200) DEFAULT NULL,
  `property_type` varchar(100) DEFAULT NULL,
  `room_type` varchar(100) DEFAULT NULL,
  `accommodates` int(11) NOT NULL,
  `bedrooms` int(11) NOT NULL,
  `bathrooms` int(11) NOT NULL,
  `price_per_night` decimal(8,4) DEFAULT NULL,
  `address_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `address_id` (`address_id`),
  KEY `host_id` (`host_id`),
  CONSTRAINT `Listings_ibfk_1` FOREIGN KEY (`address_id`) REFERENCES `Listing_addresses` (`id`),
  CONSTRAINT `Listings_ibfk_2` FOREIGN KEY (`host_id`) REFERENCES `Users` (`id`),
  CONSTRAINT `Listings_ibfk_3` FOREIGN KEY (`address_id`) REFERENCES `Listing_addresses` (`id`),
  CONSTRAINT `Listings_ibfk_4` FOREIGN KEY (`host_id`) REFERENCES `Users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Listings`
--

LOCK TABLES `Listings` WRITE;
/*!40000 ALTER TABLE `Listings` DISABLE KEYS */;
INSERT INTO `Listings` VALUES (1,10,'Hilltop Hideaway','villa','entire home/apt',10,5,1,406.0000,11),(2,11,'Park Hyatt','house','private room',5,4,2,429.0000,10),(3,9,'The Peninsula','apartment','private room',3,5,3,214.0000,9),(4,8,'The Mandarin Oriental','villa','private room',1,6,2,382.0000,8),(5,7,'The Plaza Hotel','apartment','shared room',7,3,1,484.0000,7),(6,6,'The Waldorf Astoria','villa','private room',7,3,1,479.0000,6),(7,5,'Hilton Hotels & Resorts','villa','entire home/apt',6,4,2,394.0000,5),(8,1,'The Four Seasons','apartment','private room',2,6,3,466.0000,4),(9,2,'Hotel de Paris','apartment','private room',7,5,1,358.0000,3),(10,3,'Serenity Spa & Resort','villa','private room',7,3,1,191.0000,2),(11,4,'Grand Hotel','house','private room',4,3,2,139.0000,1);
/*!40000 ALTER TABLE `Listings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Messages`
--

DROP TABLE IF EXISTS `Messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Messages` (
  `id` int(11) NOT NULL,
  `sender_id` int(11) NOT NULL,
  `recipient_id` int(11) NOT NULL,
  `content` varchar(200) DEFAULT NULL,
  `date_sent` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `users_id_fk_sender_id` (`sender_id`),
  KEY `users_id_fk_recipient_id` (`recipient_id`),
  CONSTRAINT `users_id_fk` FOREIGN KEY (`sender_id`) REFERENCES `Users` (`id`),
  CONSTRAINT `users_id_fk_recipient_id` FOREIGN KEY (`recipient_id`) REFERENCES `Users` (`id`),
  CONSTRAINT `users_id_fk_sender_id` FOREIGN KEY (`sender_id`) REFERENCES `Users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Messages`
--

LOCK TABLES `Messages` WRITE;
/*!40000 ALTER TABLE `Messages` DISABLE KEYS */;
INSERT INTO `Messages` VALUES (0,12,2,'Thanks for the information. Can you tell me more about the amenities?','2023-02-10'),(1,12,2,'Yes, it\'s available. Would you like to make a reservation?','2018-07-05'),(2,12,2,'Is the room available from May 10','2020-10-12'),(3,12,2,'Sure, what would you like to know?','2022-02-09'),(4,12,2,'Hi,I\'m interested in your listing.Can you tell me more about it?','2021-05-02');
/*!40000 ALTER TABLE `Messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Payments`
--

DROP TABLE IF EXISTS `Payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Payments` (
  `id` int(11) NOT NULL,
  `reservation_id` int(11) NOT NULL,
  `payee_id` int(11) NOT NULL,
  `payer_id` int(11) NOT NULL,
  `payment_method` varchar(100) DEFAULT NULL,
  `payment_date` date DEFAULT NULL,
  `amount` decimal(8,4) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `users_id_fk_payer_id` (`payer_id`),
  KEY `users_id_fk_payee_id` (`payee_id`),
  CONSTRAINT `users_id_fk_payee_id` FOREIGN KEY (`payee_id`) REFERENCES `Users` (`id`),
  CONSTRAINT `users_id_fk_payer_id` FOREIGN KEY (`payer_id`) REFERENCES `Users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Payments`
--

LOCK TABLES `Payments` WRITE;
/*!40000 ALTER TABLE `Payments` DISABLE KEYS */;
INSERT INTO `Payments` VALUES (1,2,7,12,'American Express','2022-05-07',9604.0000),(2,8,4,1,'American Express','2020-12-30',3702.0000),(3,7,4,2,'American Express','2022-08-26',3526.0000),(4,5,3,16,'Mastercard','2021-01-19',6601.0000),(5,3,2,14,'American Express','2022-02-11',5949.0000);
/*!40000 ALTER TABLE `Payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Reservations`
--

DROP TABLE IF EXISTS `Reservations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Reservations` (
  `id` int(11) NOT NULL,
  `guest_id` int(11) NOT NULL,
  `listing_id` int(11) NOT NULL,
  `check_in_date` date DEFAULT NULL,
  `check_out_date` date DEFAULT NULL,
  `total_cost` decimal(8,4) DEFAULT NULL,
  INDEX(id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Reservations`
--

LOCK TABLES `Reservations` WRITE;
/*!40000 ALTER TABLE `Reservations` DISABLE KEYS */;
INSERT INTO `Reservations` VALUES (0,12,3,'2020-04-07','2019-02-23',2520.0000),(1,1,3,'2019-12-22','2020-01-22',5989.0000),(2,2,2,'2020-02-01','2020-01-17',7148.0000),(3,16,1,'2019-06-14','2020-05-04',7484.0000),(4,14,0,'2018-10-31','2021-04-28',5014.0000);
/*!40000 ALTER TABLE `Reservations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Reviews`
--

DROP TABLE IF EXISTS `Reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Reviews` (
  `id` int(11) NOT NULL,
  `listing_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `content` varchar(150) DEFAULT NULL,
  `review_date` date DEFAULT NULL,
  `rating` int(11) NOT NULL,
  `host_response` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `listing_id` (`listing_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `Reviews_ibfk_1` FOREIGN KEY (`listing_id`) REFERENCES `Listings` (`id`),
  CONSTRAINT `Reviews_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`),
  CONSTRAINT `Reviews_ibfk_3` FOREIGN KEY (`listing_id`) REFERENCES `Listings` (`id`),
  CONSTRAINT `Reviews_ibfk_4` FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Reviews`
--

LOCK TABLES `Reviews` WRITE;
/*!40000 ALTER TABLE `Reviews` DISABLE KEYS */;
INSERT INTO `Reviews` VALUES (1,8,21,'Leg cover growth.','2020-06-25',6,'Although song main throw despite get add.'),(2,11,20,'Tend although hear interest Mr loss late.','2021-10-17',3,'Others line civil management cut important.'),(3,10,19,'Radio dinner field suggest learn.','2022-06-08',2,'Step hit mouth.'),(4,4,18,'Glass also hair remember lead no.','2019-02-15',2,'Study son test it from.'),(5,4,17,'Picture plan anything several.','2023-02-14',4,'Room matter single go happen.'),(6,3,16,'Statement with my music artist court describe.','2021-08-31',6,'Former drug natural among off thousand role reveal.'),(7,3,15,'Every behavior American second eat.','2021-08-09',5,'Level friend job ever final.'),(8,2,14,'Treat part thing common including.','2019-12-26',4,'Ten protect answer loss pay.'),(9,1,13,'Can six stage each.','2021-01-01',2,'Leg throw fall get benefit fast.');
/*!40000 ALTER TABLE `Reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User_addresses`
--

DROP TABLE IF EXISTS `User_addresses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User_addresses` (
  `id` int(11) NOT NULL,
  `street_name` varchar(200) DEFAULT NULL,
  `house_number` int(11) NOT NULL,
  `city` varchar(100) DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  `zip_code` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User_addresses`
--

LOCK TABLES `User_addresses` WRITE;
/*!40000 ALTER TABLE `User_addresses` DISABLE KEYS */;
INSERT INTO `User_addresses` VALUES (1,'Elizabeth Union',5284,'South Wesleyside','Togo',6337),(2,'Vazquez Hill',9575,'West Alyssa','Cook Islands',77649),(3,'Catherine Centers',95735,'Reevesville','Monaco',13482),(4,'Martinez Vista',7836,'East Kathleen','Uganda',38858),(5,'Gabriel Land',64,'Evansmouth','Libyan Arab Jamahiriya',38758),(6,'Elijah Rapid',817,'Peterfurt','Congo',13077),(7,'Blankenship Manors',97451,'North Michaelborough','Colombia',99714),(8,'Stephen Turnpike',2359,'Watkinsshire','Sao Tome and Principe',96528),(9,'Baxter Points',5644,'Chelsealand','Jersey',66131),(10,'Smith Haven',545,'Taylorside','Moldova',80197),(11,'Nathan Islands',110,'South Savannahfurt','Greenland',97373),(12,'David Manors',161,'North Davidton','Tunisia',40544),(13,'Zimmerman Mews',7347,'Alexandrafurt','Pitcairn Islands',18608),(14,'Esparza Crescent',682,'Port Phyllismouth','United States Minor Outlying Islands',35866),(15,'Harris Summit',3858,'Leland','Guinea',54689),(16,'Brown Landing',760,'Jamieland','Sweden',36784),(17,'Mueller Glens',436,'Port Roger','Somalia',7400),(18,'Jackson Parkway',33629,'New Stevenburgh','French Southern Territories',28486),(19,'William Trail',52863,'Carrollfort','Eritrea',60347),(20,'Danielle Rest',1143,'Christinetown','Guinea-Bissau',44465);
/*!40000 ALTER TABLE `User_addresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Users` (
  `id` int(11) NOT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone_number` varchar(100) DEFAULT NULL,
  `DoB` date DEFAULT NULL,
  `gender` enum('Male','Female') DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  `user_type` enum('host','guest') DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (1,'Rebecca','Baker','mitchellcastillo@example.org','489-926-1438','1933-03-11','Female','Ecuador','host'),(2,'Ashley','Perry','pwest@example.com','937.233.9170x026','1993-08-19','Male','Burundi','host'),(3,'Joseph','Hopkins','potterjuan@example.org','(142)716-7217x39938','1993-09-14','Male','Jordan','host'),(4,'Timothy','Reeves','barajasdaniel@example.com','498.759.4267','1969-06-13','Male','Mexico','host'),(5,'Jennifer','Hampton','npatel@example.org','273.254.6632x44407','1931-04-09','Female','Paraguay','host'),(6,'Jonathan','Trevino','burchjennifer@example.com','214.791.0968','1988-08-19','Male','Saint Kitts and Nevis','host'),(7,'Tristan','Ward','hrussell@example.org','+1-534-024-2250x8597','1938-03-13','Female','Lebanon','host'),(8,'Scott','Watkins','lindsey02@example.org','001-072-368-9527x4807','1965-11-18','Male','Nepal','host'),(9,'Patricia','Walker','davisstephanie@example.org','001-362-263-1604x078','1944-08-30','Male','Sierra Leone','host'),(10,'Joseph','Salazar','cgarrett@example.com','4396060150','1948-08-26','Female','Thailand','host'),(11,'Joseph','Adams','donna47@example.net','1773207666','1988-04-16','Male','India','host'),(12,'Keith','Bennett','rileymartinez@example.com','(040)447-2494','1965-08-10','Female','Belize','guest'),(13,'David','Jones','sandersbenjamin@example.org','8386766180','1968-10-17','Male','Guam','guest'),(14,'Charles','Williams','weaverkelly@example.org','001-555-263-0013x87749','1980-06-25','Male','Marshall Islands','guest'),(15,'Laura','Richmond','charles21@example.net','711.914.7683x981','1992-03-15','Male','North Macedonia','guest'),(16,'Christopher','Kennedy','myerssara@example.com','233-577-9951x811','2003-01-07','Male','Cameroon','guest'),(17,'Bobby','Clarke','debra13@example.com','070.383.5523x5320','1958-03-04','Female','Marshall Islands','guest'),(18,'Lacey','Smith','morgandavid@example.org','001-823-904-0577x19564','1945-01-18','Female','Moldova','guest'),(19,'Kathryn','Edwards','denniswaters@example.com','333-406-1956x93135','2002-09-04','Female','Saint Vincent and the Grenadines','guest'),(20,'Tricia','Clayton','hensonkenneth@example.net','001-504-259-5788','1966-04-15','Male','Jersey','guest'),(21,'Rick','Baker','lucas37@example.com','063-883-9344x093','1946-07-09','Female','Colombia','guest');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-01 15:29:08
