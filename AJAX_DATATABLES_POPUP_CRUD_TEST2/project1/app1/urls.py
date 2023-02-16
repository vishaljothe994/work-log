from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('fetch/', views.load_data,name='load_data'),
    path('post-store/', views.PostStore.as_view(),name='post_store'),
    path('post/<int:id>/edit/', views.post_edit,name='post_edit'),
    path('post/<int:id>/delete', views.post_delete,name='post_delete'),
]