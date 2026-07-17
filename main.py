from db import get_connection
import login

connection = get_connection()


if connection:
    print("System Ready")
else:
    print("Connection Failed")
