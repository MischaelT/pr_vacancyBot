from backend.data.db.base_db import Base_db

import psycopg2

from settings.config import (POSTGRES_DB, POSTGRES_HOST, POSTGRES_PASSWORD,
                             POSTGRES_PORT, POSTGRES_USER)


class Postgres_db(Base_db):

    """
        Class provides access to postgres database
    """    

    def __init__(self) -> None:

        super().__init__()

        self.__create_table_users()
        self.__create_table_vacancies()

    def get_data(self, request_text:str, params:tuple) -> list:

        """
            Method returns data from database

        Returns:
            list(tuple): requested data
        """        
      
        return self._read(request_text, params)

    def push_data(self, query:str, params: tuple) -> None:

        """
            Method pushes data to database
        """        
        
        self._write(query, params)

    def __create_table_users(self) -> None:

        """
            Method create table users.
            Raise Exception if table already exists
        """        

        connection = self._make_connection()

        try:

            cursor = connection.cursor()

            create_users_query = '''CREATE TABLE users
                                (
                                ID              INT       PRIMARY KEY       NOT NULL,
                                IS_REGISTERED   BOOLEAN                     NOT NULL,                                
                                EXP             TEXT                        NOT NULL,
                                LANG            TEXT                        NOT NULL,
                                CITY            TEXT                        NOT NULL,
                                SALARY          TEXT                        NOT NULL
                                ); '''

            cursor.execute(create_users_query)

            connection.commit()
            print('успешно')

        except (Exception) as exception:
            print('не успешно', exception)
            
        finally:
            if connection:
                cursor.close()
                connection.close()

    def __create_table_vacancies(self)-> None:

        """
            Method create table vacancies.
            Raise Exception if table already exists
        """       

        connection = self._make_connection()

        try:

            cursor = connection.cursor()

            create_vacancies_query = '''CREATE TABLE vacancies
                                (
                                ID             SMALLSERIAL                  NOT NULL,
                                DATE           DATE                         NOT NULL,
                                EXP            TEXT                         NOT NULL,
                                LANG           TEXT                         NOT NULL,
                                CITY           TEXT                         NOT NULL,
                                TITLE          TEXT                         NOT NULL,
                                INFO           TEXT                         NOT NULL,
                                LINK           TEXT                         NOT NULL,
                                SALARY         SMALLINT                     NOT NULL
                                ); '''

            cursor.execute(create_vacancies_query)

            connection.commit()

            print('успешно')

        except (Exception) as exception:
            print('не успешно', exception)
            
        finally:
            if connection:
                cursor.close()
                connection.close()     

    def _make_connection(self):

        """
            Method connecting to database using autentication data from config.py

        Returns:
           connection: Connection object
        """

        try:
            connection = psycopg2.connect(
                                        user=POSTGRES_USER,
                                        password=POSTGRES_PASSWORD,
                                        host=POSTGRES_HOST,
                                        port=POSTGRES_PORT,
                                        database=POSTGRES_DB
                                        )

        except (Exception) as ex:
            print(ex)

        return connection

    def _write(self, query:str, params: tuple) -> None:

        """
        Method writes data to database.

        Args:
            query (str): SQL query
            params (tuple): parameters for inserting to query
        """  

        connection = self._make_connection()

        try:

            cursor = connection.cursor()
            cursor.execute(query, params)
            connection.commit()

        except Exception as ex:
            print(ex)

        finally:
            if connection:
                cursor.close()
                connection.close()

    def _read(self, query:str, params:tuple) -> list:

        """
            Method receives data from database 

        Returns:
            list: requested data
        """        

        connection = self._make_connection()

        record =[]

        try:
            cursor = connection.cursor()
            cursor.execute(query, params)
            record = cursor.fetchall()

        except Exception as ex:
            print(ex)

        finally:
            if connection:
                cursor.close()
                connection.close()

        return record
