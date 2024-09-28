from flask import Flask, jsonify
from routes.kazuma import efficient_hunter_kazuma

app = Flask(__name__)

# Register the blueprint for the efficient hunter kazuma route
app.register_blueprint(efficient_hunter_kazuma, url_prefix='/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
