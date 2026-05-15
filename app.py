from flask import Flask, jsonify, request, send_from_directory
import json, os


def ler_tarefas():
    if not os.path.exists('tarefas.json'):
        return []
    with open('tarefas.json', 'r') as f:
        return json.load(f)
    
def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as f:
        json.dump(tarefas, f, indent=2, ensure_ascii=False)


app = Flask(__name__)

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    tarefas = ler_tarefas()
    return jsonify({"tarefas": tarefas})

@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    dados = request.get_json()
    tarefas = ler_tarefas()
    novo_id = max((t["id"] for t in tarefas), default=0) + 1
    nova = {
        "id": novo_id,
        "titulo": dados["titulo"],
        "concluida": False
    }
    tarefas.append(nova)
    salvar_tarefas(tarefas)
    return jsonify(nova), 201

@app.route('/tarefas/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    dados = request.get_json()
    tarefas = ler_tarefas()
    tarefa = next((t for t in tarefas if t["id"] == id), None)
    if not tarefa:
        return jsonify({"erro": "tarefa não encontrada"}), 404
    tarefa.update(dados)
    salvar_tarefas(tarefas)
    return jsonify(tarefa)

@app.route('/tarefas/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    tarefas = ler_tarefas()
    tarefas = [t for t in tarefas if t["id"] != id]
    salvar_tarefas(tarefas)
    return jsonify({"mensagem": "Tarefa deletada"})



@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)

