from django.shortcuts import render

# Create your views here.

def home(request):
    '''
        It serves the index file to the client
    '''
    template = 'index.html'
    context ={}    
    return render(request, template, context)    
