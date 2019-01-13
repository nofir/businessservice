
class Business(object):

    def __init__(self, id = 0):
        self.id = id

    def init_from_db(self, dbRet):
        self.id = dbRet['id']
