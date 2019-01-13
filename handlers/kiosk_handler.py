import datetime

from repositories.kiosk_repository import KioskRepository

from config import config

from helpers.logger import appLogger

class KioskHandler(object):

    @staticmethod
    def process_kiosk_heartbeat(name):
        kioskRepository = KioskRepository()
        
        kiosk = kioskRepository.get_kiosk_by_name(name)

        if kiosk is None:
            return False

        last_seen_date = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

        kioskRepository.update_kiosk_by_name(name, {
            "last_seen_date": last_seen_date,
        })

        appLogger.info('Kiosk heartbeat. name=%s, last_seen_date=%s' % (name, last_seen_date))

        return True

    @staticmethod
    def process_kiosks_monitor():
        kioskRepository = KioskRepository()
        
        kiosks = kioskRepository.get_kiosks()

        for kiosk in kiosks:
            if not kiosk.is_healthy():
                appLogger.info('Kiosk unhealthy. name=%s, last_seen_date=%s' % (kiosk.name, kiosk.last_seen_date))

        return True

    @staticmethod
    def get_kiosks():
        response = {
            'kiosks': []
        }
        
        kioskRepository = KioskRepository()
        
        kiosks = kioskRepository.get_kiosks()

        for kiosk in kiosks:
            kioskJSON = kiosk.to_json()
            kioskJSON['is_healthy'] = kiosk.is_healthy()

            response['kiosks'].append(kioskJSON)

        return response