
import pyodbc

PLAYER_DATA_TUPLE = ('Gautam Gambhir', '1981-14-08', 'Left', 'LegBreak')

QMARK_INSERT_QUERY = f"""
INSERT INTO Player
VALUES (?, ?, ?, ?)
"""


def insert_player(conn, query, *query_params):
    cur = conn.cursor()
    cur.execute(query, *query_params)
    cur.execute('SELECT * FROM Player')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.execute('DELETE FROM Player')
    cur.commit()
    cur.close()


def main():
    connection_string = "Driver=SQLITE3;Database=fantasy.db"
    conn = pyodbc.connect(connection_string)
    insert_player(conn, QMARK_INSERT_QUERY, *PLAYER_DATA_TUPLE)
    conn.close()


if __name__ == '__main__':
    main()
