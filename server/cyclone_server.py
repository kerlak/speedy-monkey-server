import cyclone.web
import sys

from cassandra.cluster import Cluster
from twisted.internet import reactor
from twisted.python import log
from datetime import datetime


def insert_to_cassandra(count_id, session):
    cql = "INSERT INTO http_request_log.http_request_time \
           (creation_time, host, id, insertion_time) VALUES \
           ('%s',0,%s,toTimestamp(now()))" % (datetime.now().strftime('%s'), count_id)
    session.execute_async(cql)


class MainHandler(cyclone.web.RequestHandler):
    def initialize(self, count_id, db_session):
        self.count_id = count_id
        self.db_session = db_session
    def get(self):
        self.write("Hello, world")
    def post(self):
        self.count_id += 1
        insert_to_cassandra(self.count_id, self.db_session)


if __name__ == "__main__":

    count_id = 0
    cluster = Cluster(['reto3db'])
    session = cluster.connect('http_request_log')

    application = cyclone.web.Application([
        (r"/", MainHandler, dict(count_id=count_id, db_session=session))
    ])

    log.startLogging(sys.stdout)
    reactor.listenTCP(8888, application)
    reactor.run()
