-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-04-2025 a las 03:25:49
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `flask_login`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id` smallint(6) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` text NOT NULL,
  `fullname` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `fullname`) VALUES
(1, 'BryanA26', 'scrypt:32768:8:1$nCzBUZkz8JX2r8C2$b1b1ace6192f7442f57ba6c1b1b36718fac579be3140f6504b3ea7649cc3e60fc6020c6632fbef307caac4e3181b1d09942644aad703950a3309f3daeaa0ceae', 'Brayan Andrey Agudelo Echavarria'),
(3, 'pedro', 'scrypt:32768:8:1$V5e2LJ0OefUuB3or$f5ec19c66a9e91909a34fbbe7ec7e25df7515f4271bdf06ef98193aade8a1db5290f', 'Pedro Pablo Jacinto Jose'),
(6, 'lupita', 'scrypt:32768:8:1$zqMv7gYfbHLoFlpq$de67d0c15eb9f0ea2770afa9892a201476c358b49063919874444dc0ea8f0e811e026dd7aec3d80b079ac895145f044e2b13ed517687485a68c2256bab22c70a', 'lupe ramirez'),
(7, 'nacional', 'scrypt:32768:8:1$39fwLcPRTbtudQR2$fc52ff438c0dc0a45e3f7a56cd8165fe390bb4e5f4532cfa6958b15631b0c993e15be22391096db955c32a9261e575ebb2f2a7d49a7d447d12e52375486e80c2', 'atl nacional');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` smallint(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
