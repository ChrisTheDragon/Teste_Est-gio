from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite requisições do frontend

# Carrega os dados do CSV
df = pd.read_csv(r"Teste de API\backend\Relatorio_cadop.csv", sep=';', encoding='utf-8')
df = df.fillna('')  # Substitui todos os valores NaN por uma string vazia

@app.route('/api/search', methods=['GET'])
def search_operadoras():
    termo = request.args.get('q', '').lower()
    print(f"Termo de busca: {termo}")  # Log do termo de busca
    
    if not termo:
        return jsonify([])
    
    # Garantir que as colunas sejam strings e preencher valores nulos
    df['Registro_ANS'] = df['Registro_ANS'].fillna("").astype(str)
    df['CNPJ'] = df['CNPJ'].fillna("").astype(str)
    df['Nome_Fantasia'] = df['Nome_Fantasia'].fillna("").astype(str)
    df['Razao_Social'] = df['Razao_Social'].fillna("").astype(str)
    
    # Filtra operadoras que contenham o termo no nome ou código
    resultados = df[
        df['Registro_ANS'].str.lower().str.contains(termo) |
        df['CNPJ'].str.contains(termo) |
        df['Nome_Fantasia'].str.lower().str.contains(termo) |
        df['Razao_Social'].str.lower().str.contains(termo)
    ].head(20).to_dict('records')
    
    print(f"Resultados encontrados: {len(resultados)}")  # Log do número de resultados
    
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True, port=5000)