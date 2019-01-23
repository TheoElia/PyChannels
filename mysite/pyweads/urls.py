from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^product/(?P<pk>[-\w]+)/$', views.ProductDetailView.as_view(), name='product-detail'),
    url(r'^$', views.ProductListView.as_view(), name='products'),
    url(r'^create_product/', views.CreateProductView.as_view(), name='create_product'),
    #url(r'^email_verification/(?P<email_token>[^/]+)/', views.email_verification),
    #url(r'^email_us/', views.email_us),
    #url(r'^create_user/', views.CreateRetailerView.as_view(), name='create_user')
    #path('login/',  views.LoginView.as_view(), name='login'),
]
