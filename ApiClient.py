import json,httplib

class ApiClient(object):
    VDM_URL="vdm.sdsu.edu"
    POST="POST"
    HEADER={"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    def getFromApi(self,urn,rType,param,mid):
        conn=self.getNewConnection()
        self.sendRequest(conn,urn,rType,param,mid)
        temp=json.loads(conn.getresponse().read())
        if not temp["success"]:
            raise ApiException(temp['error_message'],temp['error_code'])
        return temp["mid"],temp["data"]
    def getNewConnection(self):
        return httplib.HTTPSConnection(self.VDM_URL)
    def sendRequest(self,conn, urn,rType, param, mid):
        temp=self.getQuery(rType,param,mid)
        conn.request(self.POST, urn,self.getQuery(rType,param,mid),self.HEADER)
    def getQuery(self,rType,param,mid):
        return "type="+rType+"&param="+json.dumps(param)+("" if (mid==None) else "&mid="+str(mid))
    def resetURL(self,url):
        this.VDM_URL=url

class ApiException(Exception):
    def __init__(self,msg,code):
        self.msg=msg
        self.code=code
    def __str__(self):
        return repre(self.msg)
