from flask import Flask


def create_app():
    import sys

    from .shared.http.api import Api
    from .shared.http.routes.main import main
    from .shared.http.routes.transactions import transactions
    from .config import DefaultConfig, TestConfig

    app = Flask(__name__, instance_relative_config=True)

    if "pytest" in sys.modules:
        app.config.from_object(TestConfig)
    else:
        app.config.from_object(DefaultConfig)

    app.register_blueprint(main)
    app.register_blueprint(transactions, url_prefix='/transactions')
    app = Api.init_app(app)

    return app