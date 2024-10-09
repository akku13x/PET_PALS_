Create database PetPlas;

use PetPals;



CREATE TABLE pets (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100),
    age INT,
    breed NVARCHAR(100)
);

-- Creating donations table
CREATE TABLE donations (
    id INT IDENTITY(1,1) PRIMARY KEY,
    donor_name NVARCHAR(100),
    amount DECIMAL(10, 2),
);

select * from pets;

select * from donations;
