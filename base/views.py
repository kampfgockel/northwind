from django.shortcuts import render

def error_403_view(request, exception=None):
    return render(request, '403.html', status=403)

def error_404_view(request, exception=None):
    return render(request, '404.html', status=404)

def error_500_view(request, exception=None):
    return render(request, '500.html', status=500)