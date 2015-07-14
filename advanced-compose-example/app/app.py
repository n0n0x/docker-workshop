import os
import platform

from flask import Flask
import redis

r= redis.StrictRedis(host='redis')

app = Flask(__name__)

@app.route("/")
def up():
    counter = r.incr('counter', 1)
    return "This page has been viewed {} times! Host: {} is production: {}".format(counter, platform.node(), os.environ.get('PRODUCTION'))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
