from flask import Flask, jsonify, request

app = Flask(__name__)

# cadastros iniciais
cads = [

    {
        'id': 1,
        'livro': 'Guerra dos Tronos',
        'status': 'disponivel',
        'rent': 'vazio',
        'returndate': 'vazio'
    },
    {
        'id': 2,
        'livro': 'Dom Casmurro',
        'status': 'alugado',
        'rent': 'Maria',
        'returndate': '12 08 2019'
    },
    {
        'id': 3,
        'livro': 'Doctor Who',
        'status': 'disponivel',
        'rent': 'vazio',
        'returndate': 'vazio'
    },
    {
        'id': 4,
        'livro': 'A Insustentavel Leveza do Ser',
        'status': 'alugado',
        'rent': 'Carol',
        'returndate': '30 08 2019'
    }
]

#  listar todos
@app.route('/cads', methods=['GET'])
def home():
    return jsonify(cads), 200

#  listar por status
@app.route('/cads/<string:status>', methods=['GET'])
def cads_per_status(status):
    cads_per_status = [cad for cad in cads if cad['status'] == status]
    return jsonify(cads_per_status), 200

#  editar status, data de devolução e cliente via id
@app.route('/cads/<int:id>', methods=['PUT'])
def change_status(id):
    for cad in cads:
        if cad['id'] == id:
            cad['status'] = request.get_json().get('status')
            cad['rent'] = request.get_json().get('rent')
            cad['returndate'] = request.get_json().get('returndate')

            return jsonify(cad), 200

    return jsonify({'error': 'cad not found'}), 404

#  listar por id
@app.route('/cads/<int:id>', methods=['GET'])
def cads_per_id(id):
    for cad in cads:
        if cad['id'] == id:
            return jsonify(cad), 200

    return jsonify({'error': 'not found'}), 404

#  novo cadastro
@app.route('/cads', methods=['POST'])
def save_cad():
    data = request.get_json()
    cads.append(data)
    return jsonify(data), 201

# deletar um cadastro
@app.route('/cads/<int:id>', methods=['DELETE'])
def remove_cad(id):
    index = id - 1
    del cads[index]

    return jsonify({'message': 'cad is no longer alive'}), 200


if __name__ == '__main__':
    app.run(debug=True)
