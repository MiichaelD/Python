'''

Program:	RegistroDelconsumidor.py

Description:	Program which unsubscribes all cellphone numbers from given area code (lada) from annoying sms ads
		using http://repep.profeco.gob.mx/registrar_telefono.jsp 's service

More Info:	http://repep.profeco.gob.mx/index.jsp 
		REPEP REgistro Publico para Evitar Publicidad => Public registry to avoid ads
		https://www.facebook.com/Frontera.info/videos/10153530275841961/ 
		https://www.youtube.com/watch?v=7TW4lNE45hk

Date:			April 13th, 2016
'''

import httplib, urllib
import time
headers = {'Host':'repep.profeco.gob.mx',
			'Content-Type':'application/x-www-form-urlencoded',
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Referer':'http://repep.profeco.gob.mx/registrar_telefono.jsp'
		 	}

payload_format = "Usuario=CONSUMIDOR&lada={}&phone={}&phonee={}{}&ext=&checkbox1=Comercio&checkbox2=Telecomunicaciones\
			&checkbox3=Tur%EDstico&Nsector=3&Pagina=1&telefono=&Submit=Aceptar"
host = "repep.profeco.gob.mx" # NO 'protocol://'
port = '80'
strict = False
timeout = 15 #secs
sleep_time = 5
receiver_script = '/RegistroConsumidor'

lada = '686'
for i in range(1000000,9999999):
	phone = format(i, '07')
	payload = payload_format.format(lada, phone, lada, phone)
	while True:
		try:
			conn = httplib.HTTPConnection(host, port, strict, timeout)
			conn.request("POST", receiver_script, payload, headers)
			response = conn.getresponse()
			data = response.read()
			print lada+phone, ': ', response.status, response.reason, data

			if len(data) > 0:
				break;

			print '\tEmpty data, trying again...'
			time.sleep(sleep_time)
				
		except Exception as e:
			print '\tThere was an exception: {}, trying again...'.format(e);
			time.sleep(sleep_time)


'''
curl -X POST --proxy "http://127.0.0.1:8888" -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36" -H "Host:repep.profeco.gob.mx" -H "Content-Type:application/x-www-form-urlencoded" \
-H "Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8" -H "Referer:http://repep.profeco.gob.mx/registrar_telefono.jsp" \
-d "Usuario=CONSUMIDOR&lada=686&phone=9999999&phonee=6869999999&ext=&checkbox1=Comercio&checkbox2=Telecomunicaciones&\
checkbox3=Tur%EDstico&Nsector=3&Pagina=1&telefono=&Submit=Aceptar" http://repep.profeco.gob.mx/RegistroConsumidor


'''
