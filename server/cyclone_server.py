#! /usr/bin/python
import cyclone.web
import sys

from cassandra.cluster import Cluster
from twisted.internet import reactor
from twisted.python import log
import time

def getMilliseconds():
    return int(time.time()*1000)

def insert_to_cassandra(self):
    cql = "INSERT INTO http_request_log.http_request_time \
           (creation_time, host, id, insertion_time) VALUES \
           ('%s',0,777,toTimestamp(now()))" % (getMilliseconds())
    self.cassandra_session.execute_async(cql)



class MainHandler(cyclone.web.RequestHandler):
    def initialize(self, db_session):
	self.cassandra_session = db_session
    def get(self):
        self.write("Hello, world")
    def post(self):
        insert_to_cassandra(self)


if __name__ == "__main__":

    cluster = Cluster(['reto3db'])
    session = cluster.connect('http_request_log')

    application = cyclone.web.Application([
        (r"/", MainHandler, dict(db_session=session))
    ])

    log.startLogging(sys.stdout)
    reactor.listenTCP(80, application)
    reactor.run()
