from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.views import APIView
# Create your views here.

class LoginView(APIView):
	def post(self,request):
		phone=request.POST.get('phone','')
		oauth=request.POST.get('oauth','')
		u=Users(phone=phone,oauth=oauth)
		u.save()
		return HttpResponse("done")		

class GCMView(APIView):
	def post(self, request):
		regid = request.POST.get('regid','')
		u_id = request.POST.get('u_id','')
		g = GCM(regid=regid, u_id=u_id)
		g.save()
		return HttpResponse("done")

