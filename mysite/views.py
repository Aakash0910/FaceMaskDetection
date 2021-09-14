from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request , 'index.html')

def analyze(request):
    # POST IS USED WHEN TEXT IS TOO LONG
    # djtext = request.GET.get('text','default')
    djtext = request.POST.get('text','default')

    # Check the checkbox value
    removepunc = request.POST.get('removepunc','off')
    fullcap = request.POST.get('fullcap','off')
    newlineremover = request.POST.get('newlineremover','off')
    import string

    # Removing punctuations
    if removepunc == "on":
        punctuation = string.punctuation
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char 
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
    
    # UPPERCASE
    if fullcap == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'UPPERCASE','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)

    # New Line Remover
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose':'New Line Removed','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)

    # else:
    #     return HttpResponse("Error") 
    if newlineremover != 'on' and fullcap != 'on' and removepunc != 'on':
        return HttpResponse('Error')
    
    return render(request , 'analyze.html' , params)

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("new line remove")

# def spaceremove(request):
#     return HttpResponse("space remover")

# def charcount(request):
#     return HttpResponse("charcount ")