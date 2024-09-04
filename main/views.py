from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306171480',
        'name': 'Chiara',
        'class': 'KKI'
    }

    return render(request, "main.html", context)
