CREATE TABLE IF NOT EXISTS myschema.film
(
	film_id INTEGER DISTKEY SORTKEY,
	title VARCHAR(255) NOT NULL,
	description TEXT,
	release_year INTEGER,
    language_id SMALLINT NOT NULL,
    rental_duration SMALLINT NOT NULL DEFAULT 3,
    rental_rate DECIMAL(4,2) NOT NULL DEFAULT 4.99,
    length SMALLINT,
    replacement_cost DECIMAL(5,2) NOT NULL DEFAULT 19.99,
    rating VARCHAR(10),
    last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT now(),
	PRIMARY KEY (film_id)
);
