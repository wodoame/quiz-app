from django.shortcuts import render
from django.http import JsonResponse
from .models import Objective
from django.db.models import Q
import json

# Pages

def testPage(request): 
    return render(request, 'test-page.html', {})

# API 

def getQuestions(request): 
    parameters = request.GET.dict()
    query = Q()
    for param, value in parameters.items(): 
        query &= Q(**{param + '__iexact':value})
    jsonData = []
    questions = Objective.objects.filter(query) if parameters else Objective.objects.all()
    for question in questions: 
        jsonData.append(question.getDict())
    return JsonResponse(data=jsonData, safe=False)

        
    