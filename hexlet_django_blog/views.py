from django.shortcuts import render 
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.shortcuts import redirect

class MainIndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        new_path = reverse('current_article', kwargs={'name': 'anton', 'age': '42'})
        return redirect(new_path)


def about(request):
    return render(request, 'about.html')

