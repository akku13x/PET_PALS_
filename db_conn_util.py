import pyodbc

def connect_db():
    try:
        connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-OFHDUG6;'
                      'Database=PetPals;'
                      'Trusted_Connection=yes;')

        return connection
    except pyodbc.Error as e:
        print(f"Database connection error: {e}")
        return None
    
def setup_database():
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            # Create pets table
            cursor.execute('''
                IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='pets' AND xtype='U')
                CREATE TABLE pets (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    name NVARCHAR(100) NOT NULL,
                    age INT NOT NULL,
                    breed NVARCHAR(100) NOT NULL
                )
            ''')
            # Create donations table
            cursor.execute('''
                IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='donations' AND xtype='U')
                CREATE TABLE donations (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    donor_name NVARCHAR(100) NOT NULL,
                    amount FLOAT NOT NULL
                )
            ''')
            connection.commit()
            print("Database setup completed.")
        except pyodbc.Error as e:
            print(f"Error setting up database: {e}")
        finally:
            connection.close()