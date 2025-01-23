document.addEventListener('DOMContentLoaded', function () {
    const portfolio = "PORTFÓLIO DE IAGO";
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
    setTimeout(function () {
        escreverTexto(portfolio, 0, 90);
    }, 1000);
});
document.addEventListener('DOMContentLoaded', function () {
    var year = 20;

    setInterval(function () {
        var data = new Date();
        if (data.getDate() === 1 && data.getMonth() === 0) {
            year += 1;
        }
    }, 1000);

    const texto = " - Sou um jovem de " + year + " anos, nascido em Joinville (SC), conheço a tecnologia/internet desde meus 7 anos de idade, onde literalmente envelheci com a evolução da internet, em 2022 comecei o meu curso como técnico em desenvolvimento de sistema consegui concluir essa etapa com formação na área e agora busco realizar a minha faculdade de engenharia de software além disso, me pós-graduar em ciência de dados!";
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

    escreverTexto(texto, 0, 25);
});
document.addEventListener('DOMContentLoaded', function () {
    const texto2 = "Tecnologias: Python, Webdev(PHP,JS,HTML,CSS), SQL & Node-red";
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
document.addEventListener('DOMContentLoaded', function () {
    const inputField = document.querySelector('.codigo_input');

    inputField.addEventListener('input', function () {
        const textSize = this.value.length;
        const minWidth = 2;
        const currentWidth = textSize * 8;
        const newWidth = Math.max(minWidth, currentWidth);
        this.style.width = newWidth + 'px';
    });
});
document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('texto_cmd');
    const codigo_input = document.getElementById('codigo_input');

    codigo_input.focus();

    // Adiciona um ouvinte de evento para o evento 'keypress'
    codigo_input.addEventListener('keypress', function (event) {
        // Verifica se a tecla pressionada foi 'Enter' (código de tecla 13)
        if (event.key === 13) {
            // Impede o envio padrão do formulário
            event.preventDefault();
            // Executa a ação desejada, por exemplo, envia o formulário
            form.submit();
        }
    });
});

