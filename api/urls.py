   
from django.urls import path
from .views import GitAuth, APIStructure
#from .views import PostList, PostDetail

app_name = 'api'
#path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
#path('', PostList.as_view(), name='listcreate'),

urlpatterns = [
    path('', APIStructure.as_view(), name='api-structure'),
    path('auth/', GitAuth.as_view(), name='github-authentication'),
]