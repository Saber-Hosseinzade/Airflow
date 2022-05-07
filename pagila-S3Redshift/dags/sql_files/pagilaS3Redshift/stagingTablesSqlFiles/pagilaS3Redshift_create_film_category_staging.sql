CREATE TABLE IF NOT EXISTS myschema.film_category_staging
(
	film_id SMALLINT NOT NULL DISTKEY SORTKEY,
    category_id SMALLINT NOT NULL,
    last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT now(),
    PRIMARY KEY (film_id, category_id)
);
