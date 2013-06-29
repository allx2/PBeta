import httplib
class RespOk:
	def __init__(self,urli):
		self.urli = urli
		conn = httplib.HTTPConnection(urli)
		conn.request("GET", "/index.html")
		r1 = conn.getresponse()
		#print r1.status
		#print r1.reason
		if r1.status == 302 or 200:
			print "OK"
		else:
			print "Reason " + r1.reason
		data1 = r1.read()
		conn.close()
UnRespOk = RespOk("www.trello.com")


 #falta hacer validaciones y condicionar los codigos de error
 
