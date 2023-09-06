from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Jason Kent',
        'class': 'PBP F',
    }

    return render(request, "main.html", context)
