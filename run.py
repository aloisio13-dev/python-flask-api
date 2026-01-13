from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota de teste
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Olá, API Flask funcionando!"})

# CRUD de usuários (exemplo simples em memória)
usuarios = []

@app.route('/users', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios)

@app.route('/users/<int:user_id>', methods=['GET'])
def detalhar_usuario(user_id):
    for u in usuarios:
        if u["id"] == user_id:
            return jsonify(u)
    return jsonify({"error": "Usuário não encontrado"}), 404

@app.route('/users', methods=['POST'])
def criar_usuario():
    data = request.get_json()
    novo = {"id": len(usuarios) + 1, "nome": data.get("nome"), "email": data.get("email")}
    usuarios.append(novo)
    return jsonify(novo), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def atualizar_usuario(user_id):
    data = request.get_json()
    for u in usuarios:
        if u["id"] == user_id:
            u["nome"] = data.get("nome", u["nome"])
            u["email"] = data.get("email", u["email"])
            return jsonify(u)
    return jsonify({"error": "Usuário não encontrado"}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def remover_usuario(user_id):
    global usuarios
    usuarios = [u for u in usuarios if u["id"] != user_id]
    return jsonify({"message": "Usuário removido com sucesso"})

if __name__ == '__main__':
    app.run(debug=True)
