import psycopg2
import yaml
import pandas as pd
from sqlalchemy import create_engine


class RDSDatabaseConnector:
    """
    A class for connecting to an Amazon RDS PostgreSQL database, extracting and saving data.

    Attributes:
        credentials_file (str): Path to the YAML file containing RDS credentials.
        credentials (dict): Dictionary containing RDS connection credentials.
        connection: psycopg2 connection object.
        cursor: psycopg2 cursor object.
        engine: SQLAlchemy engine object.

    Methods:
        load_credentials(): Load RDS credentials from a YAML file.
        connect(): Establish a connection to the RDS database.
        disconnect(): Disconnect from the RDS database.
        initialize_engine(): Initialize the SQLAlchemy engine for the RDS connection.
        extract_data_to_dataframe(table_name="loan_payments"): Extract data from a specified table and return as a Pandas DataFrame.
        save_data_to_csv(data_frame, file_path="output_data.csv", index=True): Save a Pandas DataFrame to a CSV file.
        load_data_from_csv(file_path="output_data.csv"): Load data from a CSV file into a Pandas DataFrame.
    """
    def __init__(self, credentials_file="credentials.yaml"):
        self.credentials_file = credentials_file
        self.credentials = self.load_credentials()
        self.connection = None
        self.cursor = None
        self.engine = None

    def load_credentials(self):
        """
        Load RDS credentials from a YAML file.

        Returns:
            dict: Dictionary containing RDS connection credentials.
        """
        try:
            with open(self.credentials_file, "r") as file:
                credentials = yaml.safe_load(file)
            return credentials
        except Exception as e:
            print(f"Error loading credentials: {e}")
            return None

    def connect(self):
        """
        Establish a connection to the RDS database.
        """
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
        """
        Disconnect from the RDS database.
        """
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Disconnected from the database.")

    def initialise_engine(self):
        """
        Initialise the SQLAlchemy engine for the RDS connection.
        """
        try:
            self.engine = create_engine(
                f"postgresql+psycopg2://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}"
            )
            print("Engine initialized.")
        except Exception as e:
            print(f"Error initializing engine: {e}")

    def extract_data_to_dataframe(self, table_name="table_name"):
        """
        Extract data from a specified table and return as a Pandas DataFrame.

        Args:
            table_name (str): Name of the table to extract data from.

        Returns:
            pd.DataFrame: Pandas DataFrame containing the extracted data.
        """
        try:
            query = f"SELECT * FROM {table_name};"
            data_frame = pd.read_sql_query(query, self.engine)
            print("Data extracted to Pandas DataFrame.")
            return data_frame
        except Exception as e:
            print(f"Error extracting data: {e}")
            return None

    def save_data_to_csv(self, data_frame, file_path="output_data.csv", index=True):
        """
        Save a Pandas DataFrame to a CSV file.

        Args:
            data_frame (pd.DataFrame): Pandas DataFrame to be saved.
            file_path (str): Path to the CSV file.
            index (bool): Whether to include the index in the CSV file.
        """
        try:
            data_frame.to_csv(file_path, index=index)
            print(f"Data saved to {file_path}.")
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data_from_csv(self, file_path="output_data.csv"):
        """
        Load data from a CSV file into a Pandas DataFrame.

        Args:
            file_path (str): Path to the CSV file.

        Returns:
            pd.DataFrame: Pandas DataFrame containing the loaded data.
        """
        try:
            data_frame = pd.read_csv(file_path)
            print(f"Data loaded from {file_path}.")
            return data_frame
        except Exception as e:
            print(f"Error loading data: {e}")
            return None
        