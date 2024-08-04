-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 17, 2017 at 07:11 AM
-- Server version: 10.1.22-MariaDB
-- PHP Version: 7.1.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `myuniversity`
--

-- --------------------------------------------------------

--
-- Table structure for table `class`
--

CREATE TABLE `class` (
  `ClassID` int(11) NOT NULL,
  `CourseID` varchar(8) NOT NULL,
  `LecturerID` int(11) NOT NULL,
  `RoomID` varchar(4) NOT NULL,
  `Day` char(4) NOT NULL,
  `Time` time(3) NOT NULL,
  `Length` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `class`
--

INSERT INTO `class` (`ClassID`, `CourseID`, `LecturerID`, `RoomID`, `Day`, `Time`, `Length`) VALUES
(1237, '1804ICT', 12345, '2_20', 'Wed', '15:00:00.000', 120),
(6885, '7003ICT', 14343, '2_34', 'Thu', '11:00:00.000', 120);

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `CourseID` varchar(8) NOT NULL,
  `CourseName` text NOT NULL,
  `Description` text NOT NULL,
  `CreditPoints` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`CourseID`, `CourseName`, `Description`, `CreditPoints`) VALUES
('1804ICT', 'Data Management', 'Database design and implementation', 10),
('7003ICT', 'Database Management', 'Database design and implementation', 10);

-- --------------------------------------------------------

--
-- Table structure for table `lecturer`
--

CREATE TABLE `lecturer` (
  `LecturerID` int(11) NOT NULL,
  `LecturerFirstName` text NOT NULL,
  `LecturerSurname` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `lecturer`
--

INSERT INTO `lecturer` (`LecturerID`, `LecturerFirstName`, `LecturerSurname`) VALUES
(12345, 'Mohammad', 'Awrangjeb'),
(14343, 'John', 'Patrick');

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `RoomID` varchar(4) NOT NULL,
  `RoomType` text NOT NULL,
  `Building` varchar(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`RoomID`, `RoomType`, `Building`) VALUES
('2_20', 'Lecture room', 'N22'),
('2_34', 'Laboratories', 'N44');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `class`
--
ALTER TABLE `class`
  ADD PRIMARY KEY (`ClassID`),
  ADD KEY `CourseID` (`CourseID`),
  ADD KEY `LecturerID` (`LecturerID`),
  ADD KEY `RoomID` (`RoomID`);

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`CourseID`);

--
-- Indexes for table `lecturer`
--
ALTER TABLE `lecturer`
  ADD PRIMARY KEY (`LecturerID`);

--
-- Indexes for table `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`RoomID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `lecturer`
--
ALTER TABLE `lecturer`
  MODIFY `LecturerID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14344;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `class`
--
ALTER TABLE `class`
  ADD CONSTRAINT `class_ibfk_1` FOREIGN KEY (`CourseID`) REFERENCES `course` (`CourseID`),
  ADD CONSTRAINT `class_ibfk_2` FOREIGN KEY (`LecturerID`) REFERENCES `lecturer` (`LecturerID`),
  ADD CONSTRAINT `class_ibfk_3` FOREIGN KEY (`RoomID`) REFERENCES `room` (`RoomID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
