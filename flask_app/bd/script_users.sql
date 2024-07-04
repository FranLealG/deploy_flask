-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema foro_publicaciones
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `foro_publicaciones` ;

-- -----------------------------------------------------
-- Schema foro_publicaciones
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `foro_publicaciones` DEFAULT CHARACTER SET utf8 ;
USE `foro_publicaciones` ;

-- -----------------------------------------------------
-- Table `foro_publicaciones`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `foro_publicaciones`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(100) NULL,
  `last_name` VARCHAR(100) NULL,
  `email` VARCHAR(200) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `foro_publicaciones`.`posts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `foro_publicaciones`.`posts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `content` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_posts_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_posts_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `foro_publicaciones`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `foro_publicaciones`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `foro_publicaciones`.`comments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `post_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `comment` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX `fk_posts_has_users_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_posts_has_users_posts1_idx` (`post_id` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_posts_has_users_posts1`
    FOREIGN KEY (`post_id`)
    REFERENCES `foro_publicaciones`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_posts_has_users_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `foro_publicaciones`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
