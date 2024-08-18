-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 18, 2024 at 09:26 AM
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
-- Database: `codingenthusiast`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `phone_num` int(50) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime DEFAULT current_timestamp(),
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `phone_num`, `msg`, `date`, `email`) VALUES
(1, 'first post', 123456789, 'first post', '2024-07-26 20:35:28', 'firstpost@gmail.com'),
(2, 'heyyy', 2147483647, 'whatsuppp peopleeeee', NULL, 'heyyy@gmail.com'),
(3, 'heyyy', 2147483647, 'whatsuppp peopleeeee', '2024-07-26 21:10:09', 'heyyy@gmail.com'),
(4, 'bhitika', 2147483647, 'bhitika pal here want to share some news', '2024-07-27 12:30:25', 'bhitikapal@gmail.com'),
(5, 'ddddfdd', 2147483647, 'heyyy broooooooo', '2024-07-28 12:58:09', 'ddf@ffm.com'),
(12, 'pratyush', 2147483647, 'hey thiiss side pratyush', '2024-07-29 12:44:04', 'pratyush@gmail.com'),
(13, 'ddddfdd', 2147483647, 'hey hi hello', '2024-07-29 12:50:02', 'ddf@ffm.com');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `tagline` text NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` text NOT NULL,
  `img_file` varchar(12) NOT NULL,
  `date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `tagline`, `slug`, `content`, `img_file`, `date`) VALUES
