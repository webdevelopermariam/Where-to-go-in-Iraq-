-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: localhost    Database: info
-- ------------------------------------------------------
-- Server version	8.0.44

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
--

DROP TABLE IF EXISTS `archaeological site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `archaeological site` (
  `id` int NOT NULL AUTO_INCREMENT,
  `location_id` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name_english` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `city_region` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `type` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `heritage_category` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `rating` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `best_for` text COLLATE utf8mb4_unicode_ci,
  `google_maps_link` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_transferred` tinyint(1) DEFAULT '0',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_location_id` (`location_id`(255))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `archaeological site`
--

LOCK TABLES `archaeological site` WRITE;
/*!40000 ALTER TABLE `archaeological site` DISABLE KEYS */;
/*!40000 ALTER TABLE `archaeological site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cafes`
--

DROP TABLE IF EXISTS `cafes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cafes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `city` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `type` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `price` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `category` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `vibe_note` text COLLATE utf8mb4_unicode_ci,
  `location_landmark` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `google_map` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_transferred` tinyint(1) DEFAULT '0',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_cafe_name_city` (`name`,`city`)
) ENGINE=InnoDB AUTO_INCREMENT=190 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cafes`
--

LOCK TABLES `cafes` WRITE;
/*!40000 ALTER TABLE `cafes` DISABLE KEYS */;
INSERT INTO `cafes` VALUES (1,'Shabandar Café','Baghdad','Traditional','$','Heritage/Intellectual','The \"Heart of Baghdad.\" 100+ years old. No games allowed, only talk. Best for history lovers.','Al-Mutanabbi St','Open Map',0,'2025-12-06 12:37:30','2025-12-06 12:37:30'),(2,'Ridha Alwan Coffee','Baghdad','Roastery/Cafe','$$','Cultural/Social','Famous meeting spot. Known for fresh roasted beans and mixing traditional vibes with modern crowds.','Karrada / Al-Wahda','Open Map',0,'2025-12-06 12:37:30','2025-12-06 12:37:30'),(3,'Al-Zahawi Café','Baghdad','Traditional','$','Heritage','Historic spot named after the poet Al-Zahawi. Classic \"old Baghdad\" atmosphere near the old square.','Al-Midan Square','Open Map',0,'2025-12-06 12:37:30','2025-12-06 12:37:30'),(4,'Umm Kulthum Café','Baghdad','Traditional','$','Heritage/Music','Dedicated to the legendary singer. Walls covered in her photos; plays her music constantly.','Rasheed Street','Open Map',0,'2025-12-06 12:37:30','2025-12-06 12:37:30'),(5,'Cafe 11','Baghdad','Modern','$$','Work/Study','Quiet, modern design, great for freelancers and students. Good WiFi.','Al-Mansour','Open Map',0,'2025-12-06 12:37:30','2025-12-06 12:37:30'),(6,'650 Café','Baghdad','Modern','$$$','Trendy/Luxury','High-end, \"Instagrammable\" design. Great for dates or evening hangouts. Serves food too.','Al-Yarmouk','Open Map',0,'2025-12-06 12:37:30','2025-12-06 12:37:30'),(7,'Bunn Coffee','Baghdad','Modern/Chain','$$','Quick/Quality','Reliable local chain for good espresso and takeaway coffee.','Multiple Branches','Open Map',0,'2025-12-06 12:37:30','2025-12-06 12:37:30'),(8,'Machko Chaikhana','Erbil','Traditional','$','Heritage/Tourist','Most famous in Kurdistan. Located under the Citadel. A must-visit for tea and photos.','Erbil Citadel','Open Map',0,'2025-12-06 12:37:30','2025-12-06 12:37:30'),(9,'Espressolab Erbil','Erbil','Modern','$$','Work/Social','Massive space, very popular with students and expats. Great terrace views of the Citadel.','Grand Majidi / Citadel','Open Map',0,'2025-12-06 12:37:30','2025-12-06 12:37:30'),(10,'Barista Lab','Erbil','Modern','$$','Specialty Coffee','Serious about coffee quality. Best for \"coffee snobs\" who want a perfect V60 or cortado.','Dream City','Open Map',0,'2025-12-06 12:37:30','2025-12-06 12:37:30'),(11,'Pappa Roti','Erbil','Modern','$$$','Family/Dessert','Famous for coffee buns. Good for families and sweet treats.','Empire World','Open Map',0,'2025-12-06 12:37:30','2025-12-06 12:37:30'),(12,'Chaikhana Shaab','Sulaymaniyah','Traditional','$','Heritage/Political','\"The People\'s Teahouse.\" Historic hub for poets, politicians, and artists. Very authentic.','Suli Bazaar','Open Map',0,'2025-12-06 12:37:30','2025-12-06 12:37:30'),(13,'Chalak\'s Place','Sulaymaniyah','Modern','$$','Artsy/Cozy','Located in a renovated heritage house. Jazz music, books, and a very \"intellectual\" vibe.','Salim Street','Open Map',0,'2025-12-06 12:37:30','2025-12-06 12:37:30'),(14,'Ahwazna Coffee','Basra','Modern','$$','Social','Popular evening spot. Good mix of traditional hospitality and modern cafe style.','Al-Jaza\'ir St','Open Map',0,'2025-12-06 12:37:30','2025-12-06 12:37:30'),(15,'Corniche Teahouses','Basra','Traditional','$','Scenic/Outdoor','Best Sunset Spot. Simple plastic chairs by the Shatt al-Arab river. Order tea and enjoy the view.','Shatt al-Arab','Open Map',0,'2025-12-06 12:37:30','2025-12-06 12:37:30'),(16,'Qantar Café','Mosul','Traditional','$','Heritage','Represents the reviving spirit of Mosul. Located in the Old City, traditional architecture.','Old City Mosul','Open Map',0,'2025-12-06 12:37:30','2025-12-06 12:37:30'),(17,'Book Forum Café','Mosul','Modern','$','Cultural/Books','A hub for Mosul\'s youth and intellectuals. Hosting book clubs and debates.','Near University','Open Map',0,'2025-12-06 12:37:30','2025-12-06 12:37:30'),(18,'Al-Faisaliya Cafe','Najaf','Traditional','$','Heritage','Museum-like. Full of antiques and old photos. A deep dive into Najaf\'s history.','Al-Mishkhab','Open Map',0,'2025-12-06 12:37:30','2025-12-06 12:37:30'),(19,'Cafe 21','Najaf','Modern','$$','Youth/Social','Modern gathering spot for young people in Najaf. Good burgers and frappes.','City Center','Open Map',0,'2025-12-06 12:37:30','2025-12-06 12:37:30'),(20,'Nova Café','Karbala','Modern','$$','Quiet/Relaxed','A rare quiet spot near the bustle of the shrines. Good for a break.','Al-Hussein Quarter','Open Map',0,'2025-12-06 12:37:30','2025-12-06 12:37:30'),(21,'One Million Cafe','Karbala','Modern','$$$','Luxury/Social','Upscale design, very busy in evenings. Popular with youth and visitors.','Karbala Center','Open Map',0,'2025-12-06 12:37:30','2025-12-06 12:37:30');
/*!40000 ALTER TABLE `cafes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `holy-places`
--

DROP TABLE IF EXISTS `holy-places`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `holy-places` (
  `id` int NOT NULL AUTO_INCREMENT,
  `location_id` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name_english` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `city` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `type` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `category` varchar(150) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `rating` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `best_for` text COLLATE utf8mb4_unicode_ci,
  `google_maps_link` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_transferred` tinyint(1) DEFAULT '0',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_location_id` (`location_id`(255))
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `holy-places`
--

LOCK TABLES `holy-places` WRITE;
/*!40000 ALTER TABLE `holy-places` DISABLE KEYS */;
INSERT INTO `holy-places` VALUES (25,'Muslim Shrines (Najaf/Karbala/Kadhimiya): Strictly conservative. Women must wear an Abaya (often provided at the door). Men should avoid shorts.','','','','','','','',0,'2025-12-06 12:58:51','2025-12-06 12:58:51'),(26,'Christian Monasteries: Modest dress (shoulders and knees covered) is respectful and required at active sites like Mar Mattai.','','','','','','','',0,'2025-12-06 12:58:52','2025-12-06 12:58:52'),(27,'Best Time to Visit:','','','','','','','',0,'2025-12-06 12:58:52','2025-12-06 12:58:52'),(28,'Shrines: Sunset or night is often the most magical time due to the lighting.','','','','','','','',0,'2025-12-06 12:58:53','2025-12-06 12:58:53'),(29,'Monasteries: Early morning for the best mountain views (especially Mar Mattai).','','','','','','','',0,'2025-12-06 12:58:54','2025-12-06 12:58:54');
/*!40000 ALTER TABLE `holy-places` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hotels`
--

DROP TABLE IF EXISTS `hotels`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hotels` (
  `id` int NOT NULL AUTO_INCREMENT,
  `location_id` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name_english` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `city` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `category` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `price_range` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `rating` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `best_for` text COLLATE utf8mb4_unicode_ci,
  `google_maps_link` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_transferred` tinyint(1) DEFAULT '0',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_location_id` (`location_id`(255))
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hotels`
--

LOCK TABLES `hotels` WRITE;
/*!40000 ALTER TABLE `hotels` DISABLE KEYS */;
INSERT INTO `hotels` VALUES (1,'HTL-BG-01','Babylon Rotana','Baghdad','Luxury','$$$','⭐ 4.4','Luxury/Views: Iconic pyramid shape on the Tigris.','Open Map',0,'2025-12-06 12:37:01','2025-12-06 12:37:01'),(2,'HTL-BG-02','Royal Tulip Al Rasheed','Baghdad','Luxury','$$$','⭐ 4.8','Security/VIP: Located in the Green Zone.','Open Map',0,'2025-12-06 12:37:02','2025-12-06 12:37:02'),(3,'HTL-BG-03','Coral Baghdad Hotel','Baghdad','Business','$$','⭐ 4.2','Business: Modern, secure location in Jadriyah.','Open Map',0,'2025-12-06 12:37:03','2025-12-06 12:37:03'),(4,'HTL-BG-04','Noor Land Hotel','Baghdad','Mid-Range','$$','⭐ 4.0','Value: Good balance of price and comfort in Karrada.','Open Map',0,'2025-12-06 12:37:04','2025-12-06 12:37:04'),(5,'HTL-BG-05','Baghdad Hotel','Baghdad','Heritage','$$','⭐ 3.9','Nostalgia: One of the oldest famous hotels.','Open Map',0,'2025-12-06 12:37:05','2025-12-06 12:37:05'),(6,'HTL-BG-06','Al-Mansour Hotel','Baghdad','Luxury/Old','$$','⭐ 3.7','River Views: Excellent location on the river bank.','Open Map',0,'2025-12-06 12:37:05','2025-12-06 12:37:05'),(7,'HTL-BG-07','Cristal Grand Ishtar','Baghdad','Luxury','$$','⭐ 3.8','Landmark: Tallest hotel in Baghdad, central location.','Open Map',0,'2025-12-06 12:37:06','2025-12-06 12:37:06'),(8,'HTL-BG-08','Rimal Hotel','Baghdad','Boutique','$$','⭐ 4.1','Couples/Quiet: Located in Karrada, cozy atmosphere.','Open Map',0,'2025-12-06 12:37:07','2025-12-06 12:37:07'),(9,'HTL-BG-09','Shanasheel Palace','Baghdad','Mid-Range','$$','⭐ 4.3','Culture: Traditional Iraqi design elements.','Open Map',0,'2025-12-06 12:37:08','2025-12-06 12:37:08'),(10,'HTL-BG-10','Al-Burhan Hotel','Baghdad','Transit','$$','⭐ 4.0','Airport: Best option for layovers near BIAP.','Open Map',0,'2025-12-06 12:37:09','2025-12-06 12:37:09'),(11,'HTL-ER-01','Divan Erbil Hotel','Erbil','Luxury','$$$','⭐ 4.6','Top Tier: Most elegant high-service hotel in Erbil.','Open Map',0,'2025-12-06 12:37:10','2025-12-06 12:37:10'),(12,'HTL-ER-02','Erbil Rotana','Erbil','Luxury','$$$','⭐ 4.5','Conferences: Large capacity, near park.','Open Map',0,'2025-12-06 12:37:11','2025-12-06 12:37:11'),(13,'HTL-ER-03','Cristal Erbil Hotel','Erbil','Mid-Range','$$','⭐ 4.0','Comfort: Reliable standard, good gym/pool.','Open Map',0,'2025-12-06 12:37:12','2025-12-06 12:37:12'),(14,'HTL-ER-04','Erbil Quartz Hotel','Erbil','Budget','$','⭐ 4.2','Budget Luxury: High quality for low price.','Open Map',0,'2025-12-06 12:37:13','2025-12-06 12:37:13'),(15,'HTL-ER-05','Erbil International','Erbil','Business','$$','⭐ 4.1','Business: Central, large meeting halls.','Open Map',0,'2025-12-06 12:37:14','2025-12-06 12:37:14'),(16,'HTL-ER-06','Canyon Hotel Erbil','Erbil','Boutique','$$','⭐ 4.3','Style: Modern design, popular restaurant.','Open Map',0,'2025-12-06 12:37:14','2025-12-06 12:37:14'),(17,'HTL-ER-07','Blue Mercury Hotel','Erbil','Mid-Range','$$','⭐ 4.0','Location: Near Ankawa (Christian district).','Open Map',0,'2025-12-06 12:37:15','2025-12-06 12:37:15'),(18,'HTL-ER-08','Ali Hotel','Erbil','Budget','$','⭐ 2.8','Backpackers: Very cheap, near Citadel (basic).','Open Map',0,'2025-12-06 12:37:16','2025-12-06 12:37:16'),(19,'HTL-SU-01','Grand Millennium','Sulaymaniyah','Luxury','$$$','⭐ 4.7','Views: Iconic tower, best city views.','Open Map',0,'2025-12-06 12:37:17','2025-12-06 12:37:17'),(20,'HTL-SU-02','Titanic Hotel & SPA','Sulaymaniyah','Mid-Range','$$','⭐ 4.3','Relaxation: Known for spa services.','Open Map',0,'2025-12-06 12:37:18','2025-12-06 12:37:18'),(21,'HTL-SU-03','Copthorne Hotel','Sulaymaniyah','Business','$$','⭐ 4.2','Business: Reliable international standard.','Open Map',0,'2025-12-06 12:37:19','2025-12-06 12:37:19'),(22,'HTL-SU-04','Ramada by Wyndham','Sulaymaniyah','Luxury','$$$','⭐ 4.4','Comfort: Modern amenities, Salim Street.','Open Map',0,'2025-12-06 12:37:19','2025-12-06 12:37:19'),(23,'HTL-SU-05','Dolphin Hotel','Sulaymaniyah','Budget','$','⭐ 4.1','Backpackers: Famous hostel/budget spot.','Open Map',0,'2025-12-06 12:37:20','2025-12-06 12:37:20'),(24,'HTL-SU-06','Khan Saray','Sulaymaniyah','Mid-Range','$$','⭐ 4.2','Location: Very central near the bazaar.','Open Map',0,'2025-12-06 12:37:21','2025-12-06 12:37:21'),(25,'HTL-BS-01','Grand Millennium','Basra','Luxury','$$$','⭐ 4.5','Luxury: Prestigious address in Basra.','Open Map',0,'2025-12-06 12:37:22','2025-12-06 12:37:22'),(26,'HTL-BS-02','Basra International','Basra','Business','$$','⭐ 4.0','Access: Close to Shatt al-Arab corniche.','Open Map',0,'2025-12-06 12:37:23','2025-12-06 12:37:23'),(27,'HTL-NJ-01','Najaf Do Hotel','Najaf','Religious','$$','⭐ 4.9','Pilgrims: Closest to Imam Ali Shrine.','Open Map',0,'2025-12-06 12:37:24','2025-12-06 12:37:24'),(28,'HTL-NJ-02','Qasr AlDur Hotel','Najaf','Mid-Range','$$','⭐ 4.2','Families: Spacious rooms for groups.','Open Map',0,'2025-12-06 12:37:25','2025-12-06 12:37:25'),(29,'HTL-KR-01','The Baron Hotel','Karbala','Luxury','$$$','⭐ 4.8','VIP Pilgrim: Finest hotel in Karbala.','Open Map',0,'2025-12-06 12:37:25','2025-12-06 12:37:25'),(30,'HTL-KR-02','Jannat Al-Hussein','Karbala','Mid-Range','$$','⭐ 4.5','Comfort: Highly rated, close to shrines.','Open Map',0,'2025-12-06 12:37:26','2025-12-06 12:37:26'),(31,'HTL-DU-01','Kristal Hotel','Duhok','Mid-Range','$$','⭐ 4.0','Mountain Trips: Good base for exploring North.','Open Map',0,'2025-12-06 12:37:26','2025-12-06 12:37:26'),(32,'HTL-KI-01','Kirkuk Plaza Hotel','Kirkuk','Business','$$','⭐ 4.0','Business: Best standard option in Kirkuk.','Open Map',0,'2025-12-06 12:37:27','2025-12-06 12:37:27'),(33,'HTL-RA-01','Rose Plaza Hotel','Ramadi','Business','$$','⭐ 3.9','Local Travel: Best option in Anbar province.','Open Map',0,'2025-12-06 12:37:27','2025-12-06 12:37:27'),(34,'HTL-AM-01','Kurmick Maysan','Amarah','Luxury','$$','⭐ 4.1','Luxury: Best hotel in Maysan province.','Open Map',0,'2025-12-06 12:37:27','2025-12-06 12:37:27'),(35,'HTL-NA-01','Sumerian Hotel','Nasiriyah','Local','$','⭐ 3.5','Archaeology: Base for visiting Ur/Marshes.','Open Map',0,'2025-12-06 12:37:28','2025-12-06 12:37:28'),(36,'HTL-BG-11','Al-Rabie Hotel','Baghdad','Apartments','$$','⭐ 4.2','Long Stay: Great apartment-style rooms.','Open Map',0,'2025-12-06 12:37:28','2025-12-06 12:37:28');
/*!40000 ALTER TABLE `hotels` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-07  1:31:42
