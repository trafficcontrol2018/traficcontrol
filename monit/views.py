from django.shortcuts import render
from monit.models import *

def Display_All(request):
	print("working")
	if(request.POST):
		print("post")
		if request.is_ajax():
			print("hi")
			text = request.POST['text']
			print(text)
	try:
		sLog = LogDataMonit.objects.latest("id")
		sData = {'Log':sLog}

	except Exception as e:
		sData = 'Data'
		print(e)
	return render(request,'monit/index.html',{'Data':sData})