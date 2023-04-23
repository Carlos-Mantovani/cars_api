CREATE DATABASE flask_api_cars

USE flask_api_cars

CREATE TABLE cars (
	id INTEGER NOT NULL AUTO_INCREMENT,
	brand VARCHAR(100),
	model VARCHAR(100),
	year INTEGER,
	PRIMARY KEY (id)
)