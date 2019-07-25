import os
import json
from flask import Flask, render_template, jsonify
from flask_cors import CORS
from flask import redirect
from flask import url_for
from environs import Env
from .json_encoder import MongoJSONEncoder
from .seed import seed

from elsy.config import APP_SECRET

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=APP_SECRET
    )

    app.json_encoder = MongoJSONEncoder

    try:
        # Ensure instance path exists
        os.makedirs(app.instance_path)
    except OSError:
        # So it already exists... do nothing
        pass

    # Applying cors
    CORS(app)

    from elsy import routes
    app.register_blueprint(routes.bp)

    app.cli.add_command(seed)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app