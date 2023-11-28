from django.shortcuts import render
from django.http import JsonResponse
from .models import Objective
from django.db.models import Q
import json
from .dataset_1 import dataset as dataset_1

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

def createData(request):
    createdData = []
    for i, data in enumerate(dataset_1, start=1): 
        objectiveQuestion = Objective.objects.create(
            year=data.get('year'), 
            instruction=data.get('instruction'),
            subject=data.get('subject'),
            topic=data.get('subject'),
            question_format='objectives',
            content=data.get('question'), 
            number=i, 
            answer=data.get('answer'),
            option_a=data.get('option_a'),
            option_b=data.get('option_b'),
            option_c=data.get('option_c'),
            option_d=data.get('option_d')
        )
        
        objectiveQuestion.save()
        createdData.append(objectiveQuestion.getDict())
    return JsonResponse(data=createdData, safe=False)
    

        
    