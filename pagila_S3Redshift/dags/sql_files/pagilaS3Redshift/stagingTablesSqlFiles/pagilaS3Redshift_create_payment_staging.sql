CREATE TABLE IF NOT EXISTS myschema.payment_staging
(
	payment_id INTEGER NOT NULL DISTKEY SORTKEY,
    customer_id SMALLINT NOT NULL,
    staff_id SMALLINT NOT NULL,
    rental_id INTEGER NOT NULL,
    amount DECIMAL(5,2) NOT NULL,
    payment_date TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    PRIMARY KEY (payment_id)
);
