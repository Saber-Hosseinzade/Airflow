CREATE TABLE IF NOT EXISTS myschema.film_actor
(
	actor_id SMALLINT NOT NULL DISTKEY SORTKEY,
    film_id SMALLINT NOT NULL,
    last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT now(),
    PRIMARY KEY (actor_id, film_id)
);
