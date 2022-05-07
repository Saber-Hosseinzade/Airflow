BEGIN TRANSACTION;

DELETE
FROM myschema.staff
    USING myschema.staff_staging
WHERE staff.staff_id = staff_staging.staff_id;

INSERT INTO myschema.staff
SELECT * FROM myschema.staff_staging;

END TRANSACTION;