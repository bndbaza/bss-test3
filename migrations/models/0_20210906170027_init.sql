-- upgrade --
CREATE TABLE IF NOT EXISTS `entry` (
    `Id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `RegNumber` VARCHAR(50) NOT NULL UNIQUE,
    `Date` DATE NOT NULL,
    `Organ` VARCHAR(250),
    `Address` VARCHAR(250),
    `Content` VARCHAR(250),
    `Sender` VARCHAR(250),
    `Wey` VARCHAR(250)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(20) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
