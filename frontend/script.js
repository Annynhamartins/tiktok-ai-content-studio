ocument.getElementById('btnGerar').addEventListener('click', async function() {
    const tema = document.getElementById('tema').value.trim();
    const plataforma = document.getElementById('plataforma').value;
    const btn = document.getElementById('btnGerar');

    if (!tema) {
        alert("Por favor, digite um tema ou produto!");
        return;
    }

    btn.innerText = "⏳ Gerando com IA...";
    btn.disabled = true;

    try {
        // Conecta diretamente ao seu servidor online no Render
        const response = await fetch('https://tiktok-ai-content-studio.onrender.com/api/gerar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ tema: tema, plataforma: plataforma })
        });

        if (!response.ok) {
            throw new Error("Erro ao se comunicar com o servidor.");
        }

        const data = await response.json();

        // Exibe os resultados no painel
        document.getElementById('outRoteiro').innerText = data.roteiro;
        document.getElementById('outLegenda').innerText = data.legenda;
        document.getElementById('outHashtags').innerText = data.hashtags;
        document.getElementById('outPrompt').innerText = data.prompt;

        document.getElementById('resultado').classList.remove('hidden');
    } catch (error) {
        alert("Não foi possível conectar ao servidor. Aguarde alguns instantes e tente novamente.");
        console.error(error);
    } finally {
        btn.innerText = "✨ Gerar Conteúdo Completo";
        btn.disabled = false;
    }
});
