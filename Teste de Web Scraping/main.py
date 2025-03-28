from bs4 import BeautifulSoup
import requests
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import zipfile


chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")


url_base = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

pdf_path = "PDFs"

pdf_links = []
def Downloader(url_base, pdf_path):
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get(url_base)
        WebDriverWait(driver, 10)
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        for link in soup.find_all('a', class_='internal-link'):
            href = link.get('href')
            if href and 'Anexo' in href and href.endswith('.pdf'):
                pdf_links.append(href)
        
        if not os.path.exists(pdf_path):
            os.makedirs(pdf_path)
        
        for pdf_link in pdf_links:
            response = requests.get(pdf_link)
            if response.status_code == 200:
                file_name = os.path.join(pdf_path, os.path.basename(pdf_link))
                with open(file_name, 'wb') as pdf_file:
                    pdf_file.write(response.content)
    finally:
        driver.quit()

def Compressor(folder_path, output_filename):
    with zipfile.ZipFile(output_filename, 'w') as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.pdf'):
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, arcname=file)


Downloader(url_base, pdf_path)
Compressor(pdf_path, 'PDFs.zip')