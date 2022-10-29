# ATM Management System
CREATE DATABASE IF NOT EXISTS `bank` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `bank`;

-- --------------------------------------------------------

--
-- Table structure for table `atm`
--

CREATE TABLE `atm` (
  `ID` int(11) NOT NULL,
  `My_AC_No` varchar(255) NOT NULL,
  `My_IFSC` varchar(255) NOT NULL,
  `My_Name` varchar(255) NOT NULL,
  `My_PIN` varchar(255) NOT NULL,
  `My_Balance` varchar(255) NOT NULL,
  `Phone_Number` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

    
![alt text](https://samrat-sarkar.github.io/ATM_Management_System/screenshots/1.png)
![alt text](https://samrat-sarkar.github.io/ATM_Management_System/screenshots/2.png)
![alt text](https://samrat-sarkar.github.io/ATM_Management_System/screenshots/3.png)
![alt text](https://samrat-sarkar.github.io/ATM_Management_System/screenshots/4.png)
![alt text](https://samrat-sarkar.github.io/ATM_Management_System/screenshots/5.png)
![alt text](https://samrat-sarkar.github.io/ATM_Management_System/screenshots/6.png)
