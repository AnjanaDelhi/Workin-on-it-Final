-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/TROvsM
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "IMDb Movies" (
    "imdb_title_id" varchar(100)   NOT NULL,
    "original_title" varchar(100)   NOT NULL,
    "year" int   NOT NULL,
    "genre" varchar(25)   NOT NULL,
    "duration" int   NOT NULL,
    "country" varchar(25)   NOT NULL,
    "language" varchar(25)   NOT NULL,
    "director" varchar(50)   NOT NULL,
    "writer" varchar(50)   NOT NULL,
    "production_company" varchar(50)   NOT NULL,
    "actors" varchar(250)   NOT NULL,
    "description" varchar(1000)   NOT NULL,
    "avg_vote" decimal[(3[,1])]   NOT NULL,
    "votes" int   NOT NULL,
    "budget" varchar(25)   NOT NULL,
    "usa_gross_income" varchar(25)   NOT NULL,
    "worlwide_gross_income" varchar(25)   NOT NULL,
    "metascore" int   NOT NULL,
    "reviews_from_users" int   NOT NULL,
    "reviews_from_critics" varchar(25)   NOT NULL
);

CREATE TABLE "movies_complete" (
    "imdb_title_id" varchar(100)   NOT NULL,
    "original_title" varchar(100)   NOT NULL,
    "year" int   NOT NULL,
    "genre" varchar(25)   NOT NULL,
    "duration" int   NOT NULL,
    "country" varchar(25)   NOT NULL,
    "language" varchar(25)   NOT NULL,
    "director" varchar(50)   NOT NULL,
    "writer" varchar(50)   NOT NULL,
    "production_company" varchar(50)   NOT NULL,
    "actors" varchar(250)   NOT NULL,
    "description" varchar(1000)   NOT NULL,
    "avg_vote" decimal[(3[,1])]   NOT NULL,
    "votes" int   NOT NULL,
    "budget" varchar(25)   NOT NULL,
    "usa_gross_income" varchar(25)   NOT NULL,
    "worlwide_gross_income" varchar(25)   NOT NULL,
    "metascore" int   NOT NULL,
    "reviews_from_users" int   NOT NULL,
    "reviews_from_critics" varchar(25)   NOT NULL
);

CREATE TABLE "movies_complete_adjusted" (
    "imdb_title_id" varchar(100)   NOT NULL,
    "original_title" varchar(100)   NOT NULL,
    "year" int   NOT NULL,
    "genre" varchar(25)   NOT NULL,
    "duration" int   NOT NULL,
    "country" varchar(25)   NOT NULL,
    "language" varchar(25)   NOT NULL,
    "director" varchar(50)   NOT NULL,
    "writer" varchar(50)   NOT NULL,
    "production_company" varchar(50)   NOT NULL,
    "actors" varchar(250)   NOT NULL,
    "description" varchar(1000)   NOT NULL,
    "avg_vote" decimal[(3[,1])]   NOT NULL,
    "votes" int   NOT NULL,
    "budget" varchar(25)   NOT NULL,
    "usa_gross_income" varchar(25)   NOT NULL,
    "worlwide_gross_income" varchar(25)   NOT NULL,
    "metascore" int   NOT NULL,
    "reviews_from_users" int   NOT NULL,
    "reviews_from_critics" varchar(25)   NOT NULL,
    "Normalize" decimal[10(,9)]   NOT NULL
);

CREATE TABLE "Actors" (
    "actors" varchar(250)   NOT NULL,
    "worldwide_gross_income" varchar(25)   NOT NULL
);

CREATE TABLE "CPI" (
    "YEAR" int   NOT NULL,
    "JAN" decimal[6(,3)]   NOT NULL,
    "FEB" decimal[6(,3)]   NOT NULL,
    "MAR" decimal[6(,3)]   NOT NULL,
    "APR" decimal[6(,3)]   NOT NULL,
    "MAY" decimal[6(,3)]   NOT NULL,
    "JUN" decimal[6(,3)]   NOT NULL,
    "JUL" decimal[6(,3)]   NOT NULL,
    "AUG" decimal[6(,3)]   NOT NULL,
    "SEP" decimal[6(,3)]   NOT NULL,
    "OCT" decimal[6(,3)]   NOT NULL,
    "NOV" decimal[6(,3)]   NOT NULL,
    "DEC" decimal[6(,3)]   NOT NULL,
    "AVE" decimal[6(,3)]   NOT NULL
);

