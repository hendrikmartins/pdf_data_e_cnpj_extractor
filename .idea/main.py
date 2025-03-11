import os
import re
import pandas as pd
import pdfplumber
from datetime import datetime

MESES = {
    'janeiro': '01',
    'fevereiro': '02',
    'março': '03',
    'abril': '04',
    'maio': '05',
    'junho': '06',
    'julho': '07',
    'agosto': '08',
    'setembro': '09',
    'outubro': '10',
    'novembro': '11',
    'dezembro': '12'
}

def normalizar_data(data):
    """Converte datas em diferentes formatos para 'DD/MM/YYYY'."""


    if re.match(r'\d{2}\.\d{2}\.\d{4}', data):
        return data.replace('.', '/')
    match = re.match(r'(\d{2}) de ([a-zA-Z]+) de (\d{4})', data)
    if match:
        dia, mes_extenso, ano = match.groups()
        mes = MESES.get(mes_extenso.lower())
        if mes:
            return f'{dia}/{mes}/{ano}'

    if re.match(r'\d{2}/\d{2}/\d{4}', data):
        return data
    return data

def extrair_dados_pdf(caminho_pdf):
    dados = []
    nome_arquivo = os.path.basename(caminho_pdf)

    with pdfplumber.open(caminho_pdf) as pdf:
        for numero_pagina, pagina in enumerate(pdf.pages, start=1):
            texto = pagina.extract_text()
            if texto:
                cnpjs = re.findall(r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}', texto)


                datas_format1 = re.findall(r'\d{2}\.\d{2}\.\d{4}', texto)
                datas_format2 = re.findall(r'\d{2} de [a-zA-Z]+ de \d{4}', texto)
                datas_format3 = re.findall(r'\d{2}/\d{2}/\d{4}', texto)


                datas = datas_format1 + datas_format2 + datas_format3
                datas_normalizadas = [normalizar_data(data) for data in datas]

                dados.append({
                    'arquivo': nome_arquivo,
                    'pagina': numero_pagina,
                    'cnpjs': ', '.join(cnpjs) if cnpjs else '',
                    'datas': ', '.join(datas_normalizadas) if datas_normalizadas else ''
                })

    return dados

def processar_pdfs(pasta_pdfs, local_salvar_excel):
    dados_totais = []

    for arquivo in os.listdir(pasta_pdfs):
        if arquivo.endswith('.pdf'):
            caminho_pdf = os.path.join(pasta_pdfs, arquivo)
            dados_pdf = extrair_dados_pdf(caminho_pdf)
            dados_totais.extend(dados_pdf)

    df = pd.DataFrame(dados_totais)
    df.to_excel(local_salvar_excel, index=False)
    print(f"Dados extraídos e salvos em {local_salvar_excel}")


pasta_pdfs = 'C:/Users/Downloads/PastaTestePDF'
local_salvar_excel = 'C:/Users/Downloads/dados_extraidos.xlsx'

processar_pdfs(pasta_pdfs, local_salvar_excel)

