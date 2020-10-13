from django.urls import path
from . import views

#Definis le nom de mon application 
app_name = 'shop'

#Definis les url pour pouvoir par la suite les appeler sans devoir les taper en dur
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, 
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]