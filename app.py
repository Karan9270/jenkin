from flask import Flask 

def create_app():

    app = Flask(__name__)

    @app.route('/',methods=['GET'])
    def root():
        return "welcome to hell"

    @app.route('/health',methods=['GET'])
    def health():
        return " hell is healthy"

    return app    