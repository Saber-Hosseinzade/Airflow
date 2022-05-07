BEGIN TRANSACTION;

DELETE
FROM myschema.payment
    USING myschema.payment_staging
WHERE payment.payment_id = payment_staging.payment_id
	AND payment_staging.payment_date BETWEEN '{{ params.begin_date }}' AND '{{ params.end_date }}';

INSERT INTO myschema.payment
SELECT * FROM myschema.payment_staging
WHERE payment_staging.payment_date BETWEEN '{{ params.begin_date }}' AND '{{ params.end_date }}';

END TRANSACTION;