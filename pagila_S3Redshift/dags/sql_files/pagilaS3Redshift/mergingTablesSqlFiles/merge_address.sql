BEGIN TRANSACTION;

DELETE
FROM myschema.address
    USING myschema.address_staging
WHERE address.address_id = address_staging.address_id;

INSERT INTO myschema.address
SELECT * FROM myschema.address_staging;

END TRANSACTION;