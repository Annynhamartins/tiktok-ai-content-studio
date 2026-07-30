import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Libera o acesso para o GitHub Pages
CORS(app, resources={r"/api/": {"origins": ""}}, supports_credentials=True)

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "projeto": "Transparência Cidadã API",
        "versao": "1.0.0"
    })

@app.route('/api/simplificar', methods=['POST', 'OPTIONS'])
def simplificar():
    if request.method == 'OPTIONS':
        return jsonify({'status': 'ok'}), 200

    data = request.get_json() or {}
    texto = data.get('texto', '')
    categoria = data.get('categoria', 'licitacao')

    # Resposta estruturada para a interface da Transparência Cidadã
    return jsonify({
        "resumo_cidadao": "Este documento trata de aquisição/contratação pública referente ao texto inserido. Os termos principais indicam a destinação de recursos para atender às demandas administrativas da gestão.",
        "impacto_social": "Garante a continuidade dos serviços prestados à população e a correta aplicação das verbas destinadas a esta categoria.",
        "recomendacao_fiscalizacao": "Verifique o número do processo, as datas de publicação no Diário Oficial e se o valor total está de acordo com o orçamento previsto."
    })

@app.route('/api/gerar', methods=['POST'])
def gerar_conteudo():
    data = request.get_json() or {}
    tema = data.get('tema', 'Geral')
    plataforma = data.get('plataforma', 'tiktok')

    return jsonify({
        'roteiro': f"[0-3s] GANCHO IMPACTANTE: Pare tudo! Se você busca sobre {tema}, precisa ver isso.\n[3-10s] DESENVOLVIMENTO: Aqui está a principal dica sobre {tema} para aplicar na prática no seu dia a dia.",
        'legenda': f"Aprenda tudo sobre {tema}! Dica rápida e prática especialmente para a sua rotina no {plataforma.capitalize()}. 💡✨",
        'hashtags': f"#{tema.replace(' ', '')} #DicasVirais #ConteudoViral #{plataforma.capitalize()} #DicasHoje",
        'prompt': f"Ultra-detailed 8k photograph, cinematic lighting, modern showcase of {tema}, vertical 9:16 aspect ratio, trending on social media --v 6.0"
    })

if __name__ == '_main_':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
