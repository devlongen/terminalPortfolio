document.addEventListener('DOMContentLoaded', function () {
    const text_project = "Esses projetos foram realizados por mim, onde eu tenho grande satisfação em apresentar-los.";
    const textoElemento = document.getElementById('text_project');

    function escreverTexto(text_project, index, intervalo) {
        if (index < text_project.length) {
            textoElemento.innerHTML += text_project.charAt(index);
            index++;
            setTimeout(function () {
                escreverTexto(text_project, index, intervalo);
            }, intervalo);
        }
    }

    escreverTexto(text_project, 0, 25);
});
document.addEventListener('DOMContentLoaded', function () {
    const text_removeBG = ".removeBG, Removedor de fundo via Python";
    const textoElemento = document.getElementById('text_removeBG');

    function escreverTexto(text_removeBG, index, intervalo) {
        if (index < text_removeBG.length) {
            textoElemento.innerHTML += text_removeBG.charAt(index);
            index++;
            setTimeout(function () {
                escreverTexto(text_removeBG, index, intervalo);
            }, intervalo);
        }
    }

    // Iniciar a animação quando a página for carregada
    escreverTexto(text_removeBG, 0, 25);
});
