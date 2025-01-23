document.addEventListener('DOMContentLoaded', function () {
    const texts = [
        { text: ".projects (projetos realizados);", elementId: 'text_projects', interval: 35 },
        { text: ".linkedin (redirecionado para meu linkedin);", elementId: 'texto_linkedin', interval: 35 },
        { text: ".voltar (digite .voltar para ser redirecionado para página principal).", elementId: 'texto_voltar', interval: 35 },
    ];

    function escreverTexto(text, elementId, interval) {
        return new Promise((resolve) => {
            const textoElemento = document.getElementById(elementId);
            let index = 0;

            function escrever() {
                if (index < text.length) {
                    textoElemento.innerHTML += text.charAt(index);
                    index++;
                    setTimeout(escrever, interval);
                } else {
                    resolve();
                }
            }
            escrever();
        });
    }

    async function executarAnimacoes() {
        for (const { text, elementId, interval } of texts) {
            await escreverTexto(text, elementId, interval);
        }
    }

    executarAnimacoes();
});
