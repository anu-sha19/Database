SELECT Title, LastUpdate
FROM Paper 
JOIN Authors ON Paper.ID = Authors.ID 
WHERE Authors.LNAME = 'Eto' AND Authors.FNAME = 'Minoru' 
ORDER BY LastUpdate DESC;