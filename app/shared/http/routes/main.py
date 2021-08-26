from flask import Blueprint, make_response
from flask.json import jsonify


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return make_response(
        jsonify({
            'enpoints': [
                'transactions/<transactions_id>',
                'transactions/list',
                'transactions/report?from_date=date&to_date=date'
            ]
        }),
        200
    )