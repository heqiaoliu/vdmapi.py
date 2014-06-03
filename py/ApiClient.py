import json,httplib

class ApiClient(object):
	VDM_URL="vdm.sdsu.edu"
	POST="POST"
	HEADER = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	def getFromApi(self,urn,rType,param,mid):	
		conn=self.getNewConnection()
		self.sendRequest(conn,urn,rType,param,mid)
		return json.loads(conn.getresponse().read())
	def getNewConnection(self):
		return httplib.HTTPConnection(self.VDM_URL)
	def sendRequest(self,conn, urn,rType, param, mid):
		temp=self.getQuery(rType,param,mid)
		print temp
		conn.request(self.POST, urn,self.getQuery(rType,param,mid),self.HEADER)
	def getQuery(self,rType,param,mid):
		return "type="+rType+"&param="+json.dumps(param)+("" if (mid==None) else "&mid="+str(mid))
			