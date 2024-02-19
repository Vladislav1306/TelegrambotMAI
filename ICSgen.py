from ics import Calendar, Event
from datetime import datetime
import codecs
import shutil
import os
import sqlite3

def del_table():
	connect = sqlite3.connect('BDdiplom.db')
	cursor = connect.cursor()
	request = "DELETE FROM Cal"
	cursor.execute(request)
	connect.commit()
	connect.close()

def add_info(name, text, time, M, d):
	connect = sqlite3.connect('BDdiplom.db')
	cursor = connect.cursor()
	request = "INSERT or REPLACE into Cal(dname, dtext, dtime, M, d) VALUES(?, ?, ?, ?, ?)"
	cursor.execute(request, (name, text, time, M, d))
	connect.commit()
	connect.close()

def write_event(i, M, cy, dtb, dte, day_time, day_inf_event, day_loc, day_text):
	c = Calendar()
	e = Event()
	die = day_inf_event.replace(':', '—')
	e.name = die
	if day_time[3:5] != '':
		e.begin = ''+str(cy)+'-'+M+'-'+i+' '+dtb+':'+day_time[3:5]+':00'
	else:
		e.begin = ''+str(cy)+'-'+M+'-'+i+' '+dtb+':00:00'
	if day_time[9:11] != '':
		e.end = ''+str(cy)+'-'+M+'-'+i+' '+dte+':'+day_time[9:11]+':00'
	else:
		if day_time[3:5] == '':
			e.end = ''+str(cy)+'-'+M+'-'+i+' '+dte+':00:00'
		else:
			e.end = ''+str(cy)+'-'+M+'-'+i+' '+dte+':'+day_time[3:5]+':00'
	e.location = day_loc
	c.events.add(e)
	add_info(die, day_text, i+'-'+M+'-'+str(cy)+' в '+day_time[0:2]+':'+day_time[3:5], M, i)
	#print (day_inf_event)
	with codecs.open('ICS\\'+die+'-'+i+'.'+M+'.ics', 'w', 'utf-8') as f:
		f.writelines(c.serialize_iter())

shutil.rmtree('ICS')
os.mkdir("ICS")

del_table()
cy = datetime.now().year