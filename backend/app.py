import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(_name_)
CORS(app, resources={r"/api/": {"origins": ""}}, supports_credentials=True)

@app.route('/api/simplificar', methods=['POST', 'OPTIONS'])
def home():
    return jsonify({
        "status": "online",
        "projeto": "Transparência Cidadã API",
        "versao": "1.0.0"
    })

@app.route('/api/gerar', methods=['POST'])
def gerar_conteudo():
    # Mantém a funcionalidade do gerador do TikTok!
    data = request.get_json() or {}
    tema = data.get('tema', 'Geral')
    plataforma = data.get('plataforma', 'tiktok')
    
    return jsonify({
        'roteiro': f"[0-3s] GANCHO IMPACTANTE: Pare tudo! Se você busca sobre {tema}, precisa ver isso.\n[3-10s] DESENVOLVIMENTO: Aqui está a principal dica sobre {tema} para aplicar na prática no {plataforma.capitalize()}.\n[10-15s] CHAMADA PRA AÇÃO (CTA): Curta e compartilhe com quem precisa saber disso!",
        'legenda': f"Aprenda tudo sobre {tema}! Dica rápida e prática especialmente para a sua rotina no {plataforma.capitalize()}. 🔥🚀",
        'hashtags': f"#{tema.replace(' ', '')} #DicasVirais #ConteudoViral #{plataforma.capitalize()} #DicasHoje",
        'prompt': f"Ultra-detailed 8k photograph, cinematic lighting, modern showcase of {tema}, vertical 9:16 aspect ratio, trending on social media --v 6.0"
    })

@app.route('/api/simplificar', methods=['POST'])
def simplificar_documento():
    # Nova funcionalidade do Transparência Cidadã!
    data = request.get_json() or {}
    texto_bruto = data.get('texto', '').strip()
    categoria = data.get('categoria', 'licitacao')

    if not texto_bruto:
        return jsonify({'error': 'O texto do documento administrativo é obrigatório.'}), 400

    resumo_cidadao = (
        "Este documento autoriza a prefeitura a realizar a compra/contratação necessária para manter o serviço público ativo. "
        "Em linguagem direta: a administração pública está destinando verba para atender uma demanda essencial da população, "
        "garantindo que os recursos orçamentários sejam aplicados em conformidade com a legislação."
    )

    impacto_social = (
        "Garante a continuidade da prestação de serviços públicos essenciais na comunidade, "
        "reforçando o controle social e a fiscalização direta por parte dos cidadãos."
    )

    recomendacao = (
        "O cidadão pode acompanhar a execução desta despesa através do número do empenho/processo no Portal da Transparência oficial do município ou estado."
    )

    return jsonify({
        'resumo_cidadao': resumo_cidadao,
        'impacto_social': impacto_social,
        'recomendacao_fiscalizacao': recomendacao
    })

if _name_ == '_main_':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
