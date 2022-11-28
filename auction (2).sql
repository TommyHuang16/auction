-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2022-11-28 09:43:53
-- 伺服器版本： 10.4.24-MariaDB
-- PHP 版本： 8.1.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `auction`
--

-- --------------------------------------------------------

--
-- 資料表結構 `auctioninfo`
--

CREATE TABLE `auctioninfo` (
  `aid` int(10) NOT NULL,
  `uid` int(10) NOT NULL,
  `id` int(10) NOT NULL,
  `price` int(10) NOT NULL,
  `uName` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `auctioninfo`
--

INSERT INTO `auctioninfo` (`aid`, `uid`, `id`, `price`, `uName`) VALUES
(1, 1, 1, 2100, '阿明'),
(2, 2, 2, 3000, 'Eric'),
(3, 1, 2, 3100, '阿明'),
(4, 4, 1, 3500, '黃兄');

-- --------------------------------------------------------

--
-- 資料表結構 `auctionlist`
--

CREATE TABLE `auctionlist` (
  `id` int(10) NOT NULL,
  `name` varchar(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `expireTime` datetime NOT NULL,
  `price` int(10) NOT NULL,
  `uid` int(10) NOT NULL,
  `uName` varchar(10) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL DEFAULT '尚未競標'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `auctionlist`
--

INSERT INTO `auctionlist` (`id`, `name`, `expireTime`, `price`, `uid`, `uName`) VALUES
(1, '競標物A', '2022-12-05 15:42:50', 3500, 0, '黃兄'),
(2, '拍賣品B', '2022-12-05 15:43:13', 3100, 0, '阿明');

-- --------------------------------------------------------

--
-- 資料表結構 `user`
--

CREATE TABLE `user` (
  `uid` int(11) NOT NULL,
  `uName` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `user`
--

INSERT INTO `user` (`uid`, `uName`) VALUES
(1, '阿明'),
(2, 'Eric'),
(4, '黃兄');

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `auctioninfo`
--
ALTER TABLE `auctioninfo`
  ADD PRIMARY KEY (`aid`);

--
-- 資料表索引 `auctionlist`
--
ALTER TABLE `auctionlist`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`uid`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `auctioninfo`
--
ALTER TABLE `auctioninfo`
  MODIFY `aid` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `auctionlist`
--
ALTER TABLE `auctionlist`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `user`
--
ALTER TABLE `user`
  MODIFY `uid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
