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
        user_name = item[0]
        return user_name
    # commit commands
    conn.commit()

# search the database for city and get weather 
def search_database(user):
    cur.execute("SELECT * FROM users WHERE user_name = (?)", (user,))
    items = cur.fetchall()
    for item in items:
        the_city = item[1]
        my_weather = get_weather(the_city)
        return my_weather

    conn.commit()

    
    

users_table()