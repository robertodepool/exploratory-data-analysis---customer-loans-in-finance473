import psycopg2
import yaml

class RDSDatabaseConnector:
    def __init__(self, credentials_file="credentials.yaml"):
        self.credentials_file = credentials_file
        self.credentials = self.load_credentials()
        self.connection = None
        self.cursor = None

    def load_credentials(self):
        try:
            with open(self.credentials_file, "r") as file:
                credentials = yaml.safe_load(file)
            return credentials
        except Exception as e:
            print(f"Error loading credentials: {e}")
            return None