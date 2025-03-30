import os
import pandas as pd
from langchain_unstructured import UnstructuredLoader
from unstructured_client import UnstructuredClient
from dotenv import load_dotenv, find_dotenv
from io import StringIO  # Import necessário para usar StringIO


def pdf_to_doc(file_path):
    """
    Carregar um documento PDF para análise e salvar o conteúdo em um arquivo TXT.
    
    Args:
        file_path (str): O caminho do arquivo PDF.
    
    Returns:
        list: Uma lista de documentos carregados.
    """
    load_dotenv(find_dotenv())
    unstructured_api_key = os.getenv("UNSTRUCTURED_API_KEY")
    unstructured_api_url = os.getenv("UNSTRUCTURED_API_URL")
    
    loader = UnstructuredLoader(
        file_path=file_path,
        strategy="hi_res",
        partition_via_api=True,
        coordinates=True,
        client=UnstructuredClient(
            api_key_auth=unstructured_api_key, 
            server_url=unstructured_api_url
        )
    )
    
    docs = loader.load()  # Carrega e divide o documento PDF em páginas
    print(f"{len(docs)} documentos carregados.")
    
    # Salvar o conteúdo dos documentos em um arquivo TXT
    with open("Teste de Transformação de Dados/docs_output.txt", "w", encoding="utf-8") as f:
        f.write(str([el.metadata['text_as_html'] for el in docs if el.metadata['category'] == "Table"]))
        print('escrevendo o arquivo...')
    
    return docs


def extract_tables_from_docs(docs):
    """
    Extrair tabelas dos documentos carregados com base na categoria 'table'.
    
    Args:
        docs (list): Lista de documentos carregados.
    
    Returns:
        list: Lista de tabelas extraídas.
    """
    tables = []
    tables = [el.metadata['text_as_html'] for el in docs if el.metadata['category'] == "Table"]
    print(f"{len(tables)} tabelas extraídas.")
    return tables


def save_tables_to_csv(html_tables, csv_path):
    """
    Salvar tabelas em formato HTML em um arquivo CSV.
    
    Args:
        html_tables (list): Lista de tabelas em formato HTML.
        csv_path (str): Caminho do arquivo CSV de saída.
    """
    # Combinar todas as tabelas HTML em um único DataFrame
    combined_df = pd.concat(
        [pd.read_html(StringIO(table), header=0)[0] for table in html_tables],
        ignore_index=True
    )
    print(f"{len(combined_df)} linhas combinadas.")
    combined_df.to_csv(csv_path, index=False)


def main():
    pdf_path = "Teste de Web Scraping/PDFs/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
    csv_path = "Teste de Transformação de Dados/tabelas_extraidas.csv"

    # Carregar o PDF e extrair os documentos
    docs = pdf_to_doc(pdf_path)
    #print(docs[0])

    # Extrair tabelas dos documentos
    tables = extract_tables_from_docs(docs)
    
    print(f"{len(tables)} tabelas extraídas.")
    print(tables[0])

    # Salvar as tabelas em um arquivo CSV
    save_tables_to_csv(tables, csv_path)

    #print(f"Tabelas extraídas e salvas em {csv_path}")


if __name__ == "__main__":
    main()
