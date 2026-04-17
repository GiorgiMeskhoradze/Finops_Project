import os
import psycopg2
from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT', '5432'),
    database=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
)

def get_connection():
    return connection_pool.getconn()

def release_connection(conn):
    connection_pool.putconn(conn)

def execute_query(query, params=None):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        rows = cursor.fetchall()
        cursor.close()
        return rows
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        release_connection(conn)