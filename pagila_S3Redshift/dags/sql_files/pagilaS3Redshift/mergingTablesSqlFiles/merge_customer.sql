BEGIN TRANSACTION;

DELETE
FROM myschema.customer
    USING myschema.customer_staging
WHERE customer.customer_id = customer_staging.customer_id;

INSERT INTO myschema.customer
SELECT * FROM myschema.customer_staging;

END TRANSACTION;