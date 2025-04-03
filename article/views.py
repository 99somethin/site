from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import View
from django.urls import reverse
from article.models import Article, ArticleComment
from article.forms import CommentArticleForm

# Create your views here.

class index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'articles.html', context={
            'articles': Article.objects.all(),
        })



class current_index(View):
    require_http_methods = ['get', 'post']

    def get(self, request, name, body):
        current_item = []
        current_item.append(next((item for item in Article.objects.all() if item.name == name),None))
        if all(0 for item in current_item if item == None):
                return render(request, 'articles.html', context={
                     'articles': current_item,
                })
        else:
            return redirect('error_404')
        
    def post(self, request, name, body):
        Article.objects.create(name=name, body=body)
        return HttpResponse('good',200)



class ArticleId(View):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        try:
            article = get_object_or_404(Article, id=kwargs['id'])
        except Http404:
            return render(request, 'Http404.html')
        
        return render(request, 'articleID.html', context={
             'articles': article
        })
        
def return_404(request):
     return render(request, 'Http404.html')

class CommentArticle(View):
    http_method_names = ['get', 'post']

    def post(self, request, *args, **kwargs):
        article = Article.objects.get() 
        form = CommentArticleForm(request.POST)
        
        if form.is_valid():
            ArticleComment.objects.create(content=form.cleaned_data["content"], article=article)
            return redirect(reverse("article_detail")) 

    def get(self, request, *args, **kwargs):
        form = CommentArticleForm()
        return render(request, 'addArticleComment.html', {'form': form})

        