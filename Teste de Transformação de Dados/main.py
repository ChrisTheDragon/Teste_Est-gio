import pdfplumber
import pandas as pd
import os


def extract_tables_from_pdf(pdf_path):
    """Extrai tabelas de um arquivo PDF usando pdfplumber."""
    tables = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                extracted_table = page.extract_table()
                if extracted_table:
                    df = pd.DataFrame(extracted_table)
                    tables.append(df)
    except Exception as e:
        print(f"Erro ao processar o PDF: {e}")
    return tables


def save_tables_to_csv(tables, output_path):
    """Salva as tabelas extraídas em um arquivo CSV."""
    try:
        if tables:
            final_table = pd.concat(tables, ignore_index=True)
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            final_table.to_csv(output_path, index=False, header=False, encoding='utf-8')
            print(f"Tabelas salvas com sucesso em: {output_path}")
        else:
            print("Nenhuma tabela encontrada no PDF.")
    except Exception as e:
        print(f"Erro ao salvar as tabelas no CSV: {e}")


def main():
    # Caminho do arquivo PDF
    pdf_path = "Teste de Web Scraping/PDFs/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
    
    # Caminho do arquivo CSV de saída
    csv_path = "Teste de Transformação de Dados/tabelas_extraidas_1.csv"
    
    # Extração e salvamento das tabelas
    tables = extract_tables_from_pdf(pdf_path)
    save_tables_to_csv(tables, csv_path)


if __name__ == "__main__":
    main()
