from flask import Flask
from config import config
from dotenv import load_dotenv

def create_app(config_name='default'):
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Add your app configuration and routes here
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/api')

    return app

app = create_app()