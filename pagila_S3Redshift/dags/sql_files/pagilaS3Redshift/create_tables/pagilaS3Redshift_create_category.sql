CREATE TABLE IF NOT EXISTS myschema.category
(
	category_id INTEGER DISTKEY SORTKEY,
    name VARCHAR(25) NOT NULL,
    last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT now(),
	PRIMARY KEY (category_id)
);
