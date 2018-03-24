from django.shortcuts import render
from services.models import *
from monit.models import *
import datetime
import pprint
from django.utils import timezone

def Value_To_Hex_String(sString):
	if(len(sString) < 4):
		if(len(sString) == 3):
			sString = "0" + sString
		if(len(sString) == 2):
			sString = "00" + sString
		if(len(sString) == 1):
			sString = "000" + sString
	return sString

def Store_Packet_Monit(sPingPacket):
	#print(sPingPacket)
	sError = "None"
	if(sPingPacket[0] == '*' and sPingPacket[-1] == '!'):
		#print("Correct packet")
		sPingPacket = sPingPacket[1:]
		sPingPacket = sPingPacket[:-1]
		#print(sPingPacket)

		#skipping first packet 
		sPingPacket = sPingPacket[sPingPacket.index(',') + 1:]
		#print(sPingPacket)

		#skipping second packet
		sPingPacket = sPingPacket[sPingPacket.index(',') + 1:]
		#print(sPingPacket)

		# Get packet id and number of sensor followed by
		sCode = sPingPacket[:sPingPacket.index(',')]
		#print(sCode)
		sPingPacket = sPingPacket[sPingPacket.index(',') + 1:]
		#print(sPingPacket)
		
		#Get TrafficState
		sTrafficState = sPingPacket[:sPingPacket.index(',')]
		#print(sTrafficState)
		ui16TrafficState = int(sTrafficState,16)
		sPingPacket = sPingPacket[sPingPacket.index(',') + 1:]
		#print(sPingPacket)

		#Get Ultrasonic state
		sUSState = sPingPacket[:sPingPacket.index(',')]
		#print(sUSState)
		ui16USState = int(sUSState,16)
		sPingPacket = sPingPacket[sPingPacket.index(',') + 1:]
		#print(sPingPacket)

		sTimeNow = timezone.now()
		sDObject = LogDataMonit(dbLogTime = sTimeNow, dbTrafficState = ui16TrafficState, dbUSState = ui16USState)
		sDObject.save()
		return 1
	else:
		print("Invalid packet")
		return 0

def Response_Packet():
	sData = LogUserDataMonit.objects.latest("id")
	sString = "*000103,010400012C03000000,0101,0001,0!"
	
	return sString

def Ping_Packet(request):
	sPingPacket = request.GET.get('pkt','')
	sString = "*000000,000000000000000000,0000!"
	try:
		sDBObjects = Ping(dbPacket=sPingPacket)
		sDBObjects.save()
		ui8Response = Store_Packet_Monit(sPingPacket)
		sString = Response_Packet()

	except Exception as e:
		print("Ping Error " + str(e))
		sErrorLog = ErrorLog(dbError=e, dbErrorCode = "ErrorCode")

	return HttpResponse(sString)
