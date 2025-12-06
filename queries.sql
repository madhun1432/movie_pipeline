SELECT title, AVG(rating) FROM ratings JOIN movies USING(movieId) GROUP BY movieId ORDER BY AVG(rating) DESC LIMIT 1;
