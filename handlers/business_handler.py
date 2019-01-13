import datetime

from repositories.kiosk_repository import KioskRepository

from config import config

from helpers.logger import appLogger

class BusinessHandler(object):

    @staticmethod
    def add_kiosk(id, args):
        kioskRepository = KioskRepository()
        
        name = args['name']

        kiosk_id = kioskRepository.create_kiosk(id, name)

        return {
            'kiosk': {
                'id': kiosk_id,
            },
        }

    