##
##
# ----------------------------------------------------------------------------
# This software is in the public domain, furnished "as is", without technical
# support, and with no warranty, express or implied, as to its usefulness for
# any purpose.
#
# Hazards_TestScript
#
# Author:
# ----------------------------------------------------------------------------


# The following tuples are of the form:

##  testName, product, comboFlag, hazards, cmdLineVars, checkStrs
def1 = "    def __init__(self):"

def2 = """
    Definition["includeCities"] = 1
    Definition["cityDescriptor"] = "Including the areas of"
    Definition["includeZoneNames"] = 0
    def __init__(self):
"""

def3 = """
    Definition["defaultEditAreas"] = [("FLZ142", "CITRUS")]
    def __init__(self):
"""

scripts = [
    {"name":"CFW1",
     "productType" : "Hazard_CFW_Local",
     "commentary": "Basic testing of CFW product with CF.Y.",
     "createGrids": [
        ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
        ("Fcst", "Hazards", "DISCRETE", 0, 96, "CF.Y", "all"),
        ],
     "checkStrings" : [
        "Coastal Hazard Message",
        "National Weather Service Tampa Bay Ruskin FL",
        "700 PM EDT Wed May 26 2010",
        "FLZ043-050-052-056-057-061-139-142-148-149-151-155-160-162-165-",
        "239-242-248-249-251-255-260-262-265-",
        "/O.NEW.KTBW.CF.Y.0001.100526T2300Z-100530T2300Z/",
        "700 PM EDT Wed May 26 2010",
        "...COASTAL FLOOD ADVISORY IN EFFECT UNTIL 7 PM EDT SUNDAY...",
        "The National Weather Service in Tampa Bay Ruskin has issued a Coastal Flood Advisory, which is in effect until 7 PM EDT Sunday.",
        "PRECAUTIONARY/PREPAREDNESS ACTIONS...", 
        "&&",
        ],
     },
    
    {"name":"FFA1", 
     "productType" : "Hazard_FFA_Local", 
     "commentary": "Basic testing of FFA product with FF.A.",
     "createGrids": [
        ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
        ("Fcst", "Hazards", "DISCRETE", 4, 7, "FF.A", "all"),
        ],
     "cmdLineVars" : "{('Issued By', 'issuedBy'): None, ('Flood Reason (HVTEC)', 'floodReason'): 'ER (Excessive Rainfall)'}",
     "checkStrings" : [
          "URGENT - IMMEDIATE BROADCAST REQUESTED",
          "Flood Watch",
          "National Weather Service Tampa Bay Ruskin FL",
          "700 PM EDT Wed May 26 2010",
          "...|*Overview headline (must edit)*|...",
          ".|*Overview (must edit)*|.",
          "FLZ043-050-052-056-057-061-139-142-148-149-151-155-160-162-165-",
          "239-242-248-249-251-255-260-262-265-",
          "/O.NEW.KTBW.FF.A.0001.100527T0300Z-100527T0600Z/",
          "/00000.0.ER.000000T0000Z.000000T0000Z.000000T0000Z.OO/",
          "Sumter-",
          "700 PM EDT Wed May 26 2010",
          "...FLASH FLOOD WATCH IN EFFECT FROM 11 PM THIS EVENING TO 2 AM EDT THURSDAY...",
          "The National Weather Service in Tampa Bay Ruskin has issued a",
          "* Flash Flood Watch for portions of central Florida, northern Florida, south central Florida, southwest Florida, and west central Florida, including the following areas, in central Florida, Hardee, Polk, and Sumter. In northern Florida, Coastal Levy and Inland Levy. In south central Florida, DeSoto and Highlands. In southwest Florida, Coastal Charlotte, Coastal Lee, Inland Charlotte, and Inland Lee. In west central Florida, Coastal Citrus, Coastal Hernando, Coastal Hillsborough, Coastal Manatee, Coastal Pasco, Coastal Sarasota, Inland Citrus, Inland Hernando, Inland Hillsborough, Inland Manatee, Inland Pasco, Inland Sarasota, and Pinellas.",
          "* From 11 PM this evening to 2 AM EDT Thursday",
          "PRECAUTIONARY/PREPAREDNESS ACTIONS...", 
          "&&",
        ],

     },
    
    
    
    {"name":"HWO1", 
     "productType" : "Hazard_HWO_Local", 
     "commentary": "Basic testing of HWO product - no active weather",
     "comboFlag" : 1,
     "combinations" :[(["FLZ142"],"")],
     "cmdLineVars" : "{('Issued By', 'issuedBy'): None, ('HWO Type', 'hwoType'): 'No Active Weather'}",
     "checkStrings" : [
        "Hazardous Weather Outlook",
        "National Weather Service Tampa Bay Ruskin FL",
        "700 PM EDT Wed May 26 2010",
        "FLZ142-",
        "Citrus-",
        "700 PM EDT Wed May 26 2010",
        "This Hazardous Weather Outlook is for portions of west central Florida.",
        ".DAY ONE...Tonight",
        "No hazardous weather is expected at this time.",
        ".DAYS TWO THROUGH SEVEN...Thursday through Tuesday",
        "No hazardous weather is expected at this time.",
        ".SPOTTER INFORMATION STATEMENT...",
        "Spotter activation will not be needed.",
        "$$",
   ],

     },
    
    {"name":"HWO2", 
     "productType" : "Hazard_HWO_Local", 
     "commentary": "Basic testing of HWO product - active weather",
     "comboFlag" : 1,
     "combinations" :[(["FLZ142"],"")],
     "cmdLineVars" : "{('Issued By', 'issuedBy'): None, ('HWO Type', 'hwoType'): 'Active Weather'}",
     "gridsStartTime": "20100527_0600",
     "checkStrings" : [
          "Hazardous Weather Outlook",
          "National Weather Service Tampa Bay Ruskin FL",
          "200 AM EDT Thu May 27 2010",
          "FLZ142-280600-",
          "Citrus-",
          "200 AM EDT Thu May 27 2010",
          "This Hazardous Weather Outlook is for portions of west central Florida.",
          ".DAY ONE...Tonight",
          ".DAYS TWO THROUGH SEVEN...Thursday through Tuesday",
          ".SPOTTER INFORMATION STATEMENT...",
          "$$",
       ],
     },
    
    {"name":"HWO3", # Test includeCities (set to 1), cityDescriptor, includeZoneNames(set to 0)
     "productType" : "Hazard_HWO_Local", 
     "commentary": "Basic testing of HWO product - active weather, includeCities, cityDescriptor, includeZoneNames set to 0",
     "comboFlag" : 1,
     "combinations" :[(["FLZ142"],"")],
     "cmdLineVars" : "{('Issued By', 'issuedBy'): None, ('HWO Type', 'hwoType'): 'Active Weather'}",
     "gridsStartTime": "20100527_0600",
     "fileChanges": [
          ("Hazard_HWO_Local", "TextProduct", "replace", (def1, def2), "undo"),
          ],
     "notCheckStrings": [
          "Citrus-",
          ],
     "checkStrings" : [
          "Hazardous Weather Outlook",
          "National Weather Service Tampa Bay Ruskin FL",
          "200 AM EDT Thu May 27 2010",
          "FLZ142-280600-",
          "Including the areas of Chassahowitzka, Crystal River, Homosassa, and Ozello",
          "200 AM EDT Thu May 27 2010",
          "This Hazardous Weather Outlook is for portions of west central Florida.",
          ".DAY ONE...Tonight",
          ".DAYS TWO THROUGH SEVEN...Thursday through Tuesday",
          ".SPOTTER INFORMATION STATEMENT...",
          "$$",
       ],
     },

    {"name":"HWO4", # Test for TK 4628
     "productType" : "Hazard_HWO_Local", 
     "commentary": "Basic testing of HWO product - tk4628- DR16885",
     "comboFlag" : 1,
     "combinations" :[(["FLZ142"],"")],
     "cmdLineVars" : "{('Issued By', 'issuedBy'): None, ('HWO Type', 'hwoType'): 'Active Weather'}",
     "gridsStartTime": "20100527_0600",
     "fileChanges": [
          ("Hazard_HWO_Local", "TextProduct", "replace", (def1, def3), "undo"),
          ],
     "checkStrings" : [
          "Hazardous Weather Outlook",
          "National Weather Service Tampa Bay Ruskin FL",
          "200 AM EDT Thu May 27 2010",
          "FLZ142-280600-",
          "Coastal Citrus-",
          "200 AM EDT Thu May 27 2010",
          "This Hazardous Weather Outlook is for portions of west central Florida.",
          ".DAY ONE...Tonight",
          ".DAYS TWO THROUGH SEVEN...Thursday through Tuesday",
          ".SPOTTER INFORMATION STATEMENT...",
          "$$",
       ],
     },
     
    {"name":"MWS1", 
     "productType" : "Hazard_MWS_Local", 
     "commentary": "Basic testing of MWS product with MA.S",
     "createGrids": [
        ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
        ("Fcst", "Hazards", "DISCRETE", 9, 13, "MA.S", "all"),
        ],
     "checkStrings" : [
         "Marine Weather Statement",
         "National Weather Service Tampa Bay Ruskin FL",
         "700 PM EDT Wed May 26 2010",
         "GMZ830-836-850-853-856-870-873-876-",
         "/O.NEW.KTBW.MA.S.0001.100527T0800Z-100527T1200Z/",
         "Tampa Bay waters-",
         "Coastal waters from Tarpon Springs to Suwannee River FL out 20 NM-",
         "Coastal waters from Englewood to Tarpon Springs FL out 20 NM-",
         "Coastal waters from Bonita Beach to Englewood FL out 20 NM-",
         "Waters from Tarpon Springs to Suwannee River FL out 20 to 60 NM-",
         "Waters from Englewood to Tarpon Springs FL out 20 to 60 NM-",
         "Waters from Bonita Beach to Englewood FL out 20 to 60 NM-",
         "700 PM EDT Wed May 26 2010",
         "|* Statement text goes here *|.",
         "$$",
        ],
     },
    
    {"name":"MWW1", 
     "productType" : "Hazard_MWW_Local", 
     "commentary": "Basic testing of MWW product with GL.A",
     "createGrids": [
        ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
        ("Fcst", "Hazards", "DISCRETE", 0, 1, "GL.A", "all"),
        ],
     "checkStrings" : [
        "URGENT - MARINE WEATHER MESSAGE",
        "National Weather Service Tampa Bay Ruskin FL",
        "700 PM EDT Wed May 26 2010",
        "...|*Overview headline (must edit)*|...",
        ".|*Overview (must edit)*|.",
        "GMZ830-836-850-853-856-870-873-876-270000-",
        "/O.NEW.KTBW.GL.A.0001.100526T2300Z-100527T0000Z/",
        "Tampa Bay waters-",
        "Coastal waters from Tarpon Springs to Suwannee River FL out 20 NM-",
        "Coastal waters from Englewood to Tarpon Springs FL out 20 NM-",
        "Coastal waters from Bonita Beach to Englewood FL out 20 NM-",
        "Waters from Tarpon Springs to Suwannee River FL out 20 to 60 NM-",
        "Waters from Englewood to Tarpon Springs FL out 20 to 60 NM-",
        "Waters from Bonita Beach to Englewood FL out 20 to 60 NM-",
        "700 PM EDT Wed May 26 2010",
        "...GALE WATCH IN EFFECT UNTIL 8 PM EDT THIS EVENING...",
        "The National Weather Service in Tampa Bay Ruskin has issued a Gale Watch, which is in effect until 8 PM EDT this evening.",
#        "|* SEGMENT TEXT GOES HERE *|.",
        "PRECAUTIONARY/PREPAREDNESS ACTIONS...", 
        "&&",
        "$$",
        ],
     },

    {"name":"MWW2",
     "productType" : "Hazard_MWW_Local",
     "commentary": "Basic testing of MWW product with MH.W",
     "createGrids": [
        ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
        ("Fcst", "Hazards", "DISCRETE", 0, 1, "MH.W", "all"),
        ],
     "checkStrings" : [
        "URGENT - MARINE WEATHER MESSAGE",
        "National Weather Service Tampa Bay Ruskin FL",
        "700 PM EDT Wed May 26 2010",
        "...|*Overview headline (must edit)*|...",
        ".|*Overview (must edit)*|.",
        "GMZ830-836-850-853-856-870-873-876-270000-",
        "/O.NEW.KTBW.MH.W.0001.100526T2300Z-100527T0000Z/",
        "Tampa Bay waters-",
        "Coastal waters from Tarpon Springs to Suwannee River FL out 20 NM-",
        "Coastal waters from Englewood to Tarpon Springs FL out 20 NM-",
        "Coastal waters from Bonita Beach to Englewood FL out 20 NM-",
        "Waters from Tarpon Springs to Suwannee River FL out 20 to 60 NM-",
        "Waters from Englewood to Tarpon Springs FL out 20 to 60 NM-",
        "Waters from Bonita Beach to Englewood FL out 20 to 60 NM-",
        "700 PM EDT Wed May 26 2010",
        "...ASHFALL WARNING IN EFFECT UNTIL 8 PM EDT THIS EVENING...",
        "The National Weather Service in Tampa Bay Ruskin has issued an Ashfall Warning, which is in effect until 8 PM EDT this evening.",
#         "|* SEGMENT TEXT GOES HERE *|.",
        "PRECAUTIONARY/PREPAREDNESS ACTIONS...",
        "An Ashfall Warning means that significant accumulation of ashfall is expected on vessels. It is recommended that vessels be prepared to take the necessary counter measures before putting to sea or entering the warning area.",
        "&&",
        "$$",
        ],
     },

    {"name":"NPW1",
     "productType" : "Hazard_NPW_Local",
     "commentary": "Basic testing of NPW product with AS.O",
     "createGrids": [
        ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
        ("Fcst", "Hazards", "DISCRETE", 0, 1, "AS.O", "all"),
        ],
     "checkStrings" : [
        "WWUS72 KTBW 262300",
        "NPWTBW",
        "URGENT - WEATHER MESSAGE",
        "National Weather Service Tampa Bay Ruskin FL",
        "700 PM EDT Wed May 26 2010",
        "...|*Overview headline (must edit)*|...",
        ".|*Overview (must edit)*|.",
        "FLZ043-050-052-056-057-061-139-142-148-149-151-155-160-162-165-",
        "239-242-248-249-251-255-260-262-265-270000-",
        "/O.NEW.KTBW.AS.O.0001.100526T2300Z-100527T0000Z/",
        "Sumter-Pinellas-Polk-Hardee-Highlands-DeSoto-Coastal Levy-",
        "Coastal Citrus-Coastal Hernando-Coastal Pasco-",
        "Coastal Hillsborough-Coastal Manatee-Coastal Sarasota-",
        "Coastal Charlotte-Coastal Lee-Inland Levy-Inland Citrus-",
        "Inland Hernando-Inland Pasco-Inland Hillsborough-Inland Manatee-",
        "Inland Sarasota-Inland Charlotte-Inland Lee-",
        "Including the cities of ",
#         "Including the cities of Williston, Chiefland, Bronson, ",
#         "Cedar Key, Fanning Springs, Homosassa Springs, Beverly Hills, ",
#         "Hernando, Inverness, LeCanto, Floral City, Citrus Springs, ",
#         "Wildwood, Lake Panasoffkee, Bushnell, Spring Hill, Holiday, ",
#         "Land O' Lakes, Jasmine Estates, New Port Richey, Hudson, ",
#         "Zephyrhills, Dade City, St. Petersburg, Clearwater, Largo, ",
#         "Tampa, Brandon, Lakeland, Winter Haven, Bradenton, ",
#         "Bayshore Gardens, Palmetto, Wauchula, Bowling Green, ",
#         "Zolfo Springs, Sebring, Avon Park, Placid Lakes, Sarasota, ",
#         "North Port, Venice, Englewood, South Venice, Arcadia, ",
#         "Port Charlotte, Punta Gorda, Cape Coral, Fort Myers, ",
#         "North Fort Myers, Lehigh Acres, and Bonita Springs",
        "...AIR STAGNATION OUTLOOK IN EFFECT UNTIL 8 PM EDT THIS EVENING...",
#       "|* SEGMENT TEXT GOES HERE *|. ",
        "$$",
        ],
     },
    
    {"name":"NPW2",
     "productType" : "Hazard_NPW_Local",
     "commentary": "Basic testing of NPW product with AF.W",
     "createGrids": [
        ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
        ("Fcst", "Hazards", "DISCRETE", 0, 1, "AF.W", "all"),
        ],
     "checkStrings" : [
        "WWUS72 KTBW 262300",
        "NPWTBW",
        "URGENT - WEATHER MESSAGE",
        "National Weather Service Tampa Bay Ruskin FL",
        "700 PM EDT Wed May 26 2010",
        "...|*Overview headline (must edit)*|...",
        ".|*Overview (must edit)*|.",
        "FLZ043-050-052-056-057-061-139-142-148-149-151-155-160-162-165-",
        "239-242-248-249-251-255-260-262-265-270000-",
        "/O.NEW.KTBW.AF.W.0001.100526T2300Z-100527T0000Z/",
        "Sumter-Pinellas-Polk-Hardee-Highlands-DeSoto-Coastal Levy-",
        "Coastal Citrus-Coastal Hernando-Coastal Pasco-",
        "Coastal Hillsborough-Coastal Manatee-Coastal Sarasota-",
        "Coastal Charlotte-Coastal Lee-Inland Levy-Inland Citrus-",
        "Inland Hernando-Inland Pasco-Inland Hillsborough-Inland Manatee-",
        "Inland Sarasota-Inland Charlotte-Inland Lee-",
        "Including the cities of ",
#         "Including the cities of Williston, Chiefland, Bronson, ",
#         "Cedar Key, Fanning Springs, Homosassa Springs, Beverly Hills, ",
#         "Hernando, Inverness, LeCanto, Floral City, Citrus Springs, ",
#         "Wildwood, Lake Panasoffkee, Bushnell, Spring Hill, Holiday, ",
#         "Land O' Lakes, Jasmine Estates, New Port Richey, Hudson, ",
#         "Zephyrhills, Dade City, St. Petersburg, Clearwater, Largo, ",
#         "Tampa, Brandon, Lakeland, Winter Haven, Bradenton, ",
#         "Bayshore Gardens, Palmetto, Wauchula, Bowling Green, ",
#         "Zolfo Springs, Sebring, Avon Park, Placid Lakes, Sarasota, ",
#         "North Port, Venice, Englewood, South Venice, Arcadia, ",
#         "Port Charlotte, Punta Gorda, Cape Coral, Fort Myers, ",
#         "North Fort Myers, Lehigh Acres, and Bonita Springs",
        "700 PM EDT Wed May 26 2010",
        "...ASHFALL WARNING IN EFFECT UNTIL 8 PM EDT THIS EVENING...",
        "The National Weather Service in Tampa Bay Ruskin has issued an Ashfall Warning, which is in effect until 8 PM EDT this evening.",
#         "|* SEGMENT TEXT GOES HERE *|.",
        "PRECAUTIONARY/PREPAREDNESS ACTIONS...",
        "An Ashfall Warning means that significant accumulation of volcanic ash is expected or occurring due to a volcanic eruption or resuspension of previously deposited ash.",
        " Listen to NOAA Weather Radio or local media for further information.",
        "&&",
        "$$",
        ],
     },
 
    {"name":"RFW1", 
     "productType" : "Hazard_RFW_Local", 
     "commentary": "Basic testing of RFW product with FW.W",
     "createGrids": [
        ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
        ("Fcst", "Hazards", "DISCRETE", 2, 15, "FW.W", "all"),
        ],
     "cmdLineVars" : "{('Select RFW Type', 'rfwType'): [], ('Source for Headline and \\nAffected Area Bullet', 'elevationSource'): 'Grids'}",
     "checkStrings" : [
         "WWUS82 KTBW 262300",
         "RFWTBW",
         "URGENT - FIRE WEATHER MESSAGE",
         "National Weather Service Tampa Bay Ruskin FL",
         "700 PM EDT Wed May 26 2010",
         "...|*Overview headline (must edit)*|...",
         ".|*Overview (must edit)*|.",
         "FLZ043-050-052-056-057-061-139-142-148-149-151-155-160-162-165-",
         "239-242-248-249-251-255-260-262-265-270700-",
         "/O.NEW.KTBW.FW.W.0001.100527T0100Z-100527T1400Z/",
         "Sumter-Pinellas-Polk-Hardee-Highlands-DeSoto-Coastal Levy-",
         "700 PM EDT Wed May 26 2010",
         "...RED FLAG WARNING IN EFFECT UNTIL 10 AM EDT THURSDAY",
         "The National Weather Service in Tampa Bay Ruskin has issued a Red Flag Warning, which is in effect until 10 AM EDT Thursday.",
#          "|* SEGMENT TEXT GOES HERE *|.",
         "PRECAUTIONARY/PREPAREDNESS ACTIONS...", 
         "A Red Flag Warning means that critical fire weather conditions are either occurring now, or will shortly.",
         "&&",
         "$$",
        ],
     },

    {"name":"WCN1", 
     "productType" : "Hazard_WCN_Local", 
     "commentary": "Basic testing of WCN product with TO.A",
     "createGrids": [
        ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
        ("Fcst", "Hazards", "DISCRETE", 0, 6, "TO.A:123", "all"),
        ],
     "checkStrings" : [
        "WWUS62 KTBW 262300",
        "WCNTBW",
        "Watch County Notification for Watch 123",
        "National Weather Service Tampa Bay Ruskin FL",
        "700 PM EDT Wed May 26 2010",
        "FLC015-017-027-049-053-055-057-071-",
        "/O.NEW.KTBW.TO.A.0123.100526T2300Z-100527T0500Z/",
        "The National Weather Service has issued Tornado Watch 123 in effect until 1 AM EDT Thursday for the following areas",
        "In Florida this watch includes 15 counties",
        "In central Florida",
        "Hardee Polk Sumter",
        "In northern Florida",
        "Levy",
        "In south central Florida",
        "DeSoto Highlands",
        "In southwest Florida",
        "Charlotte Lee",
        "In west central Florida",
        "Citrus Hernando Hillsborough",
        "Manatee Pasco Pinellas",
        "Sarasota",
        "$$",
        "GMZ830-836-850-853-856-870-873-876-270500-",
        "/O.NEW.KTBW.TO.A.0123.100526T2300Z-100527T0500Z/",
        "The National Weather Service has issued Tornado Watch 123 in effect until 1 AM EDT Thursday for the following areas",
        "This watch includes the following adjacent coastal waters",
        "Tampa Bay waters",
        "Coastal waters from Tarpon Springs to Suwannee River FL out 20 NM",
        "Coastal waters from Englewood to Tarpon Springs FL out 20 NM",
        "Coastal waters from Bonita Beach to Englewood FL out 20 NM",
        "Waters from Tarpon Springs to Suwannee River FL out 20 to 60 NM",
        "Waters from Englewood to Tarpon Springs FL out 20 to 60 NM",
        "Waters from Bonita Beach to Englewood FL out 20 to 60 NM",
        "$$",

       ],
     },
    
    {"name":"WSW1", 
     "productType" : "Hazard_WSW_Local", 
     "commentary": "Basic testing of WSW product with BZ.W",
     "createGrids": [
        ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
        ("Fcst", "Hazards", "DISCRETE", 12, 21, "BZ.W", "all"),
        ],
     "checkStrings" : [
        "WWUS42 KTBW 262300",
        "WSWTBW",
        "URGENT - WINTER WEATHER MESSAGE",
        "National Weather Service Tampa Bay Ruskin FL",
        "700 PM EDT Wed May 26 2010",
        "...|*Overview headline (must edit)*|...",
        ".|*Overview (must edit)*|.",
        "FLZ043-050-052-056-057-061-139-142-148-149-151-155-160-162-165-",
        "239-242-248-249-251-255-260-262-265-270700-",
        "/O.NEW.KTBW.BZ.W.0001.100527T1100Z-100527T2000Z/",
        "Sumter-Pinellas-Polk-Hardee-Highlands-DeSoto-Coastal Levy-",
        "700 PM EDT Wed May 26 2010",
        "...BLIZZARD WARNING IN EFFECT FROM 7 AM TO 4 PM EDT THURSDAY...",
        "The National Weather Service in Tampa Bay Ruskin has issued a Blizzard Warning, which is in effect from 7 AM to 4 PM EDT Thursday.",
#       "|* SEGMENT TEXT GOES HERE *|. ",
        "PRECAUTIONARY/PREPAREDNESS ACTIONS...", 
        "A Blizzard Warning means severe winter weather conditions are expected or occurring. Falling and blowing snow with strong winds and poor visibilities are likely. This will lead to whiteout conditions, making travel extremely dangerous. Do not travel. If you must travel, have a winter survival kit with you. If you get",
        "stranded, stay with your vehicle.",
        "&&",
        "$$",
        ],
     },    
    {"name":"AQA1",
     "productType" : "Hazard_AQA_ABC_Local",
     "commentary": "Basic testing of AQA product with AQ.Y",
     "createGrids": [
        ("Fcst", "Hazards", "DISCRETE", -100, 100, "<None>", "all"),
        ("Fcst", "Hazards", "DISCRETE", 0, 1, "AQ.Y", "all"),
        ],
       "cmdLineVars" :"{('Source', 'source'): 'Colorado Emergency Management Agency Denver Colorado', ('Issued By', 'issuedBy'): None, ('EAS Level', 'eas'): 'None', ('Alert Code', 'alertCode'): 'Orange'}",
     "checkStrings" : [

        "UFUS42 KTBW 262300",
        "AQAABC",

        "Air Quality Alert",
        "Relayed by National Weather Service Tampa Bay Ruskin FL",
        "700 PM EDT Wed May 26 2010",

        "FLZ043-050-052-056-057-061-139-142-148-149-151-155-160-162-165-239-",
        "242-248-249-251-255-260-262-265-270000-",
        "/O.NEW.KTBW.AQ.Y.0001.100526T2300Z-100527T0000Z/",
        "Sumter-Pinellas-Polk-Hardee-Highlands-DeSoto-Coastal Levy-",
        "Coastal Citrus-Coastal Hernando-Coastal Pasco-Coastal Hillsborough-",
        "Coastal Manatee-Coastal Sarasota-Coastal Charlotte-Coastal Lee-",
        "Inland Levy-Inland Citrus-Inland Hernando-Inland Pasco-",
        "Inland Hillsborough-Inland Manatee-Inland Sarasota-Inland Charlotte-",
        "Inland Lee-",
        "Including the cities of ",
#         "Including the cities of Williston, Chiefland, Bronson, ",
#         "Cedar Key, Fanning Springs, Homosassa Springs, Beverly Hills, ",
#         "Hernando, Inverness, LeCanto, Floral City, Citrus Springs, ",
#         "Wildwood, Lake Panasoffkee, Bushnell, Spring Hill, Holiday, ",
#         "Land O' Lakes, Jasmine Estates, New Port Richey, Hudson, ",
#         "Zephyrhills, Dade City, St. Petersburg, Clearwater, Largo, ",
#         "Tampa, Brandon, Lakeland, Winter Haven, Bradenton, ",
#         "Bayshore Gardens, Palmetto, Wauchula, Bowling Green, ",
#         "Zolfo Springs, Sebring, Avon Park, Placid Lakes, Sarasota, ",
#         "North Port, Venice, Englewood, South Venice, Arcadia, ",
#         "Port Charlotte, Punta Gorda, Cape Coral, Fort Myers, ",
#         "North Fort Myers, Lehigh Acres, and Bonita Springs",
        "700 PM EDT Wed May 26 2010",

        "...AIR QUALITY ALERT IN EFFECT UNTIL 8 PM EDT THIS EVENING...",

        "The North Carolina Department of Environmental and Natural Resources",
        "has issued an Air Quality Action Day, in effect until 8 PM EDT this",
        "evening.",

        "A Code Orange Air Quality Alert for Ozone has been issued. Ground",
        "level ozone concentrations within the region may approach or exceed",
        "unhealthy standards. Members of sensitive groups may experience",
        "health effects. The general public is not likely to be affected.",
        "For additional information, please visit the North Carolina",
        "Division of Air Quality web site at",
        "http://daq.state.nc.us/airaware/forecast/.",

        "$$",
        ],
     },

    ]

import TestScript
def testScript(self, dataMgr):
    defaults = {
        "cmdLineVars" :"{('Source', 'source'): 'Colorado Emergency Management Agency Denver Colorado', ('Issued By', 'issuedBy'): None, ('EAS Level', 'eas'): 'None'}",
        "publishGrids" : 1,
        "vtecMode" : "O",
        "clearHazardsTable": 1,
        "gridsStartTime": "20100526_2300",
        "orderStrings": 1,
        "deleteGrids" : [("Fcst", "Hazards", "SFC", "all", "all")],
        }
    return TestScript.generalTestScript(self, dataMgr, scripts, defaults)

