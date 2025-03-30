from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Carrega os dados do CSV
df = pd.read_csv(
    r"Teste de API\backend\Relatorio_cadop.csv", 
    sep=';', 
    encoding='utf-8'
)
df = df.fillna('')  # Substitui valores NaN por strings vazias

@app.route('/api/search', methods=['GET'])
def search_operadoras():
    # Obtém o termo de busca da query string
    termo = request.args.get('q', '').lower()
    print(f"Termo de busca: {termo}")
    
    # Retorna uma lista vazia se nenhum termo for fornecido
    if not termo:
        return jsonify([])
    
    # Filtra os dados com base no termo de busca
    resultados = df[
        df['Registro_ANS'].str.lower().str.contains(termo) |
        df['CNPJ'].str.contains(termo) |
        df['Nome_Fantasia'].str.lower().str.contains(termo) |
        df['Razao_Social'].str.lower().str.contains(termo)
    ].head(20).to_dict('records')
    
    # Log do número de resultados encontrados
    print(f"Resultados encontrados: {len(resultados)}")
    
    # Retorna os resultados como JSON
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True, port=5000)