
from django.shortcuts import render
from django.shortcuts import redirect


def portfolio(request):
    return render(request,"home/index.html")
    input_text = request.POST.get('texto_codigo')
    if input_text == ".help":
        return redirect("python/help_python.html")
    """ Conexão com diretório

    Returns:
        _render_: _renderiza a página principal no localhost_
    """

def help_python(request):
    """ Transição de diretórios

    Args:
        request (_conexão_): _requisição_

    Returns:
        _render_: _renderizar as páginas que for informado_
    """
    return render(request,"python/help_python.html")