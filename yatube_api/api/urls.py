from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
from .views import (PostViewSet, CommentViewSet, FollowViewSet,
                    GroupViewSet, UserViewSet)


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'follow', FollowViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('djoser.urls.jwt')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
