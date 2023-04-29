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
-- Table structure for table `Addresses`
--

DROP TABLE IF EXISTS `Addresses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Addresses` (
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
-- Dumping data for table `Addresses`
--

LOCK TABLES `Addresses` WRITE;
/*!40000 ALTER TABLE `Addresses` DISABLE KEYS */;
INSERT INTO `Addresses` VALUES (0,'Davis Harbors',46692,'Juliaton','North Macedonia',34657),(1,'Powell Spur',72806,'Derekport','Bosnia and Herzegovina',93738),(2,'Davis Trail',40441,'North Kristen','Bolivia',38677),(3,'Brian Green',115,'Jenningsfurt','Japan',36994),(4,'Vang Club',594,'South Samuelside','Tajikistan',97500),(5,'Barr Canyon',691,'New Lisa','Dominican Republic',55917),(6,'Ryan Plaza',54776,'New Brandonshire','Venezuela',10516),(7,'Steve Curve',21424,'Oliverfurt','Syrian Arab Republic',14136),(8,'Hill Stream',490,'New Jason','Algeria',61438),(9,'Sherri Motorway',35072,'South Karen','Argentina',62989);
/*!40000 ALTER TABLE `Addresses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Amenities`
--

DROP TABLE IF EXISTS `Amenities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Amenities` (
  `id` int(11) NOT NULL,
  `listing_id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `listing_id` (`listing_id`),
  CONSTRAINT `Amenities_ibfk_1` FOREIGN KEY (`listing_id`) REFERENCES `Listings` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Amenities`
--

LOCK TABLES `Amenities` WRITE;
/*!40000 ALTER TABLE `Amenities` DISABLE KEYS */;
INSERT INTO `Amenities` VALUES (0,4,'Air conditioning','Central air conditioning system in all rooms'),(1,3,'Free parking','Designated parking spot on property for guest use'),(2,2,'Pool','Private outdoor pool for guest use only'),(3,1,'Kitchen','Fully equipped kitchen'),(4,0,'Wi-Fi','High-speed internet access throughout the property');
/*!40000 ALTER TABLE `Amenities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Hosts`
--

DROP TABLE IF EXISTS `Hosts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Hosts` (
  `id` int(11) NOT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone_number` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Hosts`
--

LOCK TABLES `Hosts` WRITE;
/*!40000 ALTER TABLE `Hosts` DISABLE KEYS */;
INSERT INTO `Hosts` VALUES (0,'Jose','Williams','olivialeon@example.net','156-692-2345x760'),(1,'Kyle','Hernandez','ywilcox@example.org','8986876891'),(2,'Connie','Reid','jamiebell@example.org','979.102.9238'),(3,'Sean','Rivers','harrellsara@example.net','001-282-445-9512x5105'),(4,'Rachel','Taylor','danieloliver@example.com','048-482-9407');
/*!40000 ALTER TABLE `Hosts` ENABLE KEYS */;
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
  `title` varchar(100) DEFAULT NULL,
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
  CONSTRAINT `Listings_ibfk_1` FOREIGN KEY (`address_id`) REFERENCES `Addresses` (`id`),
  CONSTRAINT `Listings_ibfk_2` FOREIGN KEY (`host_id`) REFERENCES `Hosts` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Listings`
--

LOCK TABLES `Listings` WRITE;
/*!40000 ALTER TABLE `Listings` DISABLE KEYS */;
INSERT INTO `Listings` VALUES (0,1,'The Waldorf Astoria','villa','private room',3,1,3,258.0000,5),(1,2,'Hilton Hotels & Resorts','house','private room',2,5,2,329.0000,4),(2,2,'The Four Seasons','apartment','entire home/apt',10,6,3,398.0000,3),(3,0,'The Ritz-CarltonHotel de Paris','apartment','private room',5,2,3,248.0000,2),(4,4,'Grand Hotel','apartment','private room',4,1,2,219.0000,1);
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
  UNIQUE KEY `ux_col1_col2` (`sender_id`,`recipient_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Messages`
--

LOCK TABLES `Messages` WRITE;
/*!40000 ALTER TABLE `Messages` DISABLE KEYS */;
INSERT INTO `Messages` VALUES (1,2,2,'hello','2020-01-01');
/*!40000 ALTER TABLE `Messages` ENABLE KEYS */;
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
  `text` varchar(150) DEFAULT NULL,
  `review_date` date DEFAULT NULL,
  `rating` int(11) NOT NULL,
  `host_response` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `listing_id` (`listing_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `Reviews_ibfk_1` FOREIGN KEY (`listing_id`) REFERENCES `Listings` (`id`),
  CONSTRAINT `Reviews_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Reviews`
--

LOCK TABLES `Reviews` WRITE;
/*!40000 ALTER TABLE `Reviews` DISABLE KEYS */;
INSERT INTO `Reviews` VALUES (0,3,3,'Assume force rest other.','2020-07-30',1,'Size inside doctor lose look least appear.'),(1,3,3,'Population property skin affect read ever heart concern.','2023-02-04',6,'Speech also century adult director hundred fly ever.'),(2,2,3,'Doctor would learn walk report rest herself.','2021-07-05',2,'Each member personal that big.'),(3,1,2,'Specific fire including drop I forward go.','2019-06-13',2,'Friend current challenge continue meet oil score.'),(4,0,1,'Middle man field newspaper.','2019-07-31',3,'Wear kitchen forget relate.');
/*!40000 ALTER TABLE `Reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Users` (
  `id` int(11) NOT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone_number` varchar(50) DEFAULT NULL,
  `DoB` date DEFAULT NULL,
  `gender` enum('Male','Female') DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `user_type` enum('host','guest') DEFAULT NULL,
  `num_of_reviews` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (0,'Katherine','Johnston','vwilliams@example.com','001-607-804-8336x610','1975-12-15','Male','Cook Islands','guest',6),(1,'Gary','Tran','matthewpayne@example.com','631-934-8026x857','1987-06-10','Male','Togo','guest',1),(2,'Christopher','Graham','randallmelissa@example.org','(206)416-8155x070','1993-05-03','Male','Saint Barthelemy','host',6),(3,'Mary','Mendoza','davidhamilton@example.com','6087690576','1943-01-29','Male','Turks and Caicos Islands','guest',3),(4,'Jason','Copeland','ortizapril@example.net','+1-982-050-7527x0641','1969-06-04','Female','Guinea-Bissau','guest',1);
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

-- Dump completed on 2023-04-29  9:56:46
