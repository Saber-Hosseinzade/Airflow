CREATE TABLE IF NOT EXISTS myschema.address_staging
(
	address_id INTEGER DISTKEY SORTKEY,
    address VARCHAR(50) NOT NULL,
	address2 VARCHAR(50) NOT NULL,
	district VARCHAR(20) NOT NULL,
	city_id SMALLINT NOT NULL,
	postal_code VARCHAR(10) NOT NULL,
	phone VARCHAR(20) NOT NULL,
    last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT now(),
	PRIMARY KEY (address_id)
);
