-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 04, 2024 at 09:19 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `class`
--

INSERT INTO `class` (`ClassID`, `CourseID`, `LecturerID`, `RoomID`, `Day`, `Time`, `Length`) VALUES
(1237, '1804ICT', 12345, '2_20', 'Wed', '15:00:00.040', 120),
(8787, '7003ICT', 14567, '2_34', 'Thu', '15:00:00.898', 120);

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `CourseID` varchar(8) NOT NULL,
  `CourseName` text NOT NULL,
  `Description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`CourseID`, `CourseName`, `Description`) VALUES
('1804ICT', 'Data Management', 'Database design and implementation'),
('7003ICT', 'Database Management', 'Database design and implementation');

-- --------------------------------------------------------

--
-- Table structure for table `lecturer`
--

CREATE TABLE `lecturer` (
  `LecturerID` int(11) NOT NULL,
  `LecturerFirstName` text NOT NULL,
  `LecturerSurname` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `lecturer`
--

INSERT INTO `lecturer` (`LecturerID`, `LecturerFirstName`, `LecturerSurname`) VALUES
(12345, 'Mohammad', 'Awrangjeb'),
(14567, 'John', 'Patrick');

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `RoomID` varchar(4) NOT NULL,
  `RoomType` text NOT NULL,
  `Building` varchar(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`RoomID`, `RoomType`, `Building`) VALUES
('1.17', 'Laboratory', 'N53'),
('1.18', 'Laboratory', 'N44'),
('244', 'Seminar room', 'N78'),
('2_20', 'Academic room', 'N22'),
('2_34', 'Laboratory', 'N44'),
('Ttr1', 'Lecture theatre', 'N22');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `class`
--
ALTER TABLE `class`
  ADD PRIMARY KEY (`ClassID`),
  ADD KEY `CourseID` (`CourseID`,`LecturerID`,`RoomID`),
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
