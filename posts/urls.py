from django.urls import path
from .views import (
                    PostListView, 
                    PostDetailView,
                    PostCreateView,
                    AboutView,
                    HomeView
                    )


urlpatterns = [
    path('', PostListView.as_view(), name= 'list'),
    path('<int:pk>/', PostDetailView.as_view(), name= 'detail'),
    path('new/', PostCreateView.as_view(), name= 'new'),
    path('about/', AboutView.as_view(), name= 'about'),
    path('home/', HomeView.as_view(), name= 'home'),

]