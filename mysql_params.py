import pyodbc
from utils import named_params
import sqlparams

PLAYER_DATA_DICT = {
    'player_name': 'Gautam Gambhir',
    'dob': '1981-14-08',
    'batting_style': 'Left',
    'bowling_style': 'LegBreak'
}

NAMED_INSERT_QUERY = f"""
INSERT INTO Player
VALUES (:player_name, :dob, :batting_style, :bowling_style)
"""

params = sqlparams.SQLParams('named', 'qmark')


def insert_player_with_out_decorator(conn, query, **query_params):
    cur = conn.cursor()
    query, query_params = params.format(query, query_params)
    print(query)  # qmark style query
    print(query_params)  # list of information
    cur.execute(query, *query_params)
    cur.execute('SELECT * FROM Player')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.execute('DELETE FROM Player')
    cur.commit()
    cur.close()


@named_params
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
    insert_player(
        conn, NAMED_INSERT_QUERY, **PLAYER_DATA_DICT)
    conn.close()


if __name__ == '__main__':
    main()
