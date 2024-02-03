
from django.shortcuts import render

def portfolio(request):
    return render(request,'home/index.html')
def index_cmd(post):
    return render(post,'home/index_cmd.html')
