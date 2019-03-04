##
##


import PointDataView, PointDataContainer, NoDataException

#
# Python module to request point data.  Split out of PointDataContainer.py.
#  
#    
#  SOFTWARE HISTORY
#  
#  Date            Ticket#       Engineer       Description
#  ------------    ----------    -----------    --------------------------
#  05/11/11                      njensen        Initial Creation.
#  25Apr2012       14688         rferrel        Made into an abstract class.
#  Sep 14, 2015    4880          njensen        Improved __queryNewestRefTime()
#    
# 
#
    
##
# This is a base file that is not intended to be overridden.
##

class PointDataRetrieve(object):
    def __init__(self, pluginName, site, parameters, keyId='forecastHr', refTime=None, constraint={}, maxSize=99):
        """Initializes a python PointDataContainer which wraps the Java PointDataContainer capabilities.
            @pluginName the name of the type of data, e.g. bufrmos
            @site the name of the station, e.g. KOMA
            @parameters a python list of parameter names as specified in the pointdata xml
            @keyId how to organize views into the point data, defaults to forecastHr
            @refTime the reference time to request data for, if None will default to the newest time
            @constraint a dictionary of extra string constraints to narrow the data type returned,
                                e.g. {'type':'LAMP'}
        """

        self.pluginName = pluginName
        self.site = site
        self.constraint = constraint
        if not refTime:
            refTime = self.__queryNewestRefTime()
            import time
            if refTime < time.time() - 86400:
                raise NoDataException.NoDataException("Newest data in system is more than 24 hours old")
        if type(refTime) is int or type(refTime) is long:
            from java.util import Date
            refTime = Date(refTime * 1000)
        self.refTime = refTime # should be a java.util.Date
        if type(parameters) is str:
            parameters = [parameters]
        if not parameters.__contains__(keyId):
            parameters.append(keyId)
        self.__keyId = keyId
        self._query(parameters, int(maxSize))
    
    # Abstract method must be implemented by sub-class.
    def _query(self, parameters, maxSize):
        raise NoDataException.NoDataException('_query not implemented')
    
    def __queryNewestRefTime(self):
        from com.raytheon.uf.viz.core.catalog import CatalogQuery
        constraints = self._buildConstraints()
        results = CatalogQuery.performTimeQuery(constraints, True, None)
        nResults = len(results)
        if nResults != 1:
            if nResults > 1:
                # this should be impossible to hit unless CatalogQuery is broken
                raise NoDataException.NoDataException("Unable to determine latest time, received multiple times")
            elif self.site:
                raise NoDataException.NoDataException("No data available for site " + self.site)
            else:
                raise NoDataException.NoDataException("No data available")
        dt = results[0]
        return dt.getRefTime().getTime() / 1000
    
    def _buildConstraints(self, refTime=None):
        from java.util import HashMap
        from com.raytheon.uf.common.dataquery.requests import RequestConstraint
        queryTerms = HashMap()
        queryTerms.put("pluginName", RequestConstraint(self.pluginName))
        if self.site:
            queryTerms.put("location.stationId", RequestConstraint(self.site))
        if refTime:
            from com.raytheon.uf.common.time.util import TimeUtil 
            queryTerms.put('dataTime.refTime', RequestConstraint(TimeUtil.formatToSqlTimestamp(refTime)))
        if self.constraint:
            for k in self.constraint.keys():
                queryTerms.put(k, RequestConstraint(self.constraint[k]))
        return queryTerms
    
    def _organizeData(self, container):
        import PointDataView
        organizedData = {}
        for i in range(container.getCurrentSz()):
            pdv = PointDataView.PointDataView(container.readRandom(i))
            fcstHr = pdv[self.__keyId]
            organizedData[fcstHr] = pdv
        return organizedData
