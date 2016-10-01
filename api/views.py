from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.views import APIView
import json
# Create your views here.
import requests

def get_headers():
	headers={}
	headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
	headers['Content-Type']="application/json"
	headers['Authorization']="key=AIzaSyBU3fVCZDUHSJbZf28Ar533J2maQPwYSBU"
	return headers

def send_invite(phone,name,table):
	u=Users.objects.get(phone=name).first()
	gcmdata=GCM.objects.filter(u_id=u.u_id).first()
	if gcmdata is not None:
		reg=GCM.regid

		url="https://android.googleapis.com/gcm/send"
		headers=get_headers()
		data={
				"registration_ids":	[reg],
				"data":{"msg":phone+" invited you to join "+table+" group","table":table,'invite':1,'sender':phone}
			}
		res=requests.post(url,data=json.dumps(data),headers=headers)
		result=json.dumps(res.json())
	else:
		result="Not found"	
	return result	



class InviteView(APIView):
	def post(self,request):
		phone=request.POST.get('senders_phone')
		name=request.POST.get('receiver_phone')
		table=request.POST.get('group')
		data=send_invite(phone,name,table)
		return HttpResponse(data)

class ListUserView(APIView):
	def post(self,request):
		name=request.POST.get('group','')
		data=""
		if name=='Family':
			data=Family.objects.all()
		elif name=='Friend':
			data=Friend.objects.all()	
		elif name=='Other':
			data=Other.objects.all()	
		ar=[]	
		for d in data:
			dict={}
			dict['phone']=d.phone
			ar.append(dict)
		return HttpResponse(json.dumps(ar))
		
class AddUserView(APIView):
	def post(self,request):
		name=request.POST.get('group','')
		phone=request.POST.get('phone','')
		if name=='Family':
			data=Family(phone)
			data.save()
		elif name=='Friend':
			data=Friend(phone)	
			data.save()
		elif name=='Other':
			data=Other(phone)
			data.save()
		return HttpResponse('done')		


class GetUserView(APIView):
	def post(self,request):
		phone=request.POST.get('phone','')
		u=Users.objects.get(phone=phone)
		dict={}
		dict["id"]=u.u_id
		return HttpResponse(json.dumps(dict))

class LoginView(APIView):
	def post(self,request):
		phone=request.POST.get('phone','')
		oauth=request.POST.get('oauth','')
		u=Users(phone=phone,oauth=oauth)
		u.save()
		data={'user_id':u.u_id}
		return HttpResponse(json.dumps(data))		
	

class GCMView(APIView):
	def post(self, request):
		regid = request.POST.get('regid','')
		u_id = request.POST.get('u_id','')
		g = GCM(regid=regid, u_id=u_id)
		g.save()
		return HttpResponse("done")
