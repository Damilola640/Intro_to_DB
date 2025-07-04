# connect to sql databae in MySQL server
import mysql.connector
# from mysql.connector import Error

def create_database():
    try:
        # connect to the database
        connection = mysql.connector.connect(
            host = 'localhost',
            user = 'Bolajeee',
            password = '12345678'
        )
    
        if connection.is_connected:
            # convert to cursor
            cursor = connection.cursor()
            # run the connection request
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as e:
        print(f"Failed to connect to database: {e}")
    finally:
        # close the connection or cursor if open
        try:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()
        except:
            password
        
__name__ = "__main__"
create_database()
