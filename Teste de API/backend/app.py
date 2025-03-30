from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite requisições do frontend

# Carrega os dados do CSV
df = pd.read_csv('operadoras.csv', sep=';', encoding='utf-8')

@app.route('/api/search', methods=['GET'])
def search_operadoras():
    termo = request.args.get('q', '').lower()
    
    if not termo:
        return jsonify([])
    
    # Filtra operadoras que contenham o termo no nome ou código
    resultados = df[
        df['DESCRICAO'].str.lower().str.contains(termo) |
        df['CD_CONTA_CONTABIL'].astype(str).str.contains(termo)
    ].head(20).to_dict('records')
    
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True, port=5000)