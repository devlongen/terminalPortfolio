document.addEventListener('DOMContentLoaded', function () {
    const portfolio = "PORTOFÓLIO DE IAGO";
    const textoElemento = document.getElementById('portfolio');

    function escreverTexto(texto, index, intervalo) {
        if (index < portfolio.length) {
            textoElemento.innerHTML += portfolio.charAt(index);
            index++;
            setTimeout(function () {
                escreverTexto(portfolio, index, intervalo);
            }, intervalo);
        }
    }

    // Iniciar a animação quando a página for carregada
    escreverTexto(portfolio, 0, 90);
});
document.addEventListener('DOMContentLoaded', function () {
    const texto = "Olá! Meu nome é Iago Longen e sou um desenvolvedor backend curioso demais na área da programação. Tenho conhecimentos em várias tecnologias, incluindo Python, Node-RED, MySQL, Javascript e C#. Estou constantemente buscando aprendizado contínuo para aprimorar minhas habilidades e oferecer as melhores soluções para os desafios dos meus projetos. Se você está procurando um profissional comprometido, criativo e dedicado para o seu próximo projeto, fique à vontade para entrar em contato comigo. Explore meu portfólio para ver alguns dos projetos que desenvolvi e entre em contato se tiver alguma dúvida ou oportunidade de colaboração. Estou ansioso para trabalhar juntos!";
    const textoElemento = document.getElementById('texto');

    function escreverTexto(texto, index, intervalo) {
        if (index < texto.length) {
            textoElemento.innerHTML += texto.charAt(index);
            index++;
            setTimeout(function () {
                escreverTexto(texto, index, intervalo);
            }, intervalo);
        }
    }

    // Iniciar a animação quando a página for carregada
    escreverTexto(texto, 0, 25);
});
document.addEventListener('DOMContentLoaded', function () {
    const texto2 = "Tecnologias: Python, Node-RED, MySQL.";
    const textoElemento = document.getElementById('texto2');

    function escreverTexto(texto, index, intervalo) {
        if (index < texto2.length) {
            textoElemento.innerHTML += texto.charAt(index);
            index++;
            setTimeout(function () {
                escreverTexto(texto2, index, intervalo);
            }, intervalo);
        }
    }

    // Iniciar a animação quando a página for carregada
    escreverTexto(texto2, 0, 150);
});
document.addEventListener('DOMContentLoaded', function () {
    const texto3 = "Digite .help para ter acesso as linhas de comando.";
    const textoElemento = document.getElementById('texto3');

    function escreverTexto(texto, index, intervalo) {
        if (index < texto3.length) {
            textoElemento.innerHTML += texto.charAt(index);
            index++;
            setTimeout(function () {
                escreverTexto(texto3, index, intervalo);
            }, intervalo);
        }
    }

    // Iniciar a animação quando a página for carregada
    escreverTexto(texto3, 0, 200);
});
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('texto_cmd');
    const input_text_cmd = document.getElementById('input_text_cmd');
    
    input_text_cmd.focus();

    // Adiciona um ouvinte de evento para o evento 'keypress'
    input_text_cmd.addEventListener('keypress', function(event) {
        // Verifica se a tecla pressionada foi 'Enter' (código de tecla 13)
        if (event.key === 13) {
            // Impede o envio padrão do formulário
            event.preventDefault();
            // Executa a ação desejada, por exemplo, envia o formulário
            form.submit();
        }
    });
});
