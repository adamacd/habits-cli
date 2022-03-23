CREATE TABLE IF NOT EXISTS habitsTable (
       periodicity TEXT NOT NULL,
       description TEXT NOT NULL,
       created TEXT NOT NULL,
       completed TEXT,
       streak INTEGER,
       active TEXT
);

select * from habitsTable