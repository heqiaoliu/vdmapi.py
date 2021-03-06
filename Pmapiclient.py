import ApiClient
################################################################################
# Author: HQ Liu
# Description: Http client for vdm.sdsu.edu/data/api/pmapi.php
# 
################################################################################
class PmapiClient(ApiClient.ApiClient):
	"""
		PmapiClient inheritates ApiClient.
	"""
	URN="/data/api/pmapi.php"
	PM_BACTLIST='getBacteriaList'
	PM_BACTEXP='getBacteriaOfExp'
	PM_BACT='getBacteria'
	PM_EXPLIST='getExperimentList'
	PM_EXP='getExperiment'
	PM_EXPFILE='getExperimentByFile'
	PM_PLATELIST='getPlateList'
	PM_PLATE='getPlate'
	PM_GROWTH='getGrowth'
	NULL_LIST=[]

	#Initialization of the Object
	def __init__(self):
		super(PmapiClient,self).__init__()
	def resetURN(self,urn):	
		self.URN=urn
	def getFromPM(self,rType,param,mid):
		return self.getFromApi(self.URN,rType,param,mid)
	def getBacteriaList(self,mid):
		return self.getFromPM(self.PM_BACTLIST,self.NULL_LIST,mid)
	def getBacteria(self,param,mid):
		return self.getFromPM(self.PM_BACT,param,mid)
	def getBacteriaOfExp(self,param,mid):
		return self.getFromPM(self.PM_BACTEXP,param,mid)
	def getExperimentList(self,mid):
		return self.getFromPM(self.PM_EXPLIST,self.NULL_LIST,mid)
	def getExperiment(self,param,mid):
		return self.getFromPM(self.PM_EXP,param,mid)
	def getExperimentByFile(self,param,mid):
		return self.getFromPM(self.PM_EXPFILE,param,mid)
	def getPlateList(self,mid):
		return self.getFromPM(self.PM_PLATELIST,self.NULL_LIST,mid)
	def getPlate(self,param,mid):
		return self.getFromPM(self.PM_PLATE,param,mid)
	def getGrowth(self,param,mid):
		return self.getFromPM(self.PM_GROWTH,param,mid)
	def getData(self,obj):
		return obj['data']

class PmDataFormatter(PmapiClient):
	def __init__(self):
		super(PmDataFormatter,self).__init__()
	def getCurveSet(self,bid,plateid,wid):
		empty,bactBuffer=self.getBacteria([bid],None)
		bactBuffer=self.getValue(bid,bactBuffer)
		bacteriaId=bactBuffer['bacteria_id']
		empty,expBuffer=self.getExperiment([bacteriaId],None)
		expBuffer=self.getData(self.getValue(str(bacteriaId),expBuffer))
		paramBuffer=[]
		for exp in expBuffer:
			if exp["plate_name"] == plateid:
				paramBuffer.append([exp['experiment_id'],wid])
		empty,curves=self.getGrowth(paramBuffer,None)
		return curves
	def getValue(self,key,obj):
		return obj[key]
