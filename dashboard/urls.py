from django.urls import path
from .views import blogView
from .views import authView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', blogView.home, name='home'),
    path('detail/<int:id>', blogView.blog_detail, name='detail'),
    path('comment', blogView.comment, name='comment'),

    path('contact_us', blogView.contact_us, name='contact_us'),
    path('login', authView.login, name='login'),
    path('registration', authView.registration, name='registration'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('create_blog', blogView.create_blog, name='create_blog'),

    path('create_blog_manually', blogView.create_blog_manually, name='create_blog_manually'),

    path('create_blog_ai', blogView.create_blog_ai, name='create_blog_ai'),

]
