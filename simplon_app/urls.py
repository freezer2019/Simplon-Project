from django.urls import path, include
from . import views
from .import HodViews, StaffViews


urlpatterns = [
    path('', views.loginPage, name="login"),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('doLogin/', views.doLogin, name="doLogin"),
    path('get_user_details/', views.get_user_details, name="get_user_details"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('admin_home/', HodViews.admin_home, name="admin_home"),
    path('add_participant/', HodViews.add_participant, name="add_participant"),
    path('add_participant_save/', HodViews.add_participant_save, name="add_participant_save"),
    path('manage_participant/', HodViews.manage_participant, name="manage_participant"),
    path('edit_participant/<participant_id>/', HodViews.edit_participant, name="edit_participant"),
    path('edit_participant_save/', HodViews.edit_participant_save, name="edit_participant_save"),
    path('delete_participant/<participant_id>/', HodViews.delete_participant, name="delete_participant"),
    path('admin_profile/', HodViews.admin_profile, name="admin_profile"),
    path('admin_profile_update/', HodViews.admin_profile_update, name="admin_profile_update"),
    path('check_email_exist/', HodViews.check_email_exist, name="check_email_exist"),
    path('check_username_exist/', HodViews.check_username_exist, name="check_username_exist"),
]