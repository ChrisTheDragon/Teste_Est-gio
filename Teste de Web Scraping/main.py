import os
import requests
import zipfile
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

# Configurações globais
CHROME_OPTIONS = Options()
CHROME_OPTIONS.add_argument("--headless")  # Executar em modo headless
CHROME_OPTIONS.add_argument("--disable-gpu")
CHROME_OPTIONS.add_argument("--no-sandbox")

URL_BASE = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
PDF_PATH = "Teste de Web Scraping/PDFs"
ZIP_OUTPUT_FILENAME = "PDFs.zip"

def setup_driver():
    """Configura e retorna uma instância do WebDriver."""
    return webdriver.Chrome(options=CHROME_OPTIONS)

def fetch_pdf_links(driver, url):
    """Obtém os links de arquivos PDF da página especificada."""
    pdf_links = []
    driver.get(url)
    WebDriverWait(driver, 10)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    for link in soup.find_all('a', class_='internal-link'):
        href = link.get('href')
        if href and 'Anexo' in href and href.endswith('.pdf'):
            pdf_links.append(href)
    
    return pdf_links

def download_pdfs(pdf_links, download_path):
    """Faz o download dos arquivos PDF para o diretório especificado."""
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    for pdf_link in pdf_links:
        response = requests.get(pdf_link)
        if response.status_code == 200:
            file_name = os.path.join(download_path, os.path.basename(pdf_link))
            print(f"Baixando {file_name} em {download_path}")
            with open(file_name, 'wb') as pdf_file:
                pdf_file.write(response.content)
            print("Download concluído")
        else:
            print(f"Falha ao baixar {pdf_link}. Código de status: {response.status_code}")

def compress_pdfs(folder_path, output_filename):
    """Compacta os arquivos PDF em um arquivo ZIP."""
    with zipfile.ZipFile(output_filename, 'w') as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.pdf'):
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, arcname=file)
                    print(f"Adicionando {file} ao arquivo {output_filename}")
    print("Compactação concluída")

def main():
    """Função principal para executar o fluxo do programa."""
    driver = setup_driver()
    try:
        pdf_links = fetch_pdf_links(driver, URL_BASE)
        download_pdfs(pdf_links, PDF_PATH)
        compress_pdfs(PDF_PATH, ZIP_OUTPUT_FILENAME)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()