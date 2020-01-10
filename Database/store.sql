-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 10, 2020 at 10:37 PM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.3.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `store`
--

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `id` int(11) NOT NULL,
  `productName` varchar(255) NOT NULL,
  `quantity` int(11) NOT NULL,
  `buy` int(11) NOT NULL,
  `sell` int(11) NOT NULL,
  `addedBy` varchar(255) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`id`, `productName`, `quantity`, `buy`, `sell`, `addedBy`, `date`) VALUES
(1, 'Potato', 33, 25, 40, 'kawserahmed', '2020-01-06'),
(2, 'Egg', 32, 5, 8, 'KawserAhmed', '2020-01-09'),
(3, 'Onion', 31, 30, 180, 'ka', '2020-01-11');

-- --------------------------------------------------------

--
-- Table structure for table `transaction`
--

CREATE TABLE `transaction` (
  `id` int(11) NOT NULL,
  `txnId` int(11) NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `quantity` int(11) NOT NULL,
  `price` varchar(255) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `transaction`
--

INSERT INTO `transaction` (`id`, `txnId`, `product_name`, `quantity`, `price`, `date`) VALUES
(41, 9365, 'Potato', 2, '80.0', '2020-01-11'),
(42, 7813, 'Potato', 2, '80.0', '2020-01-11'),
(43, 7813, 'Egg', 4, '32.0', '2020-01-11'),
(44, 9090, 'Potato', 3, '120.0', '2020-01-11'),
(45, 9090, 'Egg', 8, '64.0', '2020-01-11'),
(46, 8830, 'Potato', 3, '120.0', '2020-01-11'),
(47, 8830, 'Egg', 1, '8.0', '2020-01-11'),
(48, 9889, 'Potato', 2, '80.0', '2020-01-11'),
(49, 9889, 'Egg', 2, '16.0', '2020-01-11'),
(50, 8427, 'Potato', 1, '40.0', '2020-01-11'),
(51, 8427, 'Egg', 3, '24.0', '2020-01-11'),
(52, 9897, 'Egg', 3, '24.0', '2020-01-11'),
(53, 5816, 'Potato', 2, '80.0', '2020-01-11'),
(54, 5816, 'Egg', 2, '16.0', '2020-01-11'),
(55, 7287, 'Potato', 2, '80.0', '2020-01-11'),
(56, 7287, 'Egg', 3, '24.0', '2020-01-11'),
(57, 5866, 'Egg', 1, '8.0', '2020-01-11'),
(58, 5866, 'Egg', 1, '8.0', '2020-01-11'),
(59, 6709, 'Egg', 10, '80.0', '2020-01-11'),
(60, 7487, 'Egg', 3, '24.0', '2020-01-11'),
(61, 9015, 'Potato', 1, '40.0', '2020-01-11'),
(62, 6836, 'Potato', 1, '40.0', '2020-01-11'),
(63, 6836, 'Egg', 2, '16.0', '2020-01-11'),
(64, 6836, 'Onion', 3, '540.0', '2020-01-11');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `inventory`
--
ALTER TABLE `inventory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transaction`
--
ALTER TABLE `transaction`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `inventory`
--
ALTER TABLE `inventory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `transaction`
--
ALTER TABLE `transaction`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
