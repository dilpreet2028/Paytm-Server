from django.conf.urls import url
from api import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.views import APIView

urlpatterns=[
	url(r"^login/$",views.LoginView.as_view(),name="login"),
	url(r"^invite/$",views.InviteView.as_view(),name="invite"),
	url(r"^list_user/$",views.ListUserView.as_view(),name="list user"),
	url(r"^confirm/$",views.AddUserView.as_view(),name="confirm user"),
	url(r"^get_user/$",views.GetUserView.as_view(),name="get user"),
	
	url(r"^gcm/$",views.GCMView.as_view(),name="GCM"),
	url(r"^send_money/$",views.SendView.as_view(),name="send money"),
	url(r"^verify_money/$",views.VerifyView.as_view(),name="verify money"),
	
	
]