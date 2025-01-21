document.addEventListener('DOMContentLoaded', function () {
    const texto_github = ".github (meu github);";
    const textoElemento = document.getElementById('texto_github');

    function escreverTexto(texto_github, index, intervalo) {
        if (index < texto_github.length) {
            textoElemento.innerHTML += texto_github.charAt(index);
            index++;
            setTimeout(function () {
                escreverTexto(texto_github, index, intervalo);
            }, intervalo);
        }
    }

    // Iniciar a animação quando a página for carregada
    escreverTexto(texto_github, 0, 25);
});
document.addEventListener('DOMContentLoaded', function () {
    const texto_wpp = ".wpp (encaminhar uma mensagem via whatsapp);";
    const textoElemento = document.getElementById('texto_wpp');

    function escreverTexto(texto_wpp, index, intervalo) {
        if (index < texto_wpp.length) {
            textoElemento.innerHTML += texto_wpp.charAt(index);
            index++;
            setTimeout(function () {
                escreverTexto(texto_wpp, index, intervalo);
            }, intervalo);
        }
    }

    // Iniciar a animação quando a página for carregada
    escreverTexto(texto_wpp, 0, 25);
});
document.addEventListener('DOMContentLoaded', function () {
    const texto_linkedin = ".linkedin (redirecionado para meu linkedin);";
    const textoElemento = document.getElementById('texto_linkedin');

    function escreverTexto(texto_linkedin, index, intervalo) {
        if (index < texto_linkedin.length) {
            textoElemento.innerHTML += texto_linkedin.charAt(index);
            index++;
            setTimeout(function () {
                escreverTexto(texto_linkedin, index, intervalo);
            }, intervalo);
        }
    }

    // Iniciar a animação quando a página for carregada
    escreverTexto(texto_linkedin, 0, 25);
});
document.addEventListener('DOMContentLoaded', function () {
    const texto_voltar = ".voltar (digite .voltar para ser redirecionado para página principal).";
    const textoElemento = document.getElementById('texto_voltar');

    function escreverTexto(texto_voltar, index, intervalo) {
        if (index < texto_voltar.length) {
            textoElemento.innerHTML += texto_voltar.charAt(index);
            index++;
            setTimeout(function () {
                escreverTexto(texto_voltar, index, intervalo);
            }, intervalo);
        }
    }

    // Iniciar a animação quando a página for carregada
    escreverTexto(texto_voltar, 0, 25);
});