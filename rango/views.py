from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #construct a dictionary to pass the template engine as its context.
    #note the key boldmessage matches to {{  boldmessage  }} in the template!
    context_dict = {'boldmessage':'Crunchy, creamy, cookie, candy, cupcake!'}

    #return a rendered response to the client
    #we make use of the shortcuut function t make our lives easier.
    #note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    # return a rendered response to the client
    # we make use of the shortcut function to make our lives easier.
    # note that the first parameter is the template we wish to use.
    return render(request, 'rango/about.html')

