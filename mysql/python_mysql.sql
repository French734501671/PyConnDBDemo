/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50709
Source Host           : localhost:3306
Source Database       : python_mysql

Target Server Type    : MYSQL
Target Server Version : 50709
File Encoding         : 65001

Date: 2017-03-13 23:53:40
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for account
-- ----------------------------
DROP TABLE IF EXISTS `account`;
CREATE TABLE `account` (
  `acctid` int(11) NOT NULL COMMENT '账户ID',
  `money` int(11) NOT NULL COMMENT '账户余额'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of account
-- ----------------------------
INSERT INTO `account` VALUES ('11', '800');
INSERT INTO `account` VALUES ('12', '300');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'c');
INSERT INTO `user` VALUES ('2', 'python');
INSERT INTO `user` VALUES ('3', 'java');
INSERT INTO `user` VALUES ('4', 'ruby');
INSERT INTO `user` VALUES ('5', 'july');
