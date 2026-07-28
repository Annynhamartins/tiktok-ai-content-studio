document.getElementById('btnGerar').addEventListener('click', function() {
    const tema = document.getElementById('tema').value.trim();
    const plataforma = document.getElementById('plataforma').value;

    if (!tema) {
        alert("Por favor, digite um tema ou produto!");
        return;
    }

    // Exibe o painel de resultados
    document.getElementById('resultado').classList.remove('hidden');

    // Simulação inicial de geração de conteúdo
    document.getElementById('outRoteiro').innerText = [0-3s] Gancho: Você não vai acreditar no que acontece quando acerta o foco em ${tema}!\n[3-10s] Corpo: Aqui está o segredo que ninguém te conta para ter resultados rápidos...\n[10-15s] CTA: Curta e siga para mais dicas!;
    
    document.getElementById('outLegenda').innerText = Descubra a melhor forma de dominar ${tema}! Dica rápida e prática para aplicar hoje mesmo. 🔥🚀;
    
    document.getElementById('outHashtags').innerText = #${tema.replace(/\s+/g, '')} #DicasVirais #Trending #ContentCreator #${plataforma};
    
    document.getElementById('outPrompt').innerText = Cinematic lighting, high-detail showcase of ${tema}, 8k resolution, vibrant color palette, vertical 16:9 aspect ratio --v 6.0;
});
