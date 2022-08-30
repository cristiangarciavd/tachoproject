from django.shortcuts import render
from django.http import HttpResponse
import datetime

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),' # operating sistem. join location of this file + templates folder
)
# Create your views here.
# def index(request):
#     return HttpResponse('Hello!!')

# def index(request):
#     return render(request, 'index.html')

#import datetime to pass variables :)

def index(request):
    today = datetime.datetime.now().date() #example
    return render(request, 'index.html', {"today": today}) # add {variable name: value}
    # remember to parse it to the html!