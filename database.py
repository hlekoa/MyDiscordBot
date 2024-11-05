import sqlite3

from weather import get_weather


# connect to database and create cursor
conn = sqlite3.connect('users.db')
cur = conn.cursor()

# Create a table
def users_table():
    # create a table and check if it exists
    cur.execute("CREATE TABLE IF NOT EXISTS users (user_name text, city text)")
    # commit command
    conn.commit()

    return "Your table has been created!"


# Add records to the table
def add_record(user, city):
    # insert values to the table
    cur.execute("INSERT INTO users VALUES (?,?)", (user, city))
    # commit commands
    conn.commit()

    return "User info added to the database!"


# Search by user
def search_by_user(user):
    cur.execute("SELECT * FROM users WHERE user_name = (?)", (user,))
    items = cur.fetchall()
    for item in items:
        the_city = item[1]
        get_weather(the_city)
    # commit commands
    conn.commit()

    return "Please wait while I fetch your weather........"


# search the database 
def search_database(user):
    cur.execute("SELECT * FROM users WHERE user_name = (?)", (user,))
    items = cur.fetchall()
    for item in items:
        my_user = item[0]
        return my_user
    
    conn.commit()
    

users_table()