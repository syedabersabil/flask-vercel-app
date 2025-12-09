from flask import Flask, render_template_string, jsonify, request
import json
import datetime

app = Flask(__name__)

# HTML template embedded in Python
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask + Vercel App</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', system-ui, sans-serif;
        }
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            max-width: 600px;
            width: 100%;
        }
        h1 {
            color: #667eea;
            margin-bottom: 10px;
            font-size: 2.5rem;
        }
        .subtitle {
            color: #666;
            margin-bottom: 30px;
            font-size: 1.1rem;
        }
        .card {
            background: #f8f9fa;
            border-radius: 12px;
            padding: 25px;
            margin: 20px 0;
        }
        .card h3 {
            color: #764ba2;
            margin-bottom: 15px;
        }
        .info-item {
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 1px solid #dee2e6;
        }
        .info-item:last-child {
            border-bottom: none;
        }
        .label {
            font-weight: 600;
            color: #495057;
        }
        .value {
            color: #6c757d;
        }
        .button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 25px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            margin-top: 20px;
            transition: transform 0.2s;
        }
        .button:hover {
            transform: translateY(-2px);
        }
        .response {
            margin-top: 20px;
            padding: 15px;
            background: #e7f3ff;
            border-left: 4px solid #667eea;
            border-radius: 8px;
            display: none;
        }
        .features {
            list-style: none;
            padding: 0;
        }
        .features li {
            padding: 8px 0;
            padding-left: 25px;
            position: relative;
        }
        .features li:before {
            content: "✓";
            position: absolute;
            left: 0;
            color: #667eea;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Flask + Vercel</h1>
        <p class="subtitle">Python serverless web application</p>
        
        <div class="card">
            <h3>App Information</h3>
            <div class="info-item">
                <span class="label">Framework:</span>
                <span class="value">Flask (Python)</span>
            </div>
            <div class="info-item">
                <span class="label">Hosting:</span>
                <span class="value">Vercel Serverless</span>
            </div>
            <div class="info-item">
                <span class="label">Status:</span>
                <span class="value" style="color: #28a745;">✓ Active</span>
            </div>
            <div class="info-item">
                <span class="label">Server Time:</span>
                <span class="value" id="serverTime">{{ server_time }}</span>
            </div>
        </div>

        <div class="card">
            <h3>Features</h3>
            <ul class="features">
                <li>Zero-config deployment on Vercel</li>
                <li>Python serverless functions</li>
                <li>Auto-scaling and CDN</li>
                <li>Free HTTPS and custom domains</li>
                <li>Easy GitHub integration</li>
            </ul>
        </div>

        <button class="button" onclick="testAPI()">Test API Endpoint</button>
        
        <div class="response" id="response"></div>
    </div>

    <script>
        async function testAPI() {
            const responseDiv = document.getElementById('response');
            responseDiv.style.display = 'block';
            responseDiv.innerHTML = 'Loading...';
            
            try {
                const res = await fetch('/api/hello');
                const data = await res.json();
                responseDiv.innerHTML = `
                    <strong>API Response:</strong><br>
                    ${JSON.stringify(data, null, 2)}
                `;
            } catch (error) {
                responseDiv.innerHTML = `<strong>Error:</strong> ${error.message}`;
            }
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    server_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template_string(HTML_TEMPLATE, server_time=server_time)

@app.route('/api/hello')
def hello_api():
    return jsonify({
        'message': 'Hello from Flask on Vercel!',
        'status': 'success',
        'timestamp': datetime.datetime.now().isoformat(),
        'framework': 'Flask',
        'platform': 'Vercel Serverless'
    })

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({
        'received': data,
        'message': 'Data echoed successfully',
        'timestamp': datetime.datetime.now().isoformat()
    })

# This is important for Vercel
if __name__ == '__main__':
    app.run(debug=True)
