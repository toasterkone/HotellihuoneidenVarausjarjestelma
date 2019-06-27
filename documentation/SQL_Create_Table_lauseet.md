# VarausApp - SQL CREATE TABLE -lauseet
- lauseiden avulla muodostetaan tietokannan taulut.

```
CREATE TABLE lisavaruste (
	id INTEGER NOT NULL, 
	nimi VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE huone (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	huonenumero INTEGER NOT NULL, 
	hinta INTEGER NOT NULL, 
	tyyppi VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE rooli (
	id INTEGER NOT NULL, 
	nimi VARCHAR(32) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	rooli_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(rooli_id) REFERENCES rooli (id)
);
CREATE TABLE huonelisavaruste (
	huone_id INTEGER NOT NULL, 
	lisavaruste_id INTEGER NOT NULL, 
	PRIMARY KEY (huone_id, lisavaruste_id), 
	FOREIGN KEY(huone_id) REFERENCES huone (id), 
	FOREIGN KEY(lisavaruste_id) REFERENCES lisavaruste (id)
);
CREATE TABLE asiakas (
	id INTEGER NOT NULL, 
	etunimi VARCHAR(144) NOT NULL, 
	sukunimi VARCHAR(144) NOT NULL, 
	puhelinnumero VARCHAR(144) NOT NULL, 
	email VARCHAR(144) NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);
CREATE TABLE varaus (
	id INTEGER NOT NULL, 
	varausviikko INTEGER NOT NULL, 
	hinta INTEGER NOT NULL, 
	asiakas_id INTEGER, 
	huone_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(asiakas_id) REFERENCES asiakas (id), 
	FOREIGN KEY(huone_id) REFERENCES huone (id)
);

```
