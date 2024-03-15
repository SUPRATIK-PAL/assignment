from database import Database

class Users:
    """Represents user-related operations."""

    def __init__(self, db):
        self.db = db

    def create_table(self):
        """Creates the 'users' table if it doesn't exist."""
        query = """
            CREATE TABLE IF NOT EXISTS users (
                id INT PRIMARY KEY,
                first_name VARCHAR(255),
                last_name VARCHAR(255),
                email VARCHAR(255)
            )
        """
        self.db.execute_query(query)

    def fetch_users(self):
        """Fetches user data from the Dummy API and stores it in the database."""
        url = "https://dummyapi.io/data/v1/user?limit=10"  # Fetch 10 users at a time
        headers = {"app-id": YOUR_APP_ID}  # Replace with your App ID

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = json.loads(response.text)
            users = data["data"]

            for user in users:
                user_id = user["id"]
                first_name = user["firstName"]
                last_name = user["lastName"]
                email = user["email"]

                # Insert user data into the table
                query = "INSERT INTO users (id, first_name, last_name, email) VALUES (%s, %s, %s, %s)"
                self.db.execute_query(query, (user_id, first_name, last_name, email))
        else:
            print("Error fetching user data:", response.status_code)
