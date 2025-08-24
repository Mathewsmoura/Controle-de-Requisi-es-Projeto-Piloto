import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS
import os

# Inicializa a aplicação Flask
app = Flask(__name__)
# Habilita o CORS para permitir que o HTML acesse o servidor
CORS(app)

# --- CONFIGURAÇÃO DOS HOSPITAIS ---
# Aponte para os seus arquivos .xlsx originais
HOSPITAIS = {
    ##"Hospital Jardim Anália": "COPIA - Lista de compras Hospital Jardim Anália.xlsx",
    ##"Hospital Layr Maia": "COPIA - Lista de compras Hospital Layr Maia.xlsx",
    ##"Hospital Ariano Suassuna": "COPIA - Lista de Compras Hospital Ariano Suassuna.xlsx",
    ##"PA Taguatinga": "COPIA - Lista de Compras PA Taguatinga.xlsx",
    "Hospital Santo Andre": "COPIA - Lista de compras Hospital Santo Andre.xlsx",
    "Hospital Lauro de Freitas": "COPIA - Lista de Compras Hospital Lauro de Freitas.xlsx",
}

def processar_dados_excel(filepath, nome_hospital):
    """
    Lê uma planilha específica de um arquivo Excel, mapeia as colunas e processa.
    """
    if not os.path.exists(filepath):
        print(f"AVISO: Arquivo não encontrado para {nome_hospital}: {filepath}")
        return []

    try:
        # --- MUDANÇA PRINCIPAL: LENDO ARQUIVO EXCEL ---
        # Usa pd.read_excel e especifica o nome da aba/planilha.
        # IMPORTANTE: Verifique se o nome da aba 'Lista de compras - Consolidado' 
        # está correto para TODOS os seus arquivos Excel.
        df = pd.read_excel(filepath, sheet_name='Lista de compras - Consolidado')
    except Exception as e:
        print(f"ERRO ao ler o arquivo Excel {filepath}: {e}")
        return []

    # Mapeamento flexível para encontrar variações nos nomes das colunas
    mapeamento_possivel = {
        'setor': ['SETOR'],
        'classificacao': ['DESCRIÇÃO ITEM', 'DESCRIÇÃO DO ITEM', 'DESCRISÇÃO ITEM'],
        'criticidade': ['ITEM CRITICO', 'ITEM CRÍTICO'],
        'tipo': ['TIPO DE UTILIZAÇÃO', 'TIPO'],
        'codigo': ['CÓDIGO ITEM', 'CÓDIGO'],
        'qtd': ['QTD. AQUISIÇÃO', 'QTD', 'QUANTIDADE'],
        'valorUnitario': ['PREÇO UNITÁRIO', 'VALOR UNITÁRIO'],
        'valorTotal': ['VALOR TOTAL'],
        'comprador': ['COMPRADOR(A)', 'COMPRADOR'],
        'rcCoupa': ['Nº REQUISIÇÃO COUPA'],
        'rcSap': ['Nº REQUISIÇÃO SAP'],
        'statusAprovacao': ['STATUS REQUISIÇÃO', 'STATUS APROVAÇÃO'],
        'aprovador': ['NOME APROVADOR', 'APROVADOR'],
        'pedidoCoupa': ['Nº PEDIDO COUPA'],
        'pedidoSap': ['Nº PEDIDO SAP'],
        'statusPedido': ['STATUS PEDIDO'],
        'fornecedor': ['FORNECEDOR'],
        'dataEntrega': ['DATA DE ENTREGA PREVISTA', 'DATA ENTREGA'],
        'statusEntrega': ['STATUS RECEBIMENTO', 'STATUS ENTREGA']
    }

    rename_dict = {}
    for standard_name, possible_names in mapeamento_possivel.items():
        for p_name in possible_names:
            if p_name in df.columns:
                rename_dict[p_name] = standard_name
                break
    
    df = df.rename(columns=rename_dict)
    df['hospital'] = nome_hospital
    
    colunas_mapeadas = list(mapeamento_possivel.keys()) + ['hospital']
    
    for col in colunas_mapeadas:
        if col not in df.columns:
            df[col] = None

    df_mapeado = df[colunas_mapeadas]
    
    for col in ['qtd', 'valorUnitario', 'valorTotal']:
        if col in df_mapeado.columns:
            df_mapeado[col] = pd.to_numeric(df_mapeado[col], errors='coerce')

    df_mapeado = df_mapeado.fillna(0)
    
    return df_mapeado.to_dict(orient='records')

@app.route('/data')
def get_data():
    todos_os_dados = []
    for hospital, arquivo_excel in HOSPITAIS.items():
        dados_hospital = processar_dados_excel(arquivo_excel, hospital)
        if dados_hospital:
            todos_os_dados.extend(dados_hospital)
    
    if not todos_os_dados:
        return jsonify({"error": "Nenhum dado encontrado. Verifique os nomes dos arquivos Excel e se eles estão na pasta correta."})

    return jsonify(todos_os_dados)

if __name__ == '__main__':
    app.run(debug=True)
