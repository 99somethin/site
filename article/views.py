from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

class index(View):
    TEAM = [
        {'name': 'petya', 'age': '18'},
        {'name': 'misha', 'age': '28'}
    ]

    def get(self, request):
        return render(request, 'articles.html', context={
            'team': self.TEAM
        })
