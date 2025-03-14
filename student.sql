-- Create the table STUDENT if it doesn't exist
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);

-- Insert records into the STUDENT table
INSERT INTO STUDENT VALUES ('Krish', 'Data Science', 'A', 90);
INSERT INTO STUDENT VALUES ('John', 'Data Science', 'B', 100);
INSERT INTO STUDENT VALUES ('Mukesh', 'Data Science', 'A', 86);
INSERT INTO STUDENT VALUES ('Jacob', 'DEVOPS', 'A', 50);
INSERT INTO STUDENT VALUES ('Dipesh', 'DEVOPS', 'A', 35);

-- Select and display all records from the STUDENT table
SELECT * FROM STUDENT;