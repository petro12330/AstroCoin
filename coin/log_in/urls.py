# from django.urls import path
#
# from . import views
# from .views import MyRegisterFormView
#
# # urlpatterns = [
# #     path('', views.user_login),
# # ]
#
#
#
#
#
# urlpatterns = [
#     path('', MyRegisterFormView.as_view(), name="register"),
#
# ]
from django.urls import path
from .views import MyRegisterFormView, LoginFormView,LogoutView
urlpatterns = [

    path('register', MyRegisterFormView.as_view(), name="register"),
    path('', LoginFormView.as_view(), name="log_in"),
    path('log_out', LogoutView.as_view(), name="log_out"),
]