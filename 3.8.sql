SELECT Paper.Title
FROM Paper
JOIN Authors ON Paper.ID = Authors.ID
GROUP BY Paper.ID, Paper.Title
HAVING COUNT(Authors.ID) = 1;
