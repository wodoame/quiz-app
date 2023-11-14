from django.urls import path
import core.views as core_views 

urlpatterns = [
    path('test/', core_views.testPage, name='test-page'), 
    path('get-questions/', core_views.getQuestions, name='get-questions')
]

