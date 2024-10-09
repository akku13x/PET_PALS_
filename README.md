PetPals is a software system designed to facilitate the adoption of pets from shelters and rescue organizations. This platform enables potential adopters to browse available pets, shelters to list adoptable pets, and donors to contribute to animal welfare efforts.

**Features**:
        
        1.Pet Management:
          -List available pets for adoption, including details like name, age, and breed.
          -Add or remove pets from the list of available pets.
          
        2.Donation System:
          -Handle both cash and item donations.
          -Record donation details and provide options for donors to contribute.
          
        3.Adoption Event Management:
          -Manage adoption events, including registration of participants (shelters and adopters).
          -List and retrieve upcoming events from the database.
          
        4.Database Connectivity:
          -Retrieve, update, and manage data for pets, donations, and events using SQL.
          
        5.Exception Handling:
          -Handle invalid inputs, null references, insufficient funds, file handling errors, and custom exceptions.


**Project Structure**

The project follows an organized directory structure:

          -entity/model: Contains entity classes representing real-world objects like Pet, Dog, Cat.
          -dao: Contains service interfaces and their implementations for database interaction.
          -exception: Defines custom exceptions to handle various error conditions.
          -util: Contains utility classes for database connection and configuration.
          -main: Contains the main application module with a menu-driven approach to showcase all functionalities.
  
**Classes Overview**

**Pet Class:**

        Attributes: Name, Age, Breed
        Methods: Constructor, Getters, Setters, toString()

**Dog and Cat Classes (Inherit from Pet):**
        
        Attributes: DogBreed (Dog), CatColor (Cat)
        Methods: Constructor, Getters, Setters

**PetShelter Class:**

        Manage a list of available pets for adoption.
        
**Donation System:**

        CashDonation and ItemDonation (derived from an abstract Donation class) handle cash and item donations, respectively.
        
**Adoption Event:**

        Manage and host adoption events, including participant registration.
        
**Database Connectivity:**

        The application interacts with a database to store and retrieve data for pets, donations, and events.
        SQL scripts generate tables based on entity classes (Pet, User, etc.).
        
**Requirements:**

        Python
        SQL Database (MSSQL)

**Setup Instructions:**

        1.Import the project into your IDE.
        2.Configure the database connection in the DBPropertyUtil class.
        3.Run the SQL schema scripts to create the necessary tables in your database.
        4.Run the MainModule class to start the application.
        
**Exception Handling**
The application implements robust exception handling for:

        1.Invalid pet age input
        2.Null reference handling for pet properties
        3.Insufficient donation amounts
        4.File handling errors for missing data
        5.Custom exceptions for adoption-related errors

**Ouput:**
        ![image](https://github.com/user-attachments/assets/fce9f108-ddfb-43d5-82c6-468d7ebdba4f)

**Pets table**:

1.Adding A PET


Before:

![image](https://github.com/user-attachments/assets/d8f91960-a690-4875-aae1-1a7fa97b863c)

After:

![image](https://github.com/user-attachments/assets/976b003a-5a80-4634-a437-be8c844c21a4)


![image](https://github.com/user-attachments/assets/e52f1930-8160-45fb-9c71-ca8da27e39ca)


**2. REMOVE A PET**:

Before:

![image](https://github.com/user-attachments/assets/e52f1930-8160-45fb-9c71-ca8da27e39ca)

After:

![image](https://github.com/user-attachments/assets/577c5e0a-fb58-49db-ac6e-196eea49f581)

![WhatsApp Image 2024-10-08 at 14 43 14_441830dd](https://github.com/user-attachments/assets/1ca26d1a-ed21-47b7-8ead-1979f42c497a)


Simialarly Implement the program for outputs 