(1, 'STOCK MARKET ', 'this is my post', 'first-post', 'A stock market, equity market, or share market is the aggregation of buyers and sellers of stocks (also called shares), which represent ownership claims on businesses; these may include securities listed on a public stock exchange as well as stock that is only traded privately, such as shares of private companies that are sold to investors through equity crowdfunding platforms. Investments are usually made with an investment strategy in mind.', 'about-bg.jpg', '2024-08-10 13:15:40.000000'),
(2, 'This is second post', 'coolest post ever', 'second-post', 'Some exchanges are physical locations where transactions are carried out on a trading floor, by a method known as open outcry. This method is used in some stock exchanges and commodities exchanges, and involves traders shouting bid and offer prices. The other type of stock exchange has a network of computers where trades are made electronically. An example of such an exchange is the NASDAQ.', 'home-bg.jpg', '2024-07-31 12:11:56.000000'),
(3, 'Variables ', 'Complete Knowledge of Variables', 'third-post', 'A variable is any characteristic, number, or quantity that can be measured or counted. A variable may also be called a data item. Age, sex, business income and expenses, country of birth, capital expenditure, class grades, eye colour and vehicle type are examples of variables. It is called a variable because the value may vary between data units in a population, and may change in value over time.\r\n\r\nFor example; \'income\' is a variable that can vary between data units in a population (i.e. the people or businesses being studied may not have the same incomes) and can also vary over time for each data unit (i.e. income can go up or down).', '', '2024-07-31 12:28:02.000000'),
(4, 'Keywords', 'Everything cleared about keywords', 'fourth-post', 'The objective of keyword research is to generate, with good precision and recall, a large number of terms that are highly relevant yet non-obvious to the given input keyword.[1] The process of keyword research involves brainstorming and the use of keyword research tools, with popular ones including Semrush and Google Trends. To achieve the best SEO results, it is important to optimize a website\'s content as well as backlinks for the most relevant keywords. It is good practice to search for related keywords that have low competition and still a high number of searches. This makes it easier to achieve a higher rank in search engines which usually results in higher web traffic and, ideally, conversions. The downside of this practice is that the website is optimized for alternative keywords instead of the main keyword; main keywords might be very difficult to rank due to high competition.[2] There are three essential concepts to consider when conducting keyword research. Good keywords are closely related to the subject of the website. Most search engines use an internal quality system to check website relevance related to possible keywords, a non-relevant keyword is unlikely to rank well for a website.[3] Good keywords that are highly competitive are less likely to rank at the top. Keywords that have no monthly searches are believed to generate little to no traffic and therefore of little value for SEO. Keyword stuffing on a web page should be avoided.', '', '2024-07-31 12:28:02.000000'),
(5, 'Whitespace control', 'Everything about whitespace', 'slug-next', 'Text documents are the final result of rendering templates. Depending on the end consumer of these documents whitespace placement could be significant. One of the major niggles in Jinja2, in my opinion, is the way control statements and other elements affect whitespace output in the end documents.\r\n\r\nTo put it bluntly, mastering whitespaces in Jinja2 is the only way of making sure your templates generate text exactly the way you intended.\r\n\r\nNow we know the importance of the problem, time to understand where it originates, to do that we’ll have a look at a lot of examples. Then we\'ll learn how we can control rendering whitespaces in Jinja2 templates.', '', '2024-07-31 12:30:01.000000'),
(12, 'STOCK MARKET ', 'this is my post', 'first-post', 'A stock market, equity market, or share market is the aggregation of buyers and sellers of stocks (also called shares), which represent ownership claims on businesses; these may include securities listed on a public stock exchange as well as stock that is only traded privately, such as shares of private companies that are sold to investors through equity crowdfunding platforms. Investments are usually made with an investment strategy in mind.', 'about-bg.jpg', '2024-08-14 12:25:33.545469'),
(13, ' itrochondria', '', '', '', '', '2024-08-14 12:38:59.578443'),
(14, 'Mitrochomndria', 'Chapter-9', 'science', 'Mitochondria are membrane-bound organelles, but they\'re membrane-bound with two different membranes. And that\'s quite unusual for an intercellular organelle. Those membranes function in the purpose of mitochondria, which is essentially to produce energy. That energy is produced by having chemicals within the cell go through pathways, in other words, be converted. And the process of that conversion produces energy in the form of ATP, because the phosphate is a high-energy bond and provides energy for other reactions within the cell. So the mitochondria\'s purpose is to produce that energy. Some different cells have different amounts of mitochondria because they need more energy. So for example, the muscle has a lot of mitochondria, the liver does too, the kidney as well, and to a certain extent, the brain, which lives off of the energy those mitochondria produce. So if you have a defect in the pathways that the mitochondria usually functions with, you\'re going to have symptoms in the muscle, in the brain, sometimes in the kidneys as well; many different types of symptoms. And we probably don\'t know all of the different diseases that mitochondrial dysfunction causes.', 'mitrochondri', '2024-08-14 12:42:16.923415'),
(15, 'Mitrochondria', 'Chapter-9', 'science', 'Mitochondria are membrane-bound organelles, but they\'re membrane-bound with two different membranes. And that\'s quite unusual for an intercellular organelle. Those membranes function in the purpose of mitochondria, which is essentially to produce energy. That energy is produced by having chemicals within the cell go through pathways, in other words, be converted. And the process of that conversion produces energy in the form of ATP, because the phosphate is a high-energy bond and provides energy for other reactions within the cell. So the mitochondria\'s purpose is to produce that energy. Some different cells have different amounts of mitochondria because they need more energy. So for example, the muscle has a lot of mitochondria, the liver does too, the kidney as well, and to a certain extent, the brain, which lives off of the energy those mitochondria produce. So if you have a defect in the pathways that the mitochondria usually functions with, you\'re going to have symptoms in the muscle, in the brain, sometimes in the kidneys as well; many different types of symptoms. And we probably don\'t know all of the different diseases that mitochondrial dysfunction causes.', 'mitrochondri', '2024-08-14 12:42:30.932533');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `Name` text NOT NULL,
  `email` varchar(20) NOT NULL,
  `password` text NOT NULL,
  `confirm_password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`Name`, `email`, `password`, `confirm_password`) VALUES
('hi', 'heyyy@gmail.com', 'pratyush', 'pratyush'),
('sakshi', 'saksho@gmail.com', 'sakshi', 'sakshi'),
('Mohammad Izhaan', 'mdizhaan21@gmail.com', 'izhaandon123', 'izhaandon123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
