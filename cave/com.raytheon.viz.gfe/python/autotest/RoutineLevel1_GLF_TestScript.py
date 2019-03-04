##
##
# ----------------------------------------------------------------------------
# This software is in the public domain, furnished "as is", without technical
# support, and with no warranty, express or implied, as to its usefulness for
# any purpose.
#
# GLF tests
#
# Author: hansen
# ----------------------------------------------------------------------------
import TestScript

scripts = [
    {
    "commentary":"""
    Morning Test at 4 a.m.
    """,
    "name":"GLF_1", 
    "productType":"GLF",
    "cmdLineVars": "{('Product Issuance', 'productIssuance'): '400 AM', ('Groupings', 'groupings'): 'West 1/2:East 1/2'}",
    "comboFlag": 0, 
    "checkStrings": ["...STORM WATCH IN EFFECT THROUGH THIS EVENING..."],
    "createGrids": [
        ("Fcst", "Hazards", "DISCRETE", 0, 24, "SR.A", "all"),
        ],
    },
    {
    "commentary":"""
    Morning Test at 4 a.m.
    """,
    "name":"GLF_2", 
    "productType":"GLF",
    "cmdLineVars": "{('Product Issuance', 'productIssuance'): '400 AM', ('Groupings', 'groupings'): 'West 1/2:East 1/2'}",
    "comboFlag": 0, 
    "checkStrings": [
        "WEST HALF", "...STORM WATCH IN EFFECT THROUGH THIS EVENING...",
        "EAST HALF", "...HAZARDOUS SEAS WATCH IN EFFECT THROUGH THIS EVENING...",
        ],
    "createGrids": [
        ("Fcst", "Hazards", "DISCRETE", 0, 24, "SR.A", ["west_half"]),
        ("Fcst", "Hazards", "DISCRETE", 0, 24, "SE.A", ["east_half"]),
        ],
    },
    {
    "commentary":"""
    Morning Test at 4 a.m.
    """,
    "name":"GLF_3", 
    "productType":"GLF",
    "cmdLineVars": "{('Product Issuance', 'productIssuance'): '400 AM', ('Groupings', 'groupings'): 'Entire Lake'}",
    "comboFlag": 0, 
    "checkStrings": [
       "...STORM WATCH IN EFFECT THROUGH THIS EVENING..."
        ],
    "notCheckStrings": [
       "WEST HALF", "EAST HALF",
        ],
    "createGrids": [
        ("Fcst", "Hazards", "DISCRETE", 0, 24, "SR.A", ["west_half"]),
        ("Fcst", "Hazards", "DISCRETE", 0, 24, "SE.A", ["east_half"]),
        ],
    },
    ]

def testScript(self, dataMgr, level="Site"):
    gridsStartTime = self.getAbsFromLocal(2010, 1, 1, 0, 0)
    drtTime = self.getAbsFromLocal(2010, 1, 1, 4, 0)    
    defaults = {
        "gridsStartTime": gridsStartTime,
        "drtTime": drtTime,
        "orderStrings": 1,
        "internalStrip": 0, 
        }
    for script in scripts:
        drtHour = script.get("drtHour", None)
        if drtHour is not None:
            script["drtTime"] =  self.getAbsFromLocal(2010, 1, 1, drtHour, 0)      
    return TestScript.generalTestScript(self, dataMgr, scripts, defaults, level=level)


