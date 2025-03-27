from django.urls import path

from article import views

urlpatterns = [
    path("", views.index.as_view(), name='all_articles'),
    path('404page/', views.return_404, name='error_404'),
    path("<str:name>/<str:body>", views.current_index.as_view(), name="current_article"),
]
