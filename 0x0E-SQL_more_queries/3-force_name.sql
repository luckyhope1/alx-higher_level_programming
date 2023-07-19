-- Task: Create table force_name in the specified MySQL database
CREATE TABLE IF NOT EXISTS $DB_NAME.force_name (
  id INT,
  name VARCHAR(256) NOT NULL
);
