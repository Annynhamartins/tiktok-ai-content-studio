document.getElementById('btnGerar').addEventListener('click', async function() {
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
        // Envia requisição para o backend
        const response = await fetch('http://127.0.0.1:5000/api/gerar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ tema: tema, plataforma: plataforma })
        });

        if (!response.ok) {
            throw new Error("Erro na comunicação com o servidor.");
        }

        const data = await response.json();

        // Exibe os dados retornados pela API
        document.getElementById('outRoteiro').innerText = data.roteiro;
        document.getElementById('outLegenda').innerText = data.legenda;
        document.getElementById('outHashtags').innerText = data.hashtags;
        document.getElementById('outPrompt').innerText = data.prompt;

        document.getElementById('resultado').classList.remove('hidden');
    } catch (error) {
        alert("Não foi possível conectar ao backend local. Verifique se o servidor Flask está rodando.");
        console.error(error);
    } finally {
        btn.innerText = "✨ Gerar Conteúdo Completo";
        btn.disabled = false;
    }
});
