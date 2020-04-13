from django.urls import path
from . import views

urlpatterns = [
    path('', views.beforeFT, name='beforeFT'),
    path('beforeFT', views.beforeFT, name='beforeFT'),
    path('afterFT', views.afterFT, name='afterFT'),
    path('requestHtmlSeizure', views.requestHtmlSeizure, name='requestHtmlSeizure'),
    path('requestHtmlNonSeizure', views.requestHtmlNonSeizure, name='requestHtmlNonSeizure'),
    path('requestHtmlSeizureFt', views.requestHtmlSeizureFt, name='requestHtmlSeizureFt'),
    path('requestHtmlNonSeizureFt', views.requestHtmlNonSeizureFt, name='requestHtmlNonSeizureFt'),
]