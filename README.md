**Summary:**

This project builds a simple ETL pipeline that reads movie data from CSV files, enriches it using the OMDb API, and loads it into a SQLite database.

The data is cleaned by extracting the movie year and standardizing titles before API calls.

After loading, SQL queries are used to find insights like top-rated movies, best genres, directors, and yearly averages.

The pipeline is easy to run with Python and SQLite, making it beginner-friendly.

Overall, it demonstrates a complete workflow from raw data to analytical insights.

**Data files:**

• MovieLens CSV files (movies.csv, ratings.csv)

• OMDb API for enrichment

• SQLite database

• Python (pandas, requests, sqlite3)

**Tech Stack**

Component	Technology

Language	Python

Database	SQLite

Libraries	pandas, requests, sqlite3

External API	OMDb API

**Project Structure**

movie pipeline

│── etl.py

│── schema.sql

│── queries.sql

│── movies.csv

│── ratings.csv

│── movies.db

│── README.md

**How to Run the Project:**
1. Install Dependencies

pip install pandas requests

2. Download MovieLens Dataset

**Required files:**

• movies.csv

• ratings.csv

Place them in the same folder as etl.py.

3. Run the Database Schema
Creates required tables:

sqlite3 movies.db < schema.sql

4. Add OMDb API Key
Open etl.py and replace:
**API_KEY** = "YOUR_KEY"

Generate a free key from:
https://www.omdbapi.com/

5. Run the ETL Pipeline
python etl.py
You will see:
**Done**

**Design Choices**

	•	SQLite is used for simplicity.
	•	Movie titles cleaned and extracted only the name and year.
	•	API errors handled using values.
	•	ETL script is idempotent (old records are removed before by inserting new ones).
  
**SQL Queries**
1. Which movie has the highest average rating?

-> SELECT m.title, AVG(r.rating) AS avg_rating

FROM ratings r

JOIN movies m ON r.movieId = m.movieId

GROUP BY m.movieId

ORDER BY avg_rating DESC

LIMIT 1;


2. What are the top 5 movie genres that have the highest average rating?

-> SELECT m.genres, AVG(r.rating) AS avg_rating

FROM ratings r

JOIN movies m ON r.movieId = m.movieId

GROUP BY m.genres

ORDER BY avg_rating DESC

LIMIT 5;

3. Who is the director with the most movies in this dataset?

-> SELECT director, COUNT(*) AS movie_count

FROM movies

GROUP BY director

ORDER BY movie_count DESC

LIMIT 1;

4. What is the average rating of movies released each year?

-> SELECT m.year, AVG(r.rating) AS avg_rating

FROM ratings r

JOIN movies m ON r.movieId = m.movieId

GROUP BY m.year

ORDER BY m.year;

**Challenges:**

1. Installing SQLite in PowerShell
It was confusing to understand how to install and run SQLite using PowerShell commands.

2. Running schema.sql using the correct SQLite command
New learners often make mistakes like wrong path or missing file name.

3. moviesId and movieId naming mismatch
The column name must match exactly in:

•	movies.csv

•	ratings.csv

•	schema.sql

•	etl.py
If names are different (MovieID, moviesId, movieId), the ETL fails.

**Conclusion:**
This project helped me understand how raw data can be cleaned, enriched, and transformed into meaningful insights.

It gave me hands-on experience with building a real ETL pipeline from start to finish.



























