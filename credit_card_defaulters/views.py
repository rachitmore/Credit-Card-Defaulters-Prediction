from django.shortcuts import render
from app_tracking.logger import App_Logger
from app_tracking.exception import AppException

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'prediction_templates/index.html')
