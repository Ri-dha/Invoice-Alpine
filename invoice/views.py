from django.shortcuts import render


def main(request):
    return render(request, 'invoice/main.html')

# Create your views here.
