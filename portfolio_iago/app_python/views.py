
from django.shortcuts import render
from django.shortcuts import redirect


def portfolio(request):
    return render(request,'home/index.html')
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
    tratativa_dados = request.POST.get('texto_codigo') 
    if tratativa_dados == '.help':
        return render(request, 'python/help_python.html')
    elif tratativa_dados == '.cd python_prog':
        return redirect('https://github.com/devlongen/python_prog')
    elif tratativa_dados == '.linkedin':
        return redirect('https://www.linkedin.com/in/iagolongen/')
    elif tratativa_dados == '.wpp':
        return redirect('https://wa.me/5547988071571')
    elif tratativa_dados == '.github':
        return redirect('https://github.com/devlongen')
    else:
        return render(request,'home/index.html')