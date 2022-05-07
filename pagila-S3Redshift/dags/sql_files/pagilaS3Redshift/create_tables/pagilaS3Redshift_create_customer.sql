CREATE TABLE IF NOT EXISTS myschema.customer
(
	customer_id INTEGER DISTKEY SORTKEY,
	store_id SMALLINT NOT NULL,
	first_name VARCHAR(45) NOT NULL,
	last_name VARCHAR(45) NOT NULL,
	email VARCHAR(50),
	address_id SMALLINT NOT NULL,
	activebool BOOLEAN NOT NULL DEFAULT true,
	create_date DATE NOT NULL DEFAULT ('now'::text)::date,
	last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT now(),
	active INTEGER,
	PRIMARY KEY (customer_id)
);
