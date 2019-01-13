import os
import sys
import logging
import logging.config
import loggly.handlers

from config import config

appLogger = logging.getLogger(config.APP_NAME)
appLogger.setLevel(logging.INFO) 

if config.LOGGLY_ENABLED:
    logglyhandler = loggly.handlers.HTTPSHandler(config.LOGGLY_URL, "POST")
    logglyhandler.setFormatter(logging.Formatter('{ "log": { "app":"%(name)s", "timestamp":"%(asctime)s", "fileName":"%(filename)s", "logRecordCreationTime":"%(created)f", "functionName":"%(funcName)s", "levelNo":"%(levelno)s", "lineNo":"%(lineno)d", "time":"%(msecs)d", "levelName":"%(levelname)s", "message":"%(message)s"} }'))
    logglyhandler.setLevel(logging.INFO) 
    appLogger.addHandler(logglyhandler)

consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setFormatter(logging.Formatter('%(asctime)s %(name)s %(levelname)s - %(filename)s - %(funcName)s - %(message)s'))
consoleHandler.setLevel(logging.DEBUG) 
appLogger.addHandler(consoleHandler)

appLogger = logging.LoggerAdapter(appLogger, {
    'env': os.environ.get('FLASK_ENV', 'development')
})
