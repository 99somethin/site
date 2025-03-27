from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views import View
from article.models import Article
from django.views.decorators.http import require_http_methods

# Create your views here.

class index(View):
    def get(self, request):
        return render(request, 'articles.html', context={
            'team': Article.objects.all(),
        })



class current_index(View):
    require_http_methods = ['get', 'post']

    def get(self, request, name, body):
        current_item = []
        current_item.append(next((item for item in Article.objects.all() if item.name == name),None))
        if all(0 for item in current_item if item == None):
                return render(request, 'articles.html', context={
                     'team': current_item,
                })
        else:
            return redirect('error_404')
        
    def post(self, request, name, body):
        Article.objects.create(name=name, body=body)
        return HttpResponse('good',200)
        
def return_404(request):
     return render(request, 'Http404.html')

        