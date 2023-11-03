SELECT COUNT(DISTINCT Paper.ID)
FROM Paper
JOIN Authors ON Paper.ID = Authors.ID
WHERE Authors.FNAME = 'Indranath' AND Authors.LNAME = 'Sengupta'
AND Paper.ID IN (
    SELECT Authors.ID
    FROM Authors
    GROUP BY Authors.ID
    HAVING COUNT(DISTINCT FNAME || ' ' || LNAME) < 3
);
