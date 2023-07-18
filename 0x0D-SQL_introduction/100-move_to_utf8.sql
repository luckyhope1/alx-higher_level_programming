-- Script to convert hbtn_0c_0 database, first_table table, and name field to
-- UTF8 (utf8mb4) in MySQL server
USE hbtn_0c_0;
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE
utf8mb4_unicode_ci;
