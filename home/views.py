from django.shortcuts import render
from googletrans import Translator

# Create your views here.

def index(request):
    return render(request, "home/index.html")

def translated(request):
    inputText = request.GET.get('text')
    inputLang = request.GET.get('inLanguage')
    outputLang = request.GET.get('outLanguage')
    tler = Translator()
    outputResult = tler.translate(inputText, outputLang, inputLang) # return type is googletrans.models.Translated
    outputText = outputResult.text
    return render(request, "home/translated.html", {'input': inputText, 'output': outputText})
