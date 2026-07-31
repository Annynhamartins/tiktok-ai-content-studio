import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq

app = Flask(__name__)
CORS(app)

# Configura a chave da API da Groq
api_key = os.environ.get('GROQ_API_KEY')
client = Groq(api_key=api_key) if api_key else None

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "projeto": "TikTok AI Studio API",
        "status": "online"
    })

@app.route('/api/gerar-roteiro', methods=['POST'])
def gerar_roteiro():
    try:
        data = request.get_json()
        tema = data.get('tema', '')
        tipo = data.get('tipo', 'roteiro') # 'roteiro' ou 'resposta_comentario'

        if not tema:
            return jsonify({'error': 'Nenhum tema ou comentário fornecido'}), 400

        if not client:
            return jsonify({
                'gancho': 'Erro: Chave GROQ_API_KEY não configurada no Render.',
                'conteudo': 'Configure a variável no painel do Render.',
                'cta': 'Verifique as configurações do projeto.'
            }), 500

        prompt = f"""
        Você é um especialista em criação de conteúdo viral para TikTok e Shorts.
        Crie um ROTEIRO DE VÍDEO CURTO (até 60 segundos) altamente engajador sobre o seguinte tema/comentário:
        
        TEMA/COMENTÁRIO:
        \"\"\"{tema}\"\"\"

        O tom deve ser dinâmico, direto ao ponto e persuasivo.
        Responda ESTRITAMENTE em formato JSON com as 3 chaves exatas abaixo:
        {{
            "gancho": "Frase impactante de 3 a 5 segundos para prender a atenção nos primeiros instantes.",
            "conteudo": "Desenvolvimento do vídeo em tópicos curtos e práticos, fácil de ler/gravar.",
            "cta": "Uma chamada para ação poderosa (ex: curtir, comentar, seguir ou clicar no link)."
        }}
        """

        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            response_format={"type": "json_object"}
        )

        resultado = json.loads(response.choices[0].message.content)
        return jsonify(resultado)

    except Exception as e:
        return jsonify({
            'gancho': f'Erro ao processar com a IA: {str(e)}',
            'conteudo': 'Tente novamente em instantes.',
            'cta': 'Verifique o tema enviado.'
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
