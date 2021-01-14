from django.urls import path
from .views import index, by_rubric, by_author
from .views import BbCreateView

urlpatterns = [
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    # path('<str:author_name>/', by_author, name='by_author'),
    path('', index, name='index'),
    path('add/', BbCreateView.as_view(), name='add'),
]

