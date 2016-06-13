from cassandra.cluster import Cluster
from datetime import datetime, timedelta
import time

def unix_time_millis(dt):
    epoch = datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000.0

def get_requests(session, query, message):
    rows = session.execute(query)
    for row in rows:
        print '%s%s' % (message, row.count)


while True:
    try:
        cluster = Cluster(['172.17.0.2'])
        session = cluster.connect('http_request_log')

        now = datetime.utcnow()
        t1 = unix_time_millis(now - timedelta(seconds=.1))
        t2 = unix_time_millis(now - timedelta(seconds=1))
        t3 = unix_time_millis(now - timedelta(minutes=1))
        now = unix_time_millis(now)

        query = "SELECT count(*) from http_request_time where insertion_time < %i and insertion_time > %i ALLOW FILTERING"
        #get_requests(session, query % (now, t1), 'Request per milisecond: ')
        get_requests(session, query % (now, t2), 'Request per second: ')
        #get_requests(session, query % (now, t3), 'Request per minute: ')
        time.sleep(.1)
    except:
        pass
