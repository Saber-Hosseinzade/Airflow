CREATE TABLE IF NOT EXISTS myschema.country
(
	country_id INTEGER DISTKEY SORTKEY,
    country VARCHAR(50) NOT NULL,
    last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT now(),
	PRIMARY KEY (country_id)
);
