from django.urls import path

from article import views

urlpatterns = [
    path("", views.index.as_view()),
    path("<str:name>/<int:age>", views.current_index.as_view(), name="current_article"),
]
