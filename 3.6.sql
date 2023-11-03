SELECT Category, COUNT(DISTINCT ID) AS NumberOfPapers
FROM Categories
GROUP BY Category;
