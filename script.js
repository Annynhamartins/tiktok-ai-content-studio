document.addEventListener('DOMContentLoaded', () => {
    // Procura os elementos na tela
    const btnGerar = document.getElementById('btnGerar') || document.querySelector('button');
    const inputTema = document.getElementById('tema') || document.querySelector('input') || document.querySelector('textarea');

    if (btnGerar) {
        btnGerar.addEventListener('click', async (e) => {
            e.preventDefault();

            const tema = inputTema ? inputTema.value.trim() : '';

            if (!tema) {
                alert('Por favor, digite um tema ou comentário!');
                return;
            }

            const textoOriginal = btnGerar.innerText;
            btnGerar.disabled = true;
            btnGerar.innerText = '⏳ Gerando com IA...';

            try {
                // Conecta com o backend do TikTok no Render
                const response = await fetch('https://tiktok-ai-content-studio.onrender.com/api/gerar-roteiro', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ tema: tema })
                });

                const data = await response.json();

                if (response.ok) {
                    // Exibe os resultados nos campos da tela
                    const boxGancho = document.getElementById('res-gancho') || document.getElementById('gancho');
                    const boxConteudo = document.getElementById('res-conteudo') || document.getElementById('conteudo');
                    const boxCta = document.getElementById('res-cta') || document.getElementById('cta');

                    if (boxGancho) boxGancho.innerText = data.gancho || '';
                    if (boxConteudo) boxConteudo.innerText = data.conteudo || '';
                    if (boxCta) boxCta.innerText = data.cta || '';

                    // Se não houver caixas separadas, mostra um alerta com o resultado
                    if (!boxGancho && !boxConteudo) {
                        alert(🪝 GANCHO:\n${data.gancho}\n\n📝 CONTEÚDO:\n${data.conteudo}\n\n📢 CTA:\n${data.cta});
                    }
                } else {
                    alert('Erro no servidor: ' + (data.error || 'Ocorreu um erro ao processar.'));
                }
            } catch (error) {
                console.error(error);
                alert('Não foi possível conectar ao servidor. O servidor pode estar inicializando (leva cerca de 30s na primeira vez). Tente novamente!');
            } finally {
                btnGerar.disabled = false;
                btnGerar.innerText = textoOriginal;
            }
        });
    }
});
