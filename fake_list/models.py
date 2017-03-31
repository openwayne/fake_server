from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ServerDef(models.Model):
	name = models.CharField(max_length=1024) #"Switchboard PVP made by yngwie123"
	rollback = models.BooleanField() #true
	dedicated = models.BooleanField() #true
	update_time = models.TimeField()
	gameid = models.CharField(max_length=1024) #"switchboardpvp"
	clients_max = models.IntegerField()
	proto_min = models.IntegerField()
	mapgen = models.CharField(max_length=128) #"v6"
	updates = models.IntegerField()
	description = models.TextField() #"This server is hosted by DI3HARD139"
	ping = models.FloatField()
	damage = models.BooleanField() #true
	password = models.BooleanField() #false
	uptime = models.IntegerField()
	address = models.CharField(max_length=2048) #"rrhgameservers.ddns.net"
	proto_max = models.IntegerField()
	game_time = models.TimeField()
	mods = models.TextField() #[]
	total_clients = models.IntegerField()
	clients = models.IntegerField()
	version = models.CharField(max_length=256) #"0.4.14-BiteMe"
	url = models.CharField(max_length=256) #""
	pop_v = models.FloatField()
	ip = models.GenericIPAddressField() #"2607:5300:60:4e5::1"
	creative = models.BooleanField() #false
	start = models.TimeField()
	pvp = models.BooleanField() #true
	lag = models.FloatField()
	can_see_far_names = models.BooleanField() #true
	port = models.IntegerField()
	clients_top = models.IntegerField()
	privs = models.TextField() #"interact shout home"
