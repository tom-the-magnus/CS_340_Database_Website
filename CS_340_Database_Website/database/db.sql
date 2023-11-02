-- phpMyAdmin SQL Dump
-- version 5.2.1-1.el7.remi
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 27, 2023 at 02:16 PM
-- Server version: 10.6.15-MariaDB-log
-- PHP Version: 8.2.11

SET FOREIGN_KEY_CHECKS=0;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cs340_javiyaa`
--

-- --------------------------------------------------------

--
-- Table structure for table `Customers`
--

CREATE TABLE `Customers` (
  `customer_id` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Dumping data for table `Customers`
--

INSERT INTO `Customers` (`customer_id`, `first_name`, `last_name`, `email`) VALUES
(1, 'Chris', 'Cornell', 'spoonman@gmail.com'),
(2, 'Kurt', 'Cobain', 'teenspirit@gmail.com'),
(3, 'Scott', 'Weiland', 'bigempty@gmail.com');


-- --------------------------------------------------------

--
-- Table structure for table `Genres`
--

CREATE TABLE `Genres` (
  `genre_id` int(11) NOT NULL,
  `genre_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Dumping data for table `Genres`
--

INSERT INTO `Genres` (`genre_id`, `genre_name`) VALUES
(1, 'Action'),
(2, 'Sci-Fi/Fantasy'),
(3, 'Thriller');

-- --------------------------------------------------------

--
-- Table structure for table `Movies`
--

CREATE TABLE `Movies` (
  `movie_id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Dumping data for table `Movies`
--

INSERT INTO `Movies` (`movie_id`, `title`) VALUES
(1, 'Gladiator'),
(2, 'Jurassic Park'),
(3, 'Silence of the Lambs'),
(4, 'The Killing of a Sacred Deer'),
(5, 'Aliens');

-- --------------------------------------------------------

--
-- Table structure for table `Movie_Genre_Details`
--

CREATE TABLE `Movie_Genre_Details` (
  `movie_genre_id` int(11) NOT NULL,
  `movie_id` int(11) DEFAULT NULL,
  `genre_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Dumping data for table `Movie_Genre_Details`
--

INSERT INTO `Movie_Genre_Details` (`movie_genre_id`, `movie_id`, `genre_id`) VALUES
(1, 1, 2),
(2, 2, 2),
(3, 3, 3),
(4, 4, 3),
(5, 5, 1),
(6, 5, 2);

-- --------------------------------------------------------

--
-- Table structure for table `Rentals`
--

CREATE TABLE `Rentals` (
  `rental_id` int(11) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `movie_id` int(11) NOT NULL,
  `due_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci;

--
-- Dumping data for table `Rentals`
--

INSERT INTO `Rentals` (`rental_id`, `customer_id`, `movie_id`, `due_date`) VALUES
(1, 1, 2, '2023-11-07'),
(2, 1, 1, '2023-11-27'),
(3, 2, 1, '2023-12-08'),
(4, 3, 3, '2023-12-24'),
(5, 3, 5, '2024-01-14');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Customers`
--
ALTER TABLE `Customers`
  ADD PRIMARY KEY (`customer_id`),
  ADD UNIQUE KEY `customer_id` (`customer_id`);

--
-- Indexes for table `Genres`
--
ALTER TABLE `Genres`
  ADD PRIMARY KEY (`genre_id`),
  ADD UNIQUE KEY `genre_id` (`genre_id`);

--
-- Indexes for table `Movies`
--
ALTER TABLE `Movies`
  ADD PRIMARY KEY (`movie_id`),
  ADD UNIQUE KEY `movie_id` (`movie_id`);

--
-- Indexes for table `Movie_Genre_Details`
--
ALTER TABLE `Movie_Genre_Details`
  ADD PRIMARY KEY (`movie_genre_id`),
  ADD UNIQUE KEY `movie_genre_id` (`movie_genre_id`),
  ADD KEY `movie_id` (`movie_id`),
  ADD KEY `genre_id` (`genre_id`);

--
-- Indexes for table `Rentals`
--
ALTER TABLE `Rentals`
  ADD PRIMARY KEY (`rental_id`),
  ADD UNIQUE KEY `rental_id` (`rental_id`),
  ADD KEY `customer_id` (`customer_id`),
  ADD KEY `movie_id` (`movie_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Customers`
--
ALTER TABLE `Customers`
  MODIFY `customer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `Genres`
--
ALTER TABLE `Genres`
  MODIFY `genre_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `Movies`
--
ALTER TABLE `Movies`
  MODIFY `movie_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `Movie_Genre_Details`
--
ALTER TABLE `Movie_Genre_Details`
  MODIFY `movie_genre_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `Rentals`
--
ALTER TABLE `Rentals`
  MODIFY `rental_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Movie_Genre_Details`
--
ALTER TABLE `Movie_Genre_Details`
  ADD CONSTRAINT `Movie_Genre_Details_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `Movies` (`movie_id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `Movie_Genre_Details_ibfk_2` FOREIGN KEY (`genre_id`) REFERENCES `Genres` (`genre_id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Constraints for table `Rentals`
--
ALTER TABLE `Rentals`
  ADD CONSTRAINT `Rentals_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `Customers` (`customer_id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `Rentals_ibfk_2` FOREIGN KEY (`movie_id`) REFERENCES `Movies` (`movie_id`) ON DELETE CASCADE ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

SET FOREIGN_KEY_CHECKS=1