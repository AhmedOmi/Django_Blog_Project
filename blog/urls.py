from django.urls import path
from .views import Home_view, List_view, Detail_view

urlpatterns = [
    path('', Home_view, name="home"),
    path('storys/', List_view, name='storys'),
    path('storys/<int:pk>/', Detail_view.as_view(), name='detail')
]
