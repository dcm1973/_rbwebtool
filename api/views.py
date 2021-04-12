from django.shortcuts import render

# Create your views here.
def BloombergAPI(request):
    return render(request, 'api/bloomberg_api.html', {})
