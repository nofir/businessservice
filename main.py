import datetime

from flask import Flask,request,jsonify

from handlers.kiosk_handler import KioskHandler
from handlers.business_handler import BusinessHandler

from helpers.logger import appLogger

app = Flask(__name__)

@app.route('/', methods=['GET'])
def healthcheck():
    return 'Business Service is running! ' + datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")

@app.route('/businesses/kiosk/<name>/heartbeat', methods=['POST'])
def process_kiosk_heartbeat(name):
    try :
        appLogger.info('name=%s' % name)

        KioskHandler.process_kiosk_heartbeat(name)
            
        return jsonify({'status': 'ok'})
    except Exception, e :
        return jsonify({'error': e.message})

@app.route('/businesses/kiosks/monitor', methods=['POST'])
def process_kiosks_monitor():
    try :
        KioskHandler.process_kiosks_monitor()

        return jsonify({'status': 'ok'})
    except Exception, e :
        return jsonify({'error': e.message})

@app.route('/businesses/kiosks', methods=['GET'])
def get_kiosks():
    try :
        data = KioskHandler.get_kiosks()

        return jsonify(data)
    except Exception, e :
        return jsonify({'error': e.message})

@app.route('/businesses/<id>/kiosks', methods=['POST'])
def add_kiosk(id):
    try :
        content_json = request.get_json(silent=True)

        appLogger.info('id=%s, content_json=%s' % (id, content_json))

        data = BusinessHandler.add_kiosk(id, content_json)

        return jsonify(data)
    except Exception, e :
        return jsonify({'error': e.message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

    