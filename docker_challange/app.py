import os
import redis
from flask import Flask

# Read host and port from env vars (with default fallbacks)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))

r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

app = Flask(__name__)
app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'Hello, World!'

@app.route('/count')
def count():
    r.incr('visits')  # increments the 'visits' key
    count = r.get('visits')
    return f"Visited: " + count

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)