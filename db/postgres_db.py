import psycopg2
import psycopg2.extras

from config import config

class Postgres(object):

    def query(self, query, single = True,insert = False, argsDict = None):

        try:
            db_config = {
                'dbname': config.POSTGRES_DB_NAME,
                'host': config.POSTGRES_DB_HOST,
                'password': config.POSTGRES_DB_PASS,
                'port': config.POSTGRES_DB_PORT,
                'user': config.POSTGRES_DB_USER
            }

            connection = psycopg2.connect(**db_config)

            cursor = connection.cursor(cursor_factory = psycopg2.extras.DictCursor)

            if not insert :
                if argsDict is not None :
                    fields = ', '.join(argsDict.keys())
                    values = ', '.join(['%%(%s)s' % x for x in argsDict])
                    query = query % (fields, values)
                    cursor.execute(query, argsDict)
                else :
                    cursor.execute(query)
                if single :
                    return cursor.fetchone()
                else :
                    return cursor.fetchall()
            else:
                if argsDict is not None:
                    fields = ', '.join(argsDict.keys())
                    values = ', '.join(['%%(%s)s' % x for x in argsDict])
                    query = query % (fields, values)

                    cursor.execute(query, argsDict)
                    connection.commit()
                else:
                    cursor.execute(query, argsDict)
                    connection.commit()
                return cursor.fetchone()
        except Exception as error:
            connection.commit()
            return None
        finally:
            connection.close()
            cursor.close()