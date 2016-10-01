from django.conf.urls import url
from api import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.views import APIView

urlpatterns=[
	url(r"^login/$",views.LoginView.as_view(),name="login"),
	url(r"^gcm/$",views.GCMView.as_view(),name="GCM"),
]