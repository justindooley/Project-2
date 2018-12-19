CREATE DATABASE beer_db;
USE beer_db;

ALTER TABLE beer_data
MODIFY COLUMN ID VARCHAR(100);

ALTER TABLE beer_data
ADD PRIMARY KEY (ID);

SELECT * FROM beer_data;

CREATE DATABASE beer_review_db;

USE beer_review_db;

SELECT * FROM beer_review;

CREATE DATABASE beer_adv_db;

USE beer_adv_db;

SELECT * FROM beer_advocate_data;