create table User
(userID int,
firstname varchar(30), 
lastname varchar(30), 
email varchar(30),
location int,
age int,
optin bool,
bio varchar (100)
);

ALTER TABLE User
ADD PRIMARY KEY (userID);

INSERT INTO User values (123, 'Lisa', 'Truong', 'abc@yahoo.com', 41844, 22, True, 11, 'hey, I am Lisa');
INSERT INTO User values (124, 'Sona', 'Jeswani', 'abcd@yahoo.com', 95746, 19, False, 10, 'hey, I am Sona');

create table Connections
(userID1 int,
userID2 int
);

ALTER TABLE Connections
ADD FOREIGN KEY (userID1) REFERENCES USER(userID);

ALTER TABLE Connections
ADD FOREIGN KEY (userID2) REFERENCES USER(userID);

create table ForumMessages
(fMessageText varchar(255),
 fMessageID int,
 userID int,
 date DateTime);

ALTER TABLE ForumMessages
ADD FOREIGN KEY (userID) REFERENCES USER(userID);

ALTER TABLE ForumMessages
ADD PRIMARY KEY (fMessageID);

create table Comments 
(userID int,
commentText VARCHAR(255),
fMessageID int);

ALTER TABLE Comments
ADD FOREIGN KEY (userID) REFERENCES USER(userID);

ALTER TABLE Comments
ADD FOREIGN KEY (fMessageID) REFERENCES ForumMessages(fMessageID);
