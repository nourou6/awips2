##
##


#
# Statistics logging thread for pypies
#  
#    
#     SOFTWARE HISTORY
#    
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    05/12/11                      njensen        Initial Creation.
#    11/06/14        3549          njensen        Log receiveData
#    11/15/16        5992          bsteffen       Log size and decompress time
#    
# 
#

import threading, time, logging
STORE_DIR = '/awips2/edex/data/hdf5/'  # TODO this should be a config file
STORE_DIR_LEN = len(STORE_DIR)
SECTION_KEYS=['total',
              '  receiveData',
              '  deserialize',
              '  decompress',
              '  getLock',
              '    approxLockSleepTime',
              '    orphanCheck',
              '  openFile',
              '  getGroup',
              '  repack',
              '  read',
              '  store',
              '  createRecord',
              '  closeFile',
              '  releaseLock',
              '  serialize',
              'size']

SIZE_UNITS=['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB' ]

class StatsThread(threading.Thread):
    
    def __init__(self, logCfg):
        threading.Thread.__init__(self)
        t = time.time()
        self.minuteStats = {'lastOutput':t}
        self.hourStats = {'lastOutput':t}
        self.lock = threading.Lock()
        self.logCfg = logCfg
    
    def run(self):
        print "stats thread running"
        while True:
            try:
                t = time.gmtime()
                sleepTime = 60 - t.tm_sec # seconds
                time.sleep(sleepTime)
                
                with self.lock:
                    msg = self._createLogStatement(self.minuteStats)
                    self.logCfg.getMinutesLogger().info(msg)
                    self.minuteStats.clear()
                    self.minuteStats['lastOutput'] = time.time()
                    if t.tm_min == 59:
                        msg = self._createLogStatement(self.hourStats)
                        self.logCfg.getHoursLogger().info(msg)
                        self.hourStats.clear()
                        self.hourStats['lastOutput'] = time.time()
                                                            
                time.sleep(1)                
                
            except Exception, e:
                import sys, traceback, string
                t, v, tb = sys.exc_info()
                print string.join(traceback.format_exception(t, v, tb))                
                self.minuteStats.clear()
                self.hourStats.clear()
                self.minuteStats['lastOutput'] = time.time()
                self.hourStats['lastOutput'] = time.time()
                
        
    def addRecord(self, rec):
        with self.lock:        
            self.minuteStats = self.__addNewStat(self.minuteStats, rec)
            self.hourStats = self.__addNewStat(self.hourStats, rec)
    
    def __addNewStat(self, statDict, rec):
        filename = rec['file']
        pluginName = filename[STORE_DIR_LEN:]
        slashIndex = pluginName.find('/')
        if slashIndex > -1:
            plugin = pluginName[0:slashIndex]
        else:
            plugin = pluginName

        if statDict.has_key(plugin):
            pluginDict = statDict[plugin]
        else:
            pluginDict = {}
            statDict[plugin]=pluginDict

        req = rec['request']

        if pluginDict.has_key(req):
            reqDict=pluginDict[req]
        else:
            reqDict={}
            pluginDict[req] = reqDict

        recTimes = rec['time']

        for timeKey in recTimes.keys():
            recTime=recTimes[timeKey]

            if not reqDict.has_key(timeKey):
                reqDict[timeKey] = {'count':0, 'time':0.0, 'slowest':0.0, 'fastest':float('inf')}

            requestEntry = reqDict[timeKey]
            requestEntry['count'] += 1
            requestEntry['time'] += recTime
            if recTime > requestEntry['slowest']:
                requestEntry['slowest'] = recTime
            if recTime < requestEntry['fastest']:
                requestEntry['fastest'] = recTime

        return statDict
    
    
    def _createLogStatement(self, statDict):        
        SPC = ' '        
        COL = SPC * 4
        format = '%Y-%m-%d %H:%M:%S'
        stmt = "Statistics for "
        stmt += time.strftime(format, time.gmtime(statDict.pop('lastOutput'))) + " to "
        stmt += time.strftime(format, time.gmtime()) + ":\n"
        if len(statDict):
            stmt += COL + 'plugin'.ljust(20)
            stmt += 'request'.ljust(20) + COL
            stmt += 'section'.ljust(25) + COL
            stmt += 'count'.rjust(7) + COL
            stmt += 'average'.rjust(8) + COL
            stmt += 'min'.rjust(5) + COL
            stmt += 'max'.rjust(5)
            stmt += '\n'
            stmt += ('-' * 114) + '\n'
            pluginNames = statDict.keys()
            pluginNames.sort()
            for plugin in pluginNames: 
                pluginDict = statDict[plugin]
                reqNames = pluginDict.keys()
                reqNames.sort()
                for req in reqNames:
                    reqDict = pluginDict[req]
                    for section in SECTION_KEYS:
                        timeKey = section.strip()
                        if reqDict.has_key(timeKey):
                            stmt += COL + plugin.ljust(20)
                            entry = reqDict[timeKey]
                            avg = '%.3f' % (entry['time'] / entry['count'])
                            fast = '%.3f' % (entry['fastest'])
                            slow = '%.3f' % (entry['slowest'])
                            stmt += req.ljust(20) + COL
                            stmt += section.ljust(25) + COL
                            count = str(entry['count'])
                            if timeKey == 'size':
                                count = self._adjustSize(entry['time'])
                                avg = self._adjustSize(avg)
                                fast = self._adjustSize(fast)
                                slow = self._adjustSize(slow)
                            stmt += count.rjust(9) + avg.rjust(9)
                            stmt += fast.rjust(9) + slow.rjust(9) + '\n'
                stmt += '\n'
        else:
            stmt += COL + 'No transactions reported'
        return stmt

    def _adjustSize(self, entry):
        index=0
        entry=float(entry)
        maxIndex = len(SIZE_UNITS) - 1
        while entry > 1024 and index < maxIndex:
            entry /= 1024
            index +=1
        return '%.1f%s' % (entry, SIZE_UNITS[index])
