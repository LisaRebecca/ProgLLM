CREATE TABLE Courses (
    CourseID SERIAL PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Description TEXT
);

CREATE TABLE Flashcards (
    FlashcardID SERIAL PRIMARY KEY,
    CourseID INT NOT NULL,
    Question TEXT NOT NULL,
    Answer TEXT NOT NULL,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

CREATE TABLE Users (
    UserID SERIAL PRIMARY KEY,
    Username VARCHAR(255) UNIQUE NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    PasswordHash CHAR(64) NOT NULL
);

CREATE TABLE UserProgress (
    ProgressID SERIAL PRIMARY KEY,
    UserID INT NOT NULL,
    FlashcardID INT NOT NULL,
    LastSeen TIMESTAMP NOT NULL,
    PerformanceRating INT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (FlashcardID) REFERENCES Flashcards(FlashcardID)
);
