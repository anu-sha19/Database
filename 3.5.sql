SELECT COUNT(DISTINCT Citations.ID)
FROM Authors
JOIN Citations ON Authors.ID = Citations.CITE_ID
WHERE Authors.LNAME = 'Yin' AND Authors.FNAME = 'Lei';
