from django.shortcuts import render
from googletrans import Translator
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from home.models import Entry
import datetime
from django.utils.timezone import utc

# Create your views here.

@login_required
def index(request):
    return render(request, "home/index.html")

@login_required
def translated(request):
    user = request.user # Retrieve user id
    inputText = request.GET.get('text').lower()
    inputLang = request.GET.get('inLanguage')
    outputLang = request.GET.get('outLanguage')
    tler = Translator()
    outputResult = tler.translate(inputText, outputLang, inputLang) # return type is googletrans.models.Translated
    outputText = outputResult.text
    language = inputLang + ' -> ' + outputLang
    updatedFrequency = int() # Instantiate counter variable to be passed into context
    # ifExist returns a boolean value depending on whether the entry is already in the database
    exist = Entry.objects.filter(input_text=inputText, output_text=outputText, language=language, user=user).exists()
    if (exist):
        item = Entry.objects.get(input_text=inputText, output_text=outputText, language=language, user=user)
        item.frequency += 1
        updatedFrequency = item.frequency
        item.save()
    else: 
        new_entry = Entry()
        new_entry.user = user
        new_entry.input_text = inputText
        new_entry.output_text = outputText
        new_entry.language = language
        new_entry.frequency = 1
        updatedFrequency = 1
        new_entry.save()
    context = {
        'owner' : user,
        'input_text' : inputText,
        'output_text' : outputText,
        'language' : language,
        'frequency' : updatedFrequency
    }
    return render(request, "home/translated.html", context)

