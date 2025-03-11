# Extração de Dados de PDFs para Excel

Este projeto tem como objetivo extrair informações específicas (CNPJs e datas) de múltiplos arquivos PDF e consolidá-las em um formato estruturado (Excel) para análise e processamento posterior.

## Dificuldades Enfrentadas

1.  **Variedade de Formatos de Data**: Os PDFs podem conter datas em diferentes formatos (DD.MM.YYYY, DD/MM/YYYY, DD de Mês de AAAA), o que exige uma normalização para garantir a consistência dos dados.
2.  **Estrutura Variável dos PDFs**: A estrutura dos PDFs pode variar, dificultando a extração de dados de forma consistente.
3.  **Extração de Texto Imprecisa**: A extração de texto de PDFs pode ser imprecisa, especialmente em PDFs digitalizados ou com formatação complexa.
4.  **Lidar com Grandes Volumes de Dados**: O processamento de um grande número de arquivos PDF pode ser demorado e exigir otimizações de desempenho.

## Soluções

1.  **Normalização de Datas**: Implementamos uma função (`normalizar_data`) que utiliza expressões regulares para identificar e converter datas em diferentes formatos para o formato 'DD/MM/YYYY'.
2.  **Expressões Regulares para Extração de Dados**: Utilizamos expressões regulares para buscar CNPJs e datas nos textos extraídos dos PDFs.
3.  **Biblioteca `pdfplumber`**: Utilizamos a biblioteca `pdfplumber` para extrair texto de PDFs de forma eficiente e precisa.
4.  **Biblioteca `pandas`**: Utilizamos a biblioteca `pandas` para organizar os dados extraídos em um DataFrame e salvá-los em um arquivo Excel.
5.  **Modularização do Código**: Dividimos o código em funções menores e mais específicas para facilitar a manutenção e o teste.
6.  **Tratamento de erros**: Implementamos tratamento de erros para arquivos PDF corrompidos ou ilegíveis.

## Bibliotecas Utilizadas

* **`pdfplumber`**: Para extrair texto e outros dados de arquivos PDF.
    * Documentação: [https://github.com/jsvine/pdfplumber](https://github.com/jsvine/pdfplumber)
* **`pandas`**: Para manipulação e análise de dados, e para salvar os dados em um arquivo Excel.
    * Documentação: [https://pandas.pydata.org/](https://pandas.pydata.org/)
* **`re`**: Para utilizar expressões regulares na busca e manipulação de texto.
    * Documentação: [https://docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html)
* **`os`**: Para manipulação de arquivos e diretórios.
    * Documentação: [https://docs.python.org/3/library/os.html](https://docs.python.org/3/library/os.html)

## Melhorias Futuras

* Implementação de testes unitários para garantir a robustez do código.
* Otimização do desempenho para lidar com grandes volumes de arquivos PDF.
* Implementação de um sistema de logs para acompanhar o progresso do programa e identificar erros.
* Implementação de um tratamento de erros mais completo, como por exemplo tratamento de erro caso o arquivo não seja encontrado, ou caso não seja um PDF.
* Suporte a outros formatos de arquivo além de PDF.
* Implementação de uma interface gráfica para facilitar o uso do programa.

## Como Executar

1.  Clone este repositório.
2.  Instale as dependências: `pip install pdfplumber pandas openpyxl`
3.  Execute o script `extracao_pdf.py`: `python extracao_pdf.py`
