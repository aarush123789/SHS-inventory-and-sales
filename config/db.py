from mysql import connector
import os

class SQLHandler:
    """Handles MySQL connection to the database."""

    def __init__(self):
        self.db_name = 'shs_inventoryDB'  # Updated to match the database name from your SQL

      
        try:
            self.connection = connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password='',
                database=self.db_name
            )

            if self.connection.is_connected():
                print(f"Connected to MySQL and database `{self.db_name}`.")

        except connector.Error as err:
            # If the database doesn't exist, create it
            if err.errno == connector.errorcode.ER_BAD_DB_ERROR:
                print(f"Database `{self.db_name}` not found. Creating it...")
                self._create_database()
                # Try connecting again now that it's created
                self.connection = connector.connect(
                    host='localhost',
                    port='3306',
                    user='root',
                    password='',
                    database=self.db_name
                )
            else:
                print("Database connection error:", err)
                raise

    def _create_database(self):
        """Create database and tables by running a .sql file."""
        try:
            # Connect to MySQL server (no DB selected)
            temp_connection = connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password=''
            )
            cursor = temp_connection.cursor()

            # Create the database if it doesn't exist
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.db_name}")

            # Select the newly created or existing database
            cursor.execute(f"USE {self.db_name}")

            # Read SQL from file
            sql_path = os.path.join(os.path.dirname(__file__), 'database.sql')
            with open(sql_path, 'r') as file:
                sql_commands = file.read()

            # Split by semicolon to handle multiple queries
            for command in sql_commands.split(';'):
                command = command.strip()
                if command:
                    cursor.execute(command)

            temp_connection.commit()
            cursor.close()
            temp_connection.close()
            print(f"Database `{self.db_name}` created successfully.")

        except Exception as e:
            print("Failed to create database:", e)
            raise

def get_connection():
    """Return an active MySQL connection."""
    handler = SQLHandler()
    return handler.connection
