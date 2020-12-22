import sqlite3
from sqlite3 import Error

#Working with DataBase
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


#Create command, that will work with DB
def selectHosts():
    return f"SELECT * from hosts"
def selectField(field):
    return f"SELECT {field} FROM hosts"
def selectFieldId(field, numberId):
    return f"SELECT {field} FROM hosts WHERE id = {numberId}"
def deleteRecord(numberId):
    return f"DELETE FROM hosts WHERE id = {numberId}"
def addHost(newHost, newLogin , newPassword, newName):
    return f"""
            INSERT INTO
                hosts (host, login, password, Name)
            VALUES
                ('{newHost}','{newLogin}','{newPassword}','{newName}');
            """
def updateField(columnsName, text, numberId):
    return f"""
            UPDATE
                hosts
            SET
                {columnsName[columnNumber]} = {text}
            WHERE
                id = {numberId}
            """

# create_hosts_table = """
# CREATE TABLE IF NOT EXISTS hosts (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   host TEXT,
#   login TEXT,
#   password TEXT
# );
# """



# updateField = """
# UPDATE
#   hosts
# SET
#   {field} = {fieldValue}
# WHERE
#   id = {numberId}
# """
# execute_query(connect, create_hosts_table)



# createHost = """
# INSERT INTO
#     hosts (host, login, password)
# VALUES
#     ('10.203.68.167','root','dom'),
#     ('10.203.68.167','roo1t','domof');
# """

# execute_query(connect, create_hosts_table)
# execute_query(connect, createHost)
# execute_query(connect, deleteRecord)
# hosts = execute_read_query(connect, selectHosts)
#
# for host in hosts:
#     print(host)

