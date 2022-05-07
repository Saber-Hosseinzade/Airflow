CREATE TABLE IF NOT EXISTS myschema.store_staging
(
	store_id INTEGER NOT NULL DISTKEY SORTKEY,
    manager_staff_id SMALLINT NOT NULL,
    address_id SMALLINT NOT NULL,
    last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT now(),
    PRIMARY KEY (store_id)
);
