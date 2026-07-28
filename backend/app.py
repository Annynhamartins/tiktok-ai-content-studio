import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite que o frontend faça chamadas para o backend

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "projeto": "TikTok-AI Studio API"
    })

@app.route('/api/gerar', methods=['POST'])
def gerar_conteudo():
    data = request.get_json() or {}
    tema = data.get('tema', '').strip()
    plataforma = data.get('plataforma', 'tiktok')

    if not tema:
        return jsonify({'error': 'O parâmetro "tema" é obrigatório.'}), 400

    # Estrutura do prompt / lógica de geração
    roteiro = (
        f"[0-3s] GANCHO IMPACTANTE: Pare tudo! Se você busca sobre {tema}, precisa ver isso.\n"
        f"[3-10s] DESENVOLVIMENTO: Aqui está a principal dica sobre {tema} para aplicar na prática no {plataforma.capitalize()}.\n"
        f"[10-15s] CHAMADA PRA AÇÃO (CTA): Curta e compartilhe com quem precisa saber disso!"
    )

    legenda = (
        f"Aprenda tudo sobre {tema}! Dica rápida e prática especialmente para a sua rotina no {plataforma.capitalize()}. 🔥🚀"
    )

    hashtags = (
        f"#{tema.replace(' ', '')} #DicasVirais #ConteudoViral #{plataforma.capitalize()} #DicasHoje"
    )

    prompt_ia = (
        f"Ultra-detailed 8k photograph, cinematic lighting, modern showcase of {tema}, "
        f"vertical 9:16 aspect ratio, trending on social media --v 6.0"
    )

    return jsonify({
        'roteiro': roteiro,
        'legenda': legenda,
        'hashtags': hashtags,
        'prompt': prompt_ia
    })

if _name_ == '_main_':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
