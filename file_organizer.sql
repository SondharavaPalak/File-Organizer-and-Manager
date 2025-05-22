-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 27, 2025 at 11:47 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `file organizer`
--

-- --------------------------------------------------------

--
-- Table structure for table `deleted_files`
--

CREATE TABLE `deleted_files` (
  `id` int(11) NOT NULL,
  `file_name` varchar(255) DEFAULT NULL,
  `original_path` varchar(255) DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `deleted_files`
--

INSERT INTO `deleted_files` (`id`, `file_name`, `original_path`, `deleted_at`) VALUES
(1, 't.txt', 'D:/Temp', '2025-02-27 15:38:42');

-- --------------------------------------------------------

--
-- Table structure for table `edited_files`
--

CREATE TABLE `edited_files` (
  `id` int(11) NOT NULL,
  `file_name` varchar(255) NOT NULL,
  `original_path` varchar(255) NOT NULL,
  `edit_content` longtext NOT NULL,
  `edited_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `edited_files`
--

INSERT INTO `edited_files` (`id`, `file_name`, `original_path`, `edit_content`, `edited_at`) VALUES
(1, 'edit.txt', 'D:/Temp', 'Hello!!!!', '2025-02-27 16:10:43');

-- --------------------------------------------------------

--
-- Table structure for table `organized_files`
--

CREATE TABLE `organized_files` (
  `id` int(11) NOT NULL,
  `file_name` varchar(255) NOT NULL,
  `original_path` varchar(255) NOT NULL,
  `target_path` varchar(255) NOT NULL,
  `move_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `organized_files`
--

INSERT INTO `organized_files` (`id`, `file_name`, `original_path`, `target_path`, `move_date`) VALUES
(1, 'app.py', 'D:/Temp\\app.py', 'D:/Temp\\Code Files\\Programming Language Files\\app.py', '2025-02-26 16:02:29'),
(2, 'db.php', 'D:/Temp\\db.php', 'D:/Temp\\Code Files\\Programming Language Files\\db.php', '2025-02-26 16:02:29'),
(3, 'demo.mp4', 'D:/Temp\\demo.mp4', 'D:/Temp\\Video Files\\Video Formats\\demo.mp4', '2025-02-26 16:02:29'),
(4, 'doctor.php', 'D:/Temp\\doctor.php', 'D:/Temp\\Code Files\\Programming Language Files\\doctor.php', '2025-02-26 16:02:29'),
(5, 'ES6.html', 'D:/Temp\\ES6.html', 'D:/Temp\\Code Files\\Programming Language Files\\ES6.html', '2025-02-26 16:02:29'),
(6, 'fatArrowFunction.html', 'D:/Temp\\fatArrowFunction.html', 'D:/Temp\\Code Files\\Programming Language Files\\fatArrowFunction.html', '2025-02-26 16:02:29'),
(7, 'file_organizer_log.txt', 'D:/Temp\\file_organizer_log.txt', 'D:/Temp\\Document Files\\Text Files\\file_organizer_log.txt', '2025-02-26 16:02:29'),
(8, 'home.js', 'D:/Temp\\home.js', 'D:/Temp\\Code Files\\Programming Language Files\\home.js', '2025-02-26 16:02:29'),
(9, 'home.php', 'D:/Temp\\home.php', 'D:/Temp\\Code Files\\Programming Language Files\\home.php', '2025-02-26 16:02:29'),
(10, 'home.zip', 'D:/Temp\\home.zip', 'D:/Temp\\Document Files\\Compressed Files\\home.zip', '2025-02-26 16:02:29'),
(11, 'home9Feb.zip', 'D:/Temp\\home9Feb.zip', 'D:/Temp\\Document Files\\Compressed Files\\home9Feb.zip', '2025-02-26 16:02:29'),
(12, 'IPE_Schedule_Sem-3_SY ALL_ODD 2024.pdf', 'D:/Temp\\IPE_Schedule_Sem-3_SY ALL_ODD 2024.pdf', 'D:/Temp\\Document Files\\PDF Files\\IPE_Schedule_Sem-3_SY ALL_ODD 2024.pdf', '2025-02-26 16:02:29'),
(13, 'pic1.jpg', 'D:/Temp\\pic1.jpg', 'D:/Temp\\Image Files\\Raster Image Files\\pic1.jpg', '2025-02-26 16:02:29'),
(14, 'pic2.jpg', 'D:/Temp\\pic2.jpg', 'D:/Temp\\Image Files\\Raster Image Files\\pic2.jpg', '2025-02-26 16:02:29'),
(15, 'pic3.jpg', 'D:/Temp\\pic3.jpg', 'D:/Temp\\Image Files\\Raster Image Files\\pic3.jpg', '2025-02-26 16:02:29'),
(16, 'Project_schedule Sem-3_SY ALL_ODD 2024.pdf', 'D:/Temp\\Project_schedule Sem-3_SY ALL_ODD 2024.pdf', 'D:/Temp\\Document Files\\PDF Files\\Project_schedule Sem-3_SY ALL_ODD 2024.pdf', '2025-02-26 16:02:29'),
(17, 'r1.jpg', 'D:/Temp\\r1.jpg', 'D:/Temp\\Image Files\\Raster Image Files\\r1.jpg', '2025-02-26 16:02:29'),
(18, 'Screenshot 2025-02-18 165944.png', 'D:/Temp\\Screenshot 2025-02-18 165944.png', 'D:/Temp\\Image Files\\Raster Image Files\\Screenshot 2025-02-18 165944.png', '2025-02-26 16:02:29'),
(19, 'Screenshot 2025-02-21 212800.png', 'D:/Temp\\Screenshot 2025-02-21 212800.png', 'D:/Temp\\Image Files\\Raster Image Files\\Screenshot 2025-02-21 212800.png', '2025-02-26 16:02:29'),
(20, 'temp.css', 'D:/Temp\\temp.css', 'D:/Temp\\Code Files\\Programming Language Files\\temp.css', '2025-02-26 16:02:29'),
(21, 'temp.txt', 'D:/Temp\\temp.txt', 'D:/Temp\\Document Files\\Text Files\\temp.txt', '2025-02-26 16:02:29'),
(22, 'ES6.html', 'D:/Temp\\ES6.html', 'D:/Temp\\Code Files\\Programming Language Files\\ES6.html', '2025-02-26 19:22:45'),
(23, 'fatArrowFunction.html', 'D:/Temp\\fatArrowFunction.html', 'D:/Temp\\Code Files\\Programming Language Files\\fatArrowFunction.html', '2025-02-26 19:22:45'),
(24, 'file_organizer_log.txt', 'D:/Temp\\file_organizer_log.txt', 'D:/Temp\\Document Files\\Text Files\\file_organizer_log.txt', '2025-02-26 19:22:45'),
(25, 'home.js', 'D:/Temp\\home.js', 'D:/Temp\\Code Files\\Programming Language Files\\home.js', '2025-02-26 19:22:45'),
(26, 'home.php', 'D:/Temp\\home.php', 'D:/Temp\\Code Files\\Programming Language Files\\home.php', '2025-02-26 19:22:45'),
(27, 'home.zip', 'D:/Temp\\home.zip', 'D:/Temp\\Document Files\\Compressed Files\\home.zip', '2025-02-26 19:22:45'),
(28, 'home9Feb.zip', 'D:/Temp\\home9Feb.zip', 'D:/Temp\\Document Files\\Compressed Files\\home9Feb.zip', '2025-02-26 19:22:45'),
(29, 'IPE_Schedule_Sem-3_SY ALL_ODD 2024.pdf', 'D:/Temp\\IPE_Schedule_Sem-3_SY ALL_ODD 2024.pdf', 'D:/Temp\\Document Files\\PDF Files\\IPE_Schedule_Sem-3_SY ALL_ODD 2024.pdf', '2025-02-26 19:22:45'),
(30, 'pic1.jpg', 'D:/Temp\\pic1.jpg', 'D:/Temp\\Image Files\\Raster Image Files\\pic1.jpg', '2025-02-26 19:22:45'),
(31, 'pic2.jpg', 'D:/Temp\\pic2.jpg', 'D:/Temp\\Image Files\\Raster Image Files\\pic2.jpg', '2025-02-26 19:22:45'),
(32, 'pic3.jpg', 'D:/Temp\\pic3.jpg', 'D:/Temp\\Image Files\\Raster Image Files\\pic3.jpg', '2025-02-26 19:22:45'),
(33, 'Project_schedule Sem-3_SY ALL_ODD 2024.pdf', 'D:/Temp\\Project_schedule Sem-3_SY ALL_ODD 2024.pdf', 'D:/Temp\\Document Files\\PDF Files\\Project_schedule Sem-3_SY ALL_ODD 2024.pdf', '2025-02-26 19:22:45'),
(34, 'r1.jpg', 'D:/Temp\\r1.jpg', 'D:/Temp\\Image Files\\Raster Image Files\\r1.jpg', '2025-02-26 19:22:45'),
(35, 'temp.css', 'D:/Temp\\temp.css', 'D:/Temp\\Code Files\\Programming Language Files\\temp.css', '2025-02-26 19:22:45'),
(36, 'temp.txt', 'D:/Temp\\temp.txt', 'D:/Temp\\Document Files\\Text Files\\temp.txt', '2025-02-26 19:22:45'),
(37, 'app.py', 'D:/Temp\\app.py', 'D:/Temp\\Code Files\\Programming Language Files\\app.py', '2025-02-27 15:09:15'),
(38, 'db.php', 'D:/Temp\\db.php', 'D:/Temp\\Code Files\\Programming Language Files\\db.php', '2025-02-27 15:09:15'),
(39, 'demo.mp4', 'D:/Temp\\demo.mp4', 'D:/Temp\\Video Files\\Video Formats\\demo.mp4', '2025-02-27 15:09:15'),
(40, 'doctor.php', 'D:/Temp\\doctor.php', 'D:/Temp\\Code Files\\Programming Language Files\\doctor.php', '2025-02-27 15:09:15'),
(41, 'ES6.html', 'D:/Temp\\ES6.html', 'D:/Temp\\Code Files\\Programming Language Files\\ES6.html', '2025-02-27 15:09:16'),
(42, 'fatArrowFunction.html', 'D:/Temp\\fatArrowFunction.html', 'D:/Temp\\Code Files\\Programming Language Files\\fatArrowFunction.html', '2025-02-27 15:09:16'),
(43, 'file_organizer_log.txt', 'D:/Temp\\file_organizer_log.txt', 'D:/Temp\\Document Files\\Text Files\\file_organizer_log.txt', '2025-02-27 15:09:16'),
(44, 'home.js', 'D:/Temp\\home.js', 'D:/Temp\\Code Files\\Programming Language Files\\home.js', '2025-02-27 15:09:16'),
(45, 'home.php', 'D:/Temp\\home.php', 'D:/Temp\\Code Files\\Programming Language Files\\home.php', '2025-02-27 15:09:16'),
(46, 'home.zip', 'D:/Temp\\home.zip', 'D:/Temp\\Document Files\\Compressed Files\\home.zip', '2025-02-27 15:09:16'),
(47, 'home9Feb.zip', 'D:/Temp\\home9Feb.zip', 'D:/Temp\\Document Files\\Compressed Files\\home9Feb.zip', '2025-02-27 15:09:16'),
(48, 'IPE_Schedule_Sem-3_SY ALL_ODD 2024.pdf', 'D:/Temp\\IPE_Schedule_Sem-3_SY ALL_ODD 2024.pdf', 'D:/Temp\\Document Files\\PDF Files\\IPE_Schedule_Sem-3_SY ALL_ODD 2024.pdf', '2025-02-27 15:09:16'),
(49, 'pic1.jpg', 'D:/Temp\\pic1.jpg', 'D:/Temp\\Image Files\\Raster Image Files\\pic1.jpg', '2025-02-27 15:09:16'),
(50, 'pic2.jpg', 'D:/Temp\\pic2.jpg', 'D:/Temp\\Image Files\\Raster Image Files\\pic2.jpg', '2025-02-27 15:09:16'),
(51, 'pic3.jpg', 'D:/Temp\\pic3.jpg', 'D:/Temp\\Image Files\\Raster Image Files\\pic3.jpg', '2025-02-27 15:09:16'),
(52, 'Project_schedule Sem-3_SY ALL_ODD 2024.pdf', 'D:/Temp\\Project_schedule Sem-3_SY ALL_ODD 2024.pdf', 'D:/Temp\\Document Files\\PDF Files\\Project_schedule Sem-3_SY ALL_ODD 2024.pdf', '2025-02-27 15:09:16'),
(53, 'r1.jpg', 'D:/Temp\\r1.jpg', 'D:/Temp\\Image Files\\Raster Image Files\\r1.jpg', '2025-02-27 15:09:16'),
(54, 'temp.css', 'D:/Temp\\temp.css', 'D:/Temp\\Code Files\\Programming Language Files\\temp.css', '2025-02-27 15:09:16'),
(55, 'temp.txt', 'D:/Temp\\temp.txt', 'D:/Temp\\Document Files\\Text Files\\temp.txt', '2025-02-27 15:09:16');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `deleted_files`
--
ALTER TABLE `deleted_files`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `edited_files`
--
ALTER TABLE `edited_files`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `organized_files`
--
ALTER TABLE `organized_files`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `deleted_files`
--
ALTER TABLE `deleted_files`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `edited_files`
--
ALTER TABLE `edited_files`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `organized_files`
--
ALTER TABLE `organized_files`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
