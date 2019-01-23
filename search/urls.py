from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('products', views.ProductView)

urlpatterns = [
    path('', views.get_results, name='gifther-home'),
    path('search/', views.get_results),
    path('api/', include(router.urls)),
    path('do_vote/', views.do_vote),
]
