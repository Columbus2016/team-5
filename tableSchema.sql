
drop table Comments;
drop table ForumMessages;
drop table Connections;
drop table User;


create table User
(userID int,
password varchar(30),
firstname varchar(30), 
lastname varchar(30), 
email varchar(30),
location varchar(30),
age varchar(3),
diagnosis varchar(50),
community varchar(30),
bio varchar (100),
gender varchar(10)
);


ALTER TABLE User
ADD PRIMARY KEY (userID);

ALTER TABLE User AUTO_INCREMENT=1;


ALTER TABLE User MODIFY COLUMN userID INT auto_increment;

INSERT INTO User values (1,'pass', 'Lisa', 'Truong', 'abc@yahoo.com', 41844, 22, 'IDC', 'survivor', 'hey, I am Lisa', 'Female');
INSERT INTO User values (2, 'pass', 'Sona', 'Jeswani', 'abcd@yahoo.com', 95746, 19, 'none', 'co-survivor', 'hey, I am Sona', 'Female');

create table Connections
(userID1 int,
userID2 int
);

ALTER TABLE Connections
ADD FOREIGN KEY (userID1) REFERENCES User(userID);

ALTER TABLE Connections
ADD FOREIGN KEY (userID2) REFERENCES User(userID);

create table ForumMessages
(fMessageText varchar(255),
 fMessageID int,
 userID int,
 date DateTime);

ALTER TABLE ForumMessages
ADD FOREIGN KEY (userID) REFERENCES User(userID);

ALTER TABLE ForumMessages
ADD PRIMARY KEY (fMessageID);

create table Comments 
(userID int,
commentText VARCHAR(255),
fMessageID int);

ALTER TABLE Comments
ADD FOREIGN KEY (userID) REFERENCES User(userID);

ALTER TABLE Comments
ADD FOREIGN KEY (fMessageID) REFERENCES ForumMessages(fMessageID);


