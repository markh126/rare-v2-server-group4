from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rareapi.views.user_view import UserView
from rareapi.views.rare_user_view import RareUserView
from rareapi.views import PostView
from rareapi.views.auth import check_user, register_user

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserView, 'user')
router.register(r'rare_users', RareUserView, 'rare_user')
router.register(r'posts', PostView, 'post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('checkuser', check_user),
]
