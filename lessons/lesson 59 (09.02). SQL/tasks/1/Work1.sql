SELECT * from titanic;

SELECT Name from titanic WHERE Age>30;

SELECT Name from titanic WHERE Sex = 'female';

SELECT Name,Age from titanic WHERE Survived = 1 ORDER BY Name ;

SELECT Name from titanic WHERE SibSp = 0 AND Parch=0;

SELECT Name,Pclass from titanic WHERE Fare>100;

SELECT Name,Pclass,Age from titanic WHERE Pclass != 1 AND Age > 18;

SELECT * from titanic WHERE Survived =0 AND Parch=0;

SELECT Name,Pclass,Fare from titanic WHERE Fare<10 AND Pclass!=3;


