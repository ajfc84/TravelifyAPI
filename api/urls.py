from django.urls import  path

from .views import ItemList, ItemDetail

urlpatterns = [
    path('<int:pk>/', ItemDetail.as_view()),
    path('', ItemList.as_view()),
]

