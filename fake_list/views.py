from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from datetime import date, datetime, timedelta


# Create your views here.

from django.http import HttpResponse
from fake_list.models import ServerDef
import json
from django.core import serializers

def set_default(obj):
	if isinstance(obj, datetime):
		serial = obj.isoformat()
		return serial

	if isinstance(obj, set):
		return list(obj)
	return str(obj)

def srvlist(request):
	serverSet = ServerDef.objects.all().values()
	dictionaries = [ obj for obj in serverSet ]
	output = {
		'list': dictionaries,
		'total': {
			'clients': len(dictionaries),
			'servers': len(dictionaries),
		},
		'total_max': {
			'clients': len(dictionaries),
			'servers': len(dictionaries),
		},
	}
	return HttpResponse(json.dumps(output, default=set_default), content_type="application/json")


@ensure_csrf_cookie
def announce(request):
	request.encoding='utf-8'
	jsonData = json.loads(request.POST['json'])
	jsonData['ip'] = request.META['REMOTE_ADDR']
	
	checkList = ServerDef.objects.filter(ip=jsonData['ip'], port=jsonData['port'])
	print(checkList)
	if len(checkList) > 0:
		return HttpResponse("boom")

	newData = ServerDef()
	
	newData.name = jsonData['name']
	newData.rollback = jsonData['rollback']
	newData.dedicated = jsonData['dedicated']
	newData.update_time = datetime.now()
	newData.gameid = jsonData['gameid']
	newData.clients_max = jsonData['clients_max']
	newData.proto_min = jsonData['proto_min']
	newData.mapgen = jsonData['mapgen']
	newData.updates = 0
	newData.description = jsonData['description']
	newData.ping = 10.0
	newData.damage = jsonData['damage']
	newData.password = jsonData['password']
	newData.uptime = jsonData['uptime']
	newData.address = jsonData['ip']
	newData.proto_max = jsonData['proto_max']
	newData.game_time = datetime.now()
	newData.mods = json.dumps(jsonData['mods'])
	newData.total_clients = 0
	newData.clients = 0
	newData.version = jsonData['version']
	newData.url = jsonData['url']
	newData.pop_v = 0
	newData.ip = jsonData['ip']
	newData.creative = jsonData['creative']
	newData.start = datetime.now()
	newData.pvp = jsonData['pvp']
	newData.lag = 0
	newData.can_see_far_names = jsonData['can_see_far_names']
	newData.port = jsonData['port']
	newData.clients_top = 0
	newData.privs = jsonData['privs']
	newData.save()
	return HttpResponse("ok")