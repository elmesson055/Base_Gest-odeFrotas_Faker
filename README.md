# Gerador de Base de Dados de Veículos

Este projeto gera uma base de dados sintética de veículos e exporta os dados para um arquivo Excel com múltiplas abas, incluindo informações do veículo, histórico de manutenções, controle de abastecimento e multas.

## Requisitos

- Python 3.7 ou superior

## Instalação

1. **Instale o Python**

   Baixe e instale o Python em [python.org](https://www.python.org/downloads/).  
   Durante a instalação, marque a opção **"Add Python to PATH"**.

2. **Instale as dependências**

   Abra o Prompt de Comando e execute:
   ```bash
   pip install pandas faker

   ## Como usar
1. Coloque o arquivo generate_vehicle_data.py na pasta c:\Users\**********\Desktop\Base .
2. Abra o Prompt de Comando e navegue até a pasta:

cd c:\Users\**********\Desktop\Base

Execute o script:

python generate_vehicle_data.py


1. Após a execução, o arquivo veiculos.xlsx será criado na mesma pasta com os dados gerados.
## Saída
- veiculos.xlsx : Arquivo Excel com as seguintes abas:
  - Principal : Dados principais e controles do veículo
  - Manutencoes : Histórico de manutenções
  - Abastecimento : Controle de abastecimento
  - Multas : Multas e infrações
## Observações
- Caso encontre problemas com o pip ou Python, verifique se o Python está instalado corretamente e adicionado ao PATH do sistema.