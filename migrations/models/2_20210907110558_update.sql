-- upgrade --
ALTER TABLE `entry` ADD `Files` VARCHAR(500);
-- downgrade --
ALTER TABLE `entry` DROP COLUMN `Files`;
