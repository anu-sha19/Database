SELECT Paper.Title
FROM Paper
LEFT JOIN Citations ON Paper.ID = Citations.ID
WHERE Citations.CITE_ID IS NULL;