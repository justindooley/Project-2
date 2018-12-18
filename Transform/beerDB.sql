create database beerDB;
use beerDB;
select * from beer_data;

ALTER TABLE beer_data1
ADD PRIMARY KEY (ID);


ALTER TABLE beer_data1
MODIFY COLUMN ID VARCHAR(100);
