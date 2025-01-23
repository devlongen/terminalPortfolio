
from django.shortcuts import render
from django.shortcuts import redirect

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
    except Exception as e:
        print(f"ERRO RENDERIZAR PAGE {e}")
    return render(request, "index.html")
    
    
       

def isDirectHelpPage(request):
    try:
        input_text = request.POST.get('texto_codigo')
        
        if input_text == ".voltar":
            return redirect('portfolio')
        else:
            print("Digitou algo errado tente novamente")    
    except Exception as e:
        print(f"Erro ao processar a requisição: {e}")
    return render(request,"help_python.html")

def isDirectProjectsPage(request):
    
    try:
        input_text = request.POST.get('texto_codigo')
        if input_text==".removeBG":
            return redirect('https://github.com/devlongen/package_Remove')
        elif input_text==".bot_report":
            return redirect('https://github.com/devlongen/bot_report')
        elif input_text==".estoqueSystem":
            return redirect('https://github.com/devlongen/startup_connect')
        elif input_text==".startup_connect":
            return redirect('https://github.com/devlongen/startup_connect')
        elif input_text==".voltar":
            return redirect('portfolio')
    except Exception as e:    
        print(f"Erro de requisição {e}")
    return render(request,"projects.html")