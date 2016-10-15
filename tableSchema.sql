create table User
(userID int,  
firstname varchar(30), 
lastname varchar(30), 
email varchar(30),
location int,
age int,
optin bool,
photoID BLOB,
bio varchar (100)
);
drop table dbo.User

ALTER TABLE dbo.User
ADD PRIMARY KEY (userID)

alter table dbo.User add column userID

INSERT INTO User values (123, 'Lisa', 'Truong', 'abc@yahoo.com', 41844, 22, True, 11, 'hey, I am Lisa');
INSERT INTO User values (124, 'Sona', 'Jeswani', 'abcd@yahoo.com', 95746, 19, False, 10, 'hey, I am Sona');

create table dbo.Connections
(foreign key(userID1) REFERENCES USER(userID),
foreign key(userID2) REFERENCES USER(userID)
);

create table ForumMessages
(fMessageText varchar(255),
primary key(fMessageID),
foreign key(user_ID) REFERENCES USER(user_ID),
`date` DateTime);

create table Comments 
(foreign key(userID1) REFERENCES USER(userID),
foreign key(fMessageText) REFERENCES USER(user_ID));

create table DirectMessages
(dMessageText varchar(255),
foreign key(toID) REFERENCES USER(userID),
foreign key(fromID) REFERENCES USER(userID),
`date` DateTime);

select * from User
