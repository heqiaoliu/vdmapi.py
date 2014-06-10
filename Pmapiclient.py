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
	PM_BACTS='getBacterias'
	PM_EXPS='getExperiments'
	PM_PLATES='getPlates'
	PM_GROWTH='getGrowth'
	NULL_LIST=[]

	#Initialization of the Object
	def __init__(self):
		super(PmapiClient,self).__init__()
	def getBacteriaList(self,mid):
		return self.getFromApi(self.URN,self.PM_BACTLIST,self.NULL_LIST,mid)
	def getBacteriaList(self):
		return self.getFromApi(self.URN,self.PM_BACTLIST,self.NULL_LIST,None)
	def getBacterias(self,param,mid):
		return self.getFromApi(self.URN,self.PM_BACTS,param,mid)
	def getBacterias(self,param):
		return self.getFromApi(self.URN,self.PM_BACTS,param,None)
	def getExperiments(self,param,mid):
		return self.getFromApi(self.URN,self.PM_EXPS,param,mid)
	def getExperiments(self,param):
		return self.getFromApi(self.URN,self.PM_EXPS,param,None)
	def getPlates(self,param,mid):
		return self.getFromApi(self.URN,self.PM_PLATES,param,mid)
	def getPlates(self,param):
		return self.getFromApi(self.URN,self.PM_PLATES,param,None)
	def getGrowth(self,param,mid):
		return self.getFromApi(self.URN,self.PM_GROWTH,param,mid)
	def getGrowth(self,param):
		return self.getFromApi(self.URN,self.PM_GROWTH,param,None)
