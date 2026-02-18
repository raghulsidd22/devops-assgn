from flask import Flask, jsonify, render_template
import datetime
import zoneinfo

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/status')
def status():
    return jsonify({
        'status': 'running',
        'message': 'Flask app is live on EC2!',
        'timestamp': datetime.datetime.now(zoneinfo.ZoneInfo('Asia/Kolkata')).isoformat()
    })

@app.route('/api/hello')
def hello():
    return jsonify({'message': 'Hello from Flask on EC2!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)
""