from django.shortcuts import render
from .logic import historiaclin_logic as hl

# Create your views here.

def historiaclin_view(request):
    if request.method == 'GET':
        historiaclins = hl.get_histoiaclins()