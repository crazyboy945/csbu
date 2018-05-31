from flask import jsonify, request, current_app, url_for
from . import api
from app.model.contract import Contract

@api.route('/contract/<int:id>')
def get_contract(id):
    contract=Contract.query.get_or_404(id)
    return jsonify(contract.to_json())


@api.route('/contract/list/')
def get_contract_list():
    limit=10
    offset=0
    
    contracts=Contract.query.filter().limit(limit).offset(offset).all()


