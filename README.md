# Painel de Controle de Compras Hospitalares

## Visão Geral

Este projeto é uma aplicação web interativa (Dashboard) projetada para centralizar, visualizar e analisar o processo de requisição de compras de múltiplos hospitais. A ferramenta transforma dados complexos de diversas planilhas Excel em uma interface de gestão visual e intuitiva, permitindo a identificação rápida de gargalos, o acompanhamento de KPIs e a análise detalhada de cada item do processo.

O objetivo principal é substituir o controle manual e fragmentado por uma solução de inteligência de negócios que otimiza a tomada de decisão e a gestão estratégica de compras.

## ✨ Funcionalidades Principais

* **Visão Multi-Hospital:** Consolida dados de diversas planilhas (uma para cada hospital) em um único painel.
* **Dashboard de KPIs:** Apresenta indicadores chave em tempo real, como Valor Total de Compras (dividido por Consumo e Imobilizado), total de Entregas em Atraso e Itens Críticos.
* **Filtros Dinâmicos:** Permite a filtragem de todos os dados por Hospital, Criticidade, Setor e Status da Entrega.
* **Funil do Processo Visual:** Gráficos interativos que mostram a distribuição das demandas em cada etapa do processo (Requisição, Pedido, Entrega).
* **Tabela Detalhada:** Exibe todos os itens de forma organizada, permitindo busca e exploração detalhada dos dados.
* **Interface Responsiva:** O layout se adapta a diferentes tamanhos de tela, funcionando em desktops, tablets e celulares.

## 🚀 Arquitetura e Tecnologias

A aplicação utiliza uma arquitetura cliente-servidor simples e eficiente:

#### Backend

* **Linguagem:** Python 3
* **Framework:** Flask
* **Bibliotecas:**
    * `pandas`: Para leitura e manipulação robusta dos dados das planilhas Excel.
    * `openpyxl`: Para que o pandas possa ler arquivos no formato `.xlsx`.
    * `Flask-Cors`: Para permitir a comunicação entre o backend e o frontend.
* **Função:** Cria um servidor local que lê os arquivos `.xlsx`, consolida os dados e os disponibiliza através de uma API REST simples no formato JSON.

#### Frontend

* **Linguagem:** HTML, CSS, JavaScript (Vanilla JS)
* **Bibliotecas:**
    * **Tailwind CSS:** Para estilização e criação de um layout moderno e responsivo.
    * **Chart.js:** Para a renderização dos gráficos interativos do painel.
* **Função:** Consome os dados fornecidos pelo backend e os renderiza em uma interface de usuário interativa, executada diretamente no navegador.

## ⚙️ Como Configurar e Executar o Projeto

Siga os passos abaixo para executar a aplicação localmente.

### 1. Pré-requisitos

* Python 3 instalado no seu computador.
* Um editor de código como o VS Code.

### 2. Estrutura de Pastas

Certifique-se de que seus arquivos estão organizados na seguinte estrutura dentro de uma única pasta:

```
/Painel_Compras/
├── 📄 app.py
├── 📄 index.html
├── 📄 hospital_A.xlsx
├── 📄 hospital_B.xlsx
└── 📄 ... (todos os outros arquivos .xlsx)
```

### 3. Instalação das Dependências

Abra um terminal na pasta raiz do projeto (`/Painel_Compras/`) e instale as bibliotecas Python necessárias:

```bash
pip install Flask pandas openpyxl Flask-Cors
```

### 4. Configuração dos Arquivos

Abra o arquivo `app.py` e edite o dicionário `HOSPITAIS` para que ele aponte para os seus arquivos Excel. O nome da "chave" (à esquerda) será exibido no filtro, e o "valor" (à direita) deve ser o nome exato do arquivo.

```python
# Exemplo de configuração em app.py
HOSPITAIS = {
    "Hospital Jardim Anália": "COPIA - Lista de compras Hospital Jardim Anália.xlsx",
    "Hospital Layr Maia": "COPIA - Lista de compras Hospital Layr Maia.xlsx",
    # Adicione os outros hospitais aqui...
}
```

**Importante:** Verifique também se o nome da aba dentro dos seus arquivos Excel corresponde ao que está definido na linha `sheet_name='...'` dentro do `app.py`. O padrão é `Lista de compras - Consolidado`.

### 5. Execução

1.  **Inicie o Servidor Backend:** No terminal, dentro da pasta do projeto, execute o comando:
    ```bash
    python app.py
    ```
    O terminal deverá indicar que o servidor está rodando em `http://127.0.0.1:5000`. Não feche este terminal.

2.  **Abra o Frontend:** Abra o arquivo `index.html` em seu navegador de preferência (Google Chrome, Firefox, etc.).

A aplicação deverá carregar e exibir os dados consolidados das suas planilhas.
