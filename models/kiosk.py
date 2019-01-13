import datetime

from config import config

class Kiosk(object):

    def __init__(self, id = 0):
        self.id = id
        self.business_id = 0
        self.name = ''
        self.last_seen_date = None

    def init_from_db(self, dbRet):
        self.id = dbRet['id']
        self.business_id = dbRet['business_id']
        self.name = dbRet['name']
        self.last_seen_date = dbRet['last_seen_date']

    def to_json(self):
        return {
            "id": self.id,
            "business_id": self.business_id,
            "name": self.name,
            "last_seen_date": self.last_seen_date,
        }

    def is_healthy(self):
        return (datetime.datetime.utcnow() - self.last_seen_date).total_seconds() <= config.KIOSK_HEALTH_CHECK_GRACE_PERIOD
