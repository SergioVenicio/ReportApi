from flask import Blueprint, current_app, request, make_response
from flask.json import jsonify


transactions = Blueprint('transactions', __name__)


@transactions.route('/<string:transaction_id>')
def get_transaction(transaction_id):
    return make_response(
        current_app.api.get_transaction(transaction_id),
        200
    )

@transactions.route('/report', methods=['GET'])
def reports():
    errors = []
    from_date = request.args.get('from_date')
    if from_date is None:
        errors.append('from_date is required!')

    to_date = request.args.get('to_date')
    if to_date is None:
        errors.append('to_date is required!')

    if len(errors) > 0:
        return jsonify({
            'errors': errors
        })

    merchant = request.args.get('merchant')
    acquirer = request.args.get('acquirer')
    payment_method = request.args.get('payment_method', 'CREDITCARD')
    data = {}
    raw_data = {
        'fromDate': from_date,
        'toDate': to_date,
        'merchant': merchant,
        'acquirer': acquirer,
        'paymentMethod': payment_method
    }
    for key, value in raw_data.items():
        if  value is None:
            continue
        
        data[key] = value

    return make_response(
        current_app.api.list_transactions_report(data=data),
        200
    )


@transactions.route('/list', methods=['GET'])
def list():
    data = {}
    raw_data = {
        'fromDate': request.args.get('from_date'),
        'toDate': request.args.get('to_date'),
        'status': request.args.get('status'),
        'operation': request.args.get('operation'),
        'merchantId': request.args.get('merchant_id'),
        'acquirerId': request.args.get('acquirer_id'),
        'paymentMethod': request.args.get('payment_method', 'CREDITCARD'),
        'errorCode': request.args.get('error_code'),
        'filterField': request.args.get('filter_field'),
        'filterValue': request.args.get('filter_value'),
        'page': request.args.get('page', 1)
    }

    for key, value in raw_data.items():
        if  value is None:
            continue
        
        data[key] = value

    content = current_app.api.list_transactions(data=data)
    def parse_urls(current_page, new_page):
        path, params = request.url.split('?')
        params = params.replace(f'page={current_page}', f'page={new_page}')
        return f'{path}?{params}'

    current_page = int(request.args.get('page', 1))
    if content.get('next_page_url'):
        content['next_page_url'] = parse_urls(current_page, current_page+1)

    if content.get('prev_page_url'):
        content['prev_page_url'] = parse_urls(current_page, current_page-1)

    return make_response(
        content,
        200
    )