"""
module for opening database and creating pandas dataframe
"""

import sqlite3
from logger_settings import logger
import pandas as pd

class DatabaseData:
    def __init__(self, database: str, isolation_level: str = "DEFERRED", check_same_thread: bool = False):
        self.database_name = database.split("/")[-1] #database name without path piece
        self.conn = sqlite3.connect(database = database, isolation_level = isolation_level, check_same_thread = check_same_thread)
        logger.info(f"Open connection with database {self.database_name}")
        self.cur = self.conn.cursor()

    def get_pandas_dataframe(self) -> pd.DataFrame:
        """
        table getting from db an
        """

        #table_name = self.cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall() #table name get from database
        #print(table_name)

        table_data = self.cur.execute("SELECT * FROM sources;").fetchall()
        table_attributes = self.cur.execute("PRAGMA table_info(sources);").fetchall()
        table_attributes = [attribute[1] for attribute in table_attributes]

        data_dataframe = pd.DataFrame(table_data, columns = table_attributes)
        return data_dataframe


    def close_connection(self):
        """
        Closing database connection
        """

        self.cur.close()
        self.conn.close()
        logger.info(f"Connection with database {self.database_name} was closed")







if __name__ == "__main__":
    db = DatabaseData("./testDB.db")
    print(db)
    db.get_pandas_dataframe()
    db.close_connection()