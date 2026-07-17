import mysql.connector


def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="JSRjsr297",
            database="insurance_db"
        )

        if conn.is_connected():
            print("Database Connected Successfully")

        return conn

    except mysql.connector.Error as e:
        print("Database Error:", e)
        return None
