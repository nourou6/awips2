##
##

##
# This is a base file that is not intended to be overridden.
##

##
# uengine is deprecated and will be removed from the system soon. Migrate your
# apps to using the Data Access Framework (DAF).
##

#
# Request of Vtec
#
#    
#     SOFTWARE HISTORY
#    
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    04/28/08        1100          bwoodle        Initial Creation.
#    
#



from com.raytheon.edex.uengine.tasks.vtec import VtecEventQuery


class VtecEventRetrieval():
    def __init__(self):
        self.query = VtecEventQuery()
        self.setTimeOut(10)
        
    def execute(self):
        return self.query.execute()
    
    def setFields(self,site,phenom,level):
        self.addField(self.query.SITE, site)
        self.addField(self.query.PHENOM, phenom)
        self.addField(self.query.LEVEL, level)
        
    def addProperty(self,key,value):
        self.query.addProperty(key,value)
        
    def addField(self,name,value):
        self.query.addField(name,value)
        
    def setTimeOut(self,time):
        self.query.setTimeOut(time*1000)
        
    def setClientID(self,clientID):
        self.query.setClientID(clientID)