async function gerarRoteiro() {
    const inputTema = document.getElementById('tema') || document.querySelector('input') || document.querySelector('textarea');
    const btn = document.getElementById('btnGerar') || document.querySelector('button');
    const boxResultado = document.getElementById('resultado');

    const tema = inputTema ? inputTema.value.trim() : '';

    if (!tema) {
        alert("Por favor, digite um tema ou comentário!");
        return;
    }

    const textoOriginal = btn ? btn.innerText : '';
    if (btn) {
        btn.disabled = true;
        btn.innerText = "⏳ Gerando com IA...";
    }
    
    if (boxResultado) {
        boxResultado.style.display = "none";
    }

    try {
        const response = await fetch('https://tiktok-ai-content-studio.onrender.com/api/gerar-roteiro', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ tema: tema })
        });

        const data = await response.json();

        if (response.ok) {
            const gancho = document.getElementById('res-gancho') || document.getElementById('gancho');
            const conteudo = document.getElementById('res-conteudo') || document.getElementById('conteudo');
            const cta = document.getElementById('res-cta') || document.getElementById('cta');

            if (gancho) gancho.innerText = data.gancho || '';
            if (conteudo) conteudo.innerText = data.conteudo || '';
            if (cta) cta.innerText = data.cta || '';

            if (boxResultado) {
                boxResultado.style.display = "block";
            } else {
                alert("🪝 GANCHO:\n" + data.gancho + "\n\n📝 CONTEÚDO:\n" + data.conteudo + "\n\n📢 CTA:\n" + data.cta);
            }
        } else {
            alert("Erro no servidor: " + (data.error || "Ocorreu um erro ao gerar o roteiro."));
        }
    } catch (error) {
        console.error(error);
        alert("O servidor está conectando (pode levar alguns segundos na primeira vez). Tente clicar novamente!");
    } finally {
        if (btn) {
            btn.disabled = false;
            btn.innerText = textoOriginal || "✨ Gerar Conteúdo";
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const btn = document.getElementById('btnGerar') || document.querySelector('button');
    if (btn) {
        btn.onclick = gerarRoteiro;
    }
});
