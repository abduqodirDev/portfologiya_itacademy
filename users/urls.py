from django.urls import path, include
from .views import Profiles, profile, login_user, logout_user, register_user,\
    my_account, profile_change, skill_add, skill_change, skill_delete, message,\
    message_all, search_result
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView,\
PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
PasswordResetCompleteView

urlpatterns = [
    path("", Profiles, name="profiles"),
    path("search_result/", search_result, name="search_result"),
    path("profile/<uuid:id>/", profile, name="profile"),
    path("profile/<uuid:id>/message/", message, name="message"),
    path("profile/<uuid:id>/message-all", message_all, name="message_all"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("register/", register_user, name="register"),
    path("account/", my_account, name="account"),
    path("account/change/", profile_change, name="profile_change"),
    path("account/change/password-change/", PasswordChangeView.as_view(), name="password_change"),
    path("account/change/password-change/done/", PasswordChangeDoneView.as_view(), name="password_change_done"),
    path("account/change/password-reset/", PasswordResetView.as_view(), name="password_reset"),
    path("account/change/password-reset/done/", PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("account/change/password-reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("account/change/password-reset/complete/", PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path("account/skill-add/", skill_add, name="skill_add"),
    path("account/skill-change/<uuid:id>/", skill_change, name="skill_change"),
    path("account/skill-delete/<uuid:id>/", skill_delete, name="skill_delete")
    ]