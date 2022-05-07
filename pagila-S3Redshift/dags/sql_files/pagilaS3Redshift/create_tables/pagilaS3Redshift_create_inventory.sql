CREATE TABLE IF NOT EXISTS myschema.inventory
(
	inventory_id INTEGER NOT NULL DISTKEY SORTKEY,
    film_id SMALLINT NOT NULL,
    store_id SMALLINT NOT NULL,
    last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT now(),
    PRIMARY KEY (inventory_id)
);
