import psycopg2
import yaml
import pandas as pd
from sqlalchemy import create_engine

class RDSDatabaseConnector:
    def __init__(self, credentials_file="credentials.yaml"):
        self.credentials_file = credentials_file
        self.credentials = self.load_credentials()
        self.connection = None
        self.cursor = None
        self.engine = None

    def load_credentials(self):
        try:
            with open(self.credentials_file, "r") as file:
                credentials = yaml.safe_load(file)
            return credentials
        except Exception as e:
            print(f"Error loading credentials: {e}")
            return None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.credentials['RDS_HOST'],
                user=self.credentials['RDS_USER'],
                password=self.credentials['RDS_PASSWORD'],
                database=self.credentials['RDS_DATABASE'],
                port=self.credentials['RDS_PORT']
            )
            self.cursor = self.connection.cursor()
            print("Connected to the database.")
        except Exception as e:
            print(f"Error connecting to the database: {e}")

    def disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Disconnected from the database.")

    def initialize_engine(self):
        try:
            self.engine = create_engine(
                f"postgresql+psycopg2://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}"
            )
            print("Engine initialized.")
        except Exception as e:
            print(f"Error initializing engine: {e}")

    def extract_data_to_dataframe(self, table_name="loan_payments"):
        try:
            query = f"SELECT * FROM {table_name};"
            data_frame = pd.read_sql_query(query, self.engine)
            print("Data extracted to Pandas DataFrame.")
            return data_frame
        except Exception as e:
            print(f"Error extracting data: {e}")
            return None

    def save_data_to_csv(self, data_frame, file_path="output_data.csv", index=True):
        try:
            data_frame.to_csv(file_path, index=index)
            print(f"Data saved to {file_path}.")
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data_from_csv(self, file_path="output_data.csv"):
        try:
            data_frame = pd.read_csv(file_path)
            print(f"Data loaded from {file_path}.")
            return data_frame
        except Exception as e:
            print(f"Error loading data: {e}")
            return None
        