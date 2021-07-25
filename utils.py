
import sqlparams
from functools import wraps

params = sqlparams.SQLParams('named', 'qmark')


def named_params(func):
    @wraps(func)
    def wrapper(conn, query: str, **query_params):
        query, query_params = params.format(query, query_params)
        return func(conn, query, *query_params)
    return wrapper
