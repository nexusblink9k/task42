from flask import Flask
import subprocess
import os
import redis

r = redis.Redis(host='redis-service', port=6379, db=0)

app = Flask(__name__)

@app.route("/")
def welcome():
    if not r.exists("counter"):
        r.set('counter', 0)

    msg =  """The application has the following endpoints:<p>
    <li><a href="/healthz">/healthz</a>: return the string \'ok\'
    <li><a href="/alert">/alert</a>: increment a counter in redis [POST HTTP/1.1]
    <li><a href="/counter">/counter</a>: print the value of the counter
    <li><a href="/version">/version</a>: return the short git commit hash"""
    return(msg)

@app.route("/healthz")
def get_healthz():
    return "ok"

@app.route('/alert',methods=["POST"])
def set_counter():
    c = int(r.get('counter')) 
    c += 1
    r.set('counter', c) 
    return 'counter increased:  %i' % c

@app.route('/counter')
def get_counter():
    return r.get('counter')

@app.route("/version")
def version():
    return os.environ.get("GIT_COMMIT_HASH", "unknown")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
