
from django.shortcuts import render
from django.shortcuts import redirect

def portfolio(request):
    """ Conexão com diretório

    Returns:
        _render_: _renderiza a página principal no localhost_
    """
    try:
        input_text = request.POST.get('texto_codigo')
        if input_text == ".help":
            return redirect('help_python')
    except Exception as e:
        print(f"Erro ao processar a requisição: {e}")
        return render(request, "home/index.html")

def help_python(request):
    """ Transição de diretórios

    Args:
        request (_conexão_): _requisição_

    Returns:
        _render_: _renderizar as páginas que for informado_
    """
    return render(request,"python/help_python.html")