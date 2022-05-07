CREATE TABLE IF NOT EXISTS myschema.actor
(
	actor_id INTEGER DISTKEY SORTKEY,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45)  NOT NULL,
    last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT now(),
	PRIMARY KEY (actor_id)
);
