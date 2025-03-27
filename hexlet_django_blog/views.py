from django.shortcuts import render 
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.shortcuts import redirect

class MainIndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        new_path = reverse('all_articles')
        return redirect(new_path)


def about(request):
    return render(request, 'about.html')

