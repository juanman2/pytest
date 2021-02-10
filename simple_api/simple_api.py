# Copyright 2021 Juan Tellez All Rights Reserved
#
# A Simple API definition.
#
from datetime import date
from datetime import datetime
import uuid
import json

class SimpleApiException(Exception):
    reason = ""
    def __init__(self, reason):
        self.reason = reason
        

class SimpleApi:
    db = {}
    def __init__(self):
        self.db = {}
        
    def set_v1(self, v=None):
        if v is None:
            return
        if not isinstance(v, str):
            raise SimpleApiException("Invalid Type: {:} expected string".format(v))
        else:
            self.v1=v

    def set_v2(self, v=None):
        if v is None:
            return
        if not isinstance(v, float):
            raise SimpleApiException("Invalid Type: {:} expected float".format(v))
        else:
            self.v2=v

    def set_v3(self, v=None):
        if v is None:
            return
        if not isinstance(v, bool):
            raise SimpleApiException("Invalid Type: {:} expected bool".format(v))
        else:
            self.v3=v

    def create(self, v1=None, v2=None, v3=None):

        sw = dict()
        self.set_v1(v1)
        self.set_v2(v2)
        self.set_v3(v3)
            
        sw['id'] = uuid.uuid4()
        ct = date.today()
        sw['creationDate']=ct
        sw['lastModificationDate']=ct
        sw['timestamp']=datetime.now()

        self.db[sw['id']] = sw
        return sw

            
    def get_collection(self):
        return [ self.db[o] for o in self.db ]
        
    def get(self, oid):
        return self.db[oid]

    def remove(self, oid):
        del self.db[oid]

    def update(self, oid, v1=None, v2=None, v3=None):
        sw = get(oid)
        if v1 is not None:
            sw['v1'] = v1
        if v2 is not None:
            sw['v2'] = v2
        if v3 is not None:
            sw['v3'] = v3
        sw['lastModificationDate']=date.today()
        sw['timestamp']=datetime.now()
        self.db[oid] = sw
