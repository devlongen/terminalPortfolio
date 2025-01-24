document.addEventListener('DOMContentLoaded', function () {
    const texts = [
        { text: "Esses projetos foram realizados por mim, onde eu tenho grande satisfação em apresentar-los.", elementId: 'text_project', interval: 25 },
        { text: ".removeBG, removedor de fundo via Python.", elementId: 'text_removeBG', interval: 35 },
        { text: ".bot_report, bot que extraia dados e mandava automaticamente para googledrive.", elementId: 'text_botReport', interval: 35 },
        { text: ".estoqueSystem, sistema de estoque.", elementId: 'text_estoque', interval: 35 },
        { text: ".startup_connect, sistema para uma empresa de gerenciamento de startups.", elementId: 'text_startupConnect', interval: 35 },
        { text: ".pokemon-api, utilização de api do pokemon para fins academicos, além disso tem como jogar também.", elementId: 'text_pokemon-api', interval:35}
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
