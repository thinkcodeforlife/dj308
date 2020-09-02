from django.urls import path

from . import views

### BLOG URLS ###

app_name = 'blog'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    # path('<int:post_id>/', views.detail, name='detail')
    # path('<int:post_id>/', views.detail_modern, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('edit/<int:post_id>/', views.edit, name='edit'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]