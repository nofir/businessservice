import json

from db.postgres_db import Postgres

from models.kiosk import Kiosk
from enums.kiosk_status import KioskStatus

from helpers.logger import appLogger

class KioskRepository(object):

    def __init__(self):
        self.db = Postgres()

    def update_kiosk_by_name(self, name, args):
        argsArray = []

        if 'last_seen_date' in args:
            argsArray.append("last_seen_date='" + args['last_seen_date'] + "'")

        query = "UPDATE business_kiosk SET " + ','.join(argsArray) + " WHERE name = '{0}'".format(name)

        self.db.query(query, False, True)

        return True

    def get_kiosk_by_name(self, name):
        query = "SELECT * FROM business_kiosk WHERE name = '{0}'".format(name)

        dbRet = self.db.query(query, True, False)

        if dbRet is not None:
            kiosk = Kiosk()
            kiosk.init_from_db(dbRet)
            return kiosk

        return None

    def get_kiosks(self):
        kiosks = []

        query = "SELECT * FROM business_kiosk"

        dbRet = self.db.query(query, False, False)

        for dbRetRow in dbRet:
            kiosk = Kiosk()
            kiosk.init_from_db(dbRetRow)
            kiosks.append(kiosk)

        return kiosks

    def create_kiosk(self, business_id, name):
        argsDict = {
            "business_id": business_id,
            "name": name,
        }

        dbRet = self.db.query('INSERT INTO business_kiosk (%s) VALUES (%s) RETURNING id', True, True, argsDict)

        return dbRet['id']