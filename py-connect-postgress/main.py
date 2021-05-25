import os

import psycopg2
from psycopg2 import Error

from config import config


def create_tables(nickname):
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE {}(
            id SERIAL PRIMARY KEY,
            nickname VARCHAR(255) NOT NULL
        )
        """.format(nickname))
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        cur.execute(commands)

        sql = "SELECT table_name FROM information_schema.tables WHERE table_schema='public' and table_name='{}';".format(nickname.lower())
        cur.execute(sql)
        tables = cur.fetchone()[0]
        print(tables)
        with open("/usr/share/nginx/html/index.html", "w") as file:
            file.write(str(tables))
            file.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            cur.close()
            print("Соединение с PostgreSQL закрыто")


def get_tables_details():
    try:
        # Подключиться к существующей базе данных
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()
        sql = "SELECT table_name FROM information_schema.tables WHERE table_schema='public';"
        cursor.execute(sql)
        tables = cursor.fetchall()
        print(tables)
        with open("/usr/share/nginx/html/index.html", "w") as file:
            file.write(str(tables))
            file.close()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")


if __name__ == '__main__':
    if bool(os.environ.get('nickname')) is False:
        get_tables_details()
    else:
        create_tables(os.environ.get('nickname'))
