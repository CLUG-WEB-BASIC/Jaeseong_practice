from django.shortcuts import render

def home(request) :
    #이 자리에 모델을 다루는 코드가 들어감.
    return render(request, 'home.html')
