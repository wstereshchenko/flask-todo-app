# -*- coding: utf-8 -*-

from flask import Flask
from application.controllers import blueprints
from application.configs import config
from application.extensions import db


def create_app(config_name=None):
    if config_name is None:
        config_name = 'default'

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # db
    db.init_app(app)

    # blueprints
    for bp in blueprints:
        app.register_blueprint(bp)

    return app
