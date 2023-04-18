-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 18, 2023 at 02:22 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `DBaudio`
--

-- --------------------------------------------------------

--
-- Table structure for table `Singer`
--

CREATE TABLE `Singer` (
  `id` int(10) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Singer`
--

INSERT INTO `Singer` (`id`, `name`) VALUES
(1, 'Trung Quân'),
(2, 'Sơn Tùng'),
(3, 'Dương Tử'),
(4, 'Demo'),
(5, 'Remix');

-- --------------------------------------------------------

--
-- Table structure for table `Song`
--

CREATE TABLE `Song` (
  `id` int(10) NOT NULL,
  `name` varchar(50) NOT NULL,
  `link` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `idType` int(10) NOT NULL,
  `idSinger` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Song`
--

INSERT INTO `Song` (`id`, `name`, `link`, `image`, `idType`, `idSinger`) VALUES
(1, 'Tìm em', './music/TimEm.mp3', '', 5, 5),
(2, 'Tình đầu', './music/TinhDau.mp3', '', 4, 4),
(3, 'Tình yêu khủng long', './music/TinhYeuKhungLong.mp3', '', 3, 3),
(4, 'Tòng phu', './music/TongPhu.mp3', '', 2, 2),
(5, 'Trên tình bạn dưới tình yêu', './music/TrenTinhBanDuoiTinhYeu.mp3', '', 1, 1),
(6, 'Hắc Nguyệt Quang', './music/HacNguyetQuang.mp3', '', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `TypeSong`
--

CREATE TABLE `TypeSong` (
  `id` int(10) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `TypeSong`
--

INSERT INTO `TypeSong` (`id`, `name`) VALUES
(1, 'Nhạc trẻ'),
(2, 'Nhạc Trữ Tình'),
(3, 'Nhạc Không Lời'),
(4, 'Nhạc Hoa'),
(5, 'Nhạc Remix');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Singer`
--
ALTER TABLE `Singer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `Song`
--
ALTER TABLE `Song`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_keyType` (`idType`),
  ADD KEY `fk_keySinger` (`idSinger`);

--
-- Indexes for table `TypeSong`
--
ALTER TABLE `TypeSong`
  ADD PRIMARY KEY (`id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Song`
--
ALTER TABLE `Song`
  ADD CONSTRAINT `fk_keySinger` FOREIGN KEY (`idSinger`) REFERENCES `Singer` (`id`),
  ADD CONSTRAINT `fk_keyType` FOREIGN KEY (`idType`) REFERENCES `TypeSong` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
