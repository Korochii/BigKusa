from django.shortcuts import render
from googletrans import Translator
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    return render(request, "home/index.html")

@login_required
def translated(request):
    inputText = request.GET.get('text')
    inputLang = request.GET.get('inLanguage')
    outputLang = request.GET.get('outLanguage')
    tler = Translator()
    outputResult = tler.translate(inputText, outputLang, inputLang) # return type is googletrans.models.Translated
    outputText = outputResult.text
    return render(request, "home/translated.html", {'input': inputText, 'output': outputText})

