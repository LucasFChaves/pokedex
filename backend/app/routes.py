from flask import Blueprint, request, jsonify
from .models import inserir_pokemon, listar_pokemons, inserir_tipo, listar_tipos

bp = Blueprint('main', __name__)

# ROTA /pokemons
@bp.route('/pokemons', methods=['GET', 'POST'])
def pokemons():
    if request.method == 'GET':
        return jsonify(listar_pokemons())
    elif request.method == 'POST':
        data = request.get_json()
        if inserir_pokemon(data):
            return jsonify({'mensagem': 'Pokémon inserido com sucesso'}), 201
        return jsonify({'erro': 'Dados inválidos'}), 400

# ROTA /tipos
@bp.route('/tipos', methods=['GET', 'POST'])
def tipos():
    if request.method == 'GET':
        return jsonify(listar_tipos())
    elif request.method == 'POST':
        data = request.get_json()
        nome = data.get("nome")
        if nome and inserir_tipo(nome):
            return jsonify({'mensagem': 'Tipo inserido com sucesso'}), 201
        return jsonify({'erro': 'Tipo já existe ou inválido'}), 400

