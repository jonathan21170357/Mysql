CREATE VIEW v_adult_ages AS
SELECT name,age
FROM users
WHERE age>=18;

SELECT * FROM v_adult_ages

DROP VIEW v_adult_ages;