CREATE TABLE IF NOT EXISTS myschema.language_staging
(
	language_id INTEGER NOT NULL DISTKEY SORTKEY,
    name CHAR(20) NOT NULL,
    last_update TIMESTAMP WITHOUT TIME ZONE NOT NULL DEFAULT now(),
    PRIMARY KEY (language_id)
);
