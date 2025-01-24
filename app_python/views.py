
from django.shortcuts import render
from django.shortcuts import redirect
import webbrowser

def portfolio(request):
    """ Conexão com diretório

    Returns:
        _render_: _renderiza a página principal no localhost_
        
    """
    input_text=request.POST.get("texto_codigo")
    try:
        if input_text==".help":
            return render(request,"help_python.html")
        elif input_text==".projects":
            return render(request,"projects.html")
        else:
            print("REDIRECIONADO PRA URL FORA")
    except Exception as e:
        print(f"ERRO RENDERIZAR PAGE {e}")
    return render(request, "index.html")
    
    
       

def isDirectHelpPage(request):
    try:
        input_text = request.POST.get('texto_codigo')
        
        if input_text == ".voltar":
            return redirect('portfolio')
        elif input_text ==".projects":
            return redirect('projects')
        else:
            print("Digitou algo errado tente novamente")    
    except Exception as e:
        print(f"Erro ao processar a requisição: {e}")
    return render(request,"help_python.html")

def isDirectProjectsPage(request):
    try:
        input_text = request.POST.get('texto_codigo')
        if input_text==".voltar":
            return redirect('portfolio')
        elif input_text==".help":
            return redirect('help_python')
    except Exception as e:    
        print(f"Erro de requisição {e}")
    return render(request,"projects.html")