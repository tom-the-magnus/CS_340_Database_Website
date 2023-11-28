-- phpMyAdmin SQL Dump
-- version 5.2.1-1.el7.remi
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 27, 2023 at 11:26 AM
-- Server version: 10.6.15-MariaDB-log
-- PHP Version: 8.2.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cs340_magnust`
--

-- --------------------------------------------------------

--
-- Stand-in structure for view `Calendar_Dimensions`
-- (See below for the actual view)
--
CREATE TABLE `Calendar_Dimensions` (
`FullDate` varchar(23)
,`DayOfYr` date
,`Month` int(2)
,`Day` int(2)
,`Quarter` int(1)
,`Years` int(4)
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `Customer_Dimensions`
-- (See below for the actual view)
--
CREATE TABLE `Customer_Dimensions` (
`customerId` int(11)
,`CustomerName` varchar(255)
,`CustomerCity` varchar(255)
,`CustomerState` varchar(255)
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `Employee_Dimensions`
-- (See below for the actual view)
--
CREATE TABLE `Employee_Dimensions` (
`EmployeeID` int(11)
,`EmployeeFirstName` varchar(255)
,`EmployeeLastName` varchar(255)
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `Sales_Facts`
-- (See below for the actual view)
--
CREATE TABLE `Sales_Facts` (
`FullDate` varchar(23)
,`CustomerID` int(11)
,`EmployeeID` int(11)
,`ProductID` varchar(255)
,`UnitsSold` int(11)
,`DollarSold` decimal(19,4)
);

-- --------------------------------------------------------

--
-- Structure for view `Calendar_Dimensions` exported as a table
--
DROP TABLE IF EXISTS `Calendar_Dimensions`;
CREATE TABLE`Calendar_Dimensions`(
    `FullDate` varchar(23) COLLATE utf8mb4_general_ci DEFAULT NULL,
    `DayOfYr` date DEFAULT NULL,
    `Month` int(2) DEFAULT NULL,
    `Day` int(2) DEFAULT NULL,
    `Quarter` int(1) DEFAULT NULL,
    `Years` int(4) DEFAULT NULL
);

-- --------------------------------------------------------

--
-- Structure for view `Customer_Dimensions` exported as a table
--
DROP TABLE IF EXISTS `Customer_Dimensions`;
CREATE TABLE`Customer_Dimensions`(
    `customerId` int(11) NOT NULL,
    `CustomerName` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
    `CustomerCity` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
    `CustomerState` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL
);

-- --------------------------------------------------------

--
-- Structure for view `Employee_Dimensions` exported as a table
--
DROP TABLE IF EXISTS `Employee_Dimensions`;
CREATE TABLE`Employee_Dimensions`(
    `EmployeeID` int(11) NOT NULL,
    `EmployeeFirstName` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
    `EmployeeLastName` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL
);

-- --------------------------------------------------------

--
-- Structure for view `Sales_Facts` exported as a table
--
DROP TABLE IF EXISTS `Sales_Facts`;
CREATE TABLE`Sales_Facts`(
    `FullDate` varchar(23) COLLATE utf8mb4_general_ci DEFAULT NULL,
    `CustomerID` int(11) DEFAULT NULL,
    `EmployeeID` int(11) DEFAULT NULL,
    `ProductID` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
    `UnitsSold` int(11) DEFAULT NULL,
    `DollarSold` decimal(19,4) DEFAULT NULL
);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
