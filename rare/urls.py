from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rareapi.views.rare_user_view import RareUserView
from rareapi.views.post import PostView
from rareapi.views import PostView
from rareapi.views.auth import check_user, register_user
from rareapi.views import SubscriptionView, CommentView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'rare_users', RareUserView, 'rare_user')
router.register(r'subscriptions', SubscriptionView, 'subscription')
router.register(r'posts', PostView, 'post')
router.register(r'comments', CommentView, 'comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('checkuser', check_user),
]
