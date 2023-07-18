-- Script to convert hbtn_0c_0 database, first_table table, and name field to
-- UTF8 (utf8mb4) in MySQL server
ALTER DATABASE $database CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE $database.$table CONVERT TO CHARACTER SET utf8mb4 COLLATE
utf8mb4_unicode_ci;
ALTER TABLE $database.$table MODIFY COLUMN $field VARCHAR(256) CHARACTER SET
utf8mb4 COLLATE utf8mb4_unicode_ci;
