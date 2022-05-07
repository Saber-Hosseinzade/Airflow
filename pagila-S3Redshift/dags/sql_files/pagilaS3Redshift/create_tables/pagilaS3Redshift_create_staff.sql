CREATE TABLE IF NOT EXISTS myschema.staff
(
	staff_id INTEGER NOT NULL DISTKEY SORTKEY,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    address_id SMALLINT NOT NULL,
    email VARCHAR(50),
    store_id SMALLINT NOT NULL,
    active BOOLEAN NOT NULL DEFAULT true,
    username VARCHAR(16) NOT NULL,
    password VARCHAR(40),
    last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT now(),
    PRIMARY KEY (staff_id)
);
