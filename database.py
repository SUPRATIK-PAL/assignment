import mysql.connector

class Database:
    """Connects to and interacts with the database."""

    def __init__(self, host, user, password, database):
        self.connection = self._connect(host, user, password, database)

    def _connect(self, host, user, password, database):
        """Establishes a connection to the database."""
        try:
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            return connection
        except mysql.connector.Error as err:
            print("Error connecting to database:", err)
            return None

    def close(self):
        """Closes the connection to the database."""
        if self.connection:
            self.connection.close()

    def execute_query(self, query, params=None):
        """Executes a query on the database."""
        cursor = self.connection.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
        except mysql.connector.Error as err:
            print("Error executing query:", err)
        finally:
            cursor.close()
