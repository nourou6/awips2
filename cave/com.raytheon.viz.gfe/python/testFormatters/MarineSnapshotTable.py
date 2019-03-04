##
##
#######################################################################
# Table Definition
#
########################################################################
## EXAMPLE OUTPUT (Scarce Data)

##    MarineSnapshotTable for Feb 29 00 17:00:00 GMT - Mar 01 00 11:00:00 GMT.

##    Edit Area      Wind (kt)  Waves (ft)  Swells (ft)

##    COAdams           W  10
##    COArapahoe        W  10
##    COBoulder         W   5
##    COClearCreek      W   5
##    CODenver          W   5
##    CODouglas         W   5
##    COElbert          W  10


MarineSnapshotTable =  {

      "type": "table",
      "displayName": "TEST_Marine Snapshot Table", # for Product Generation Menu

        # Output file for product results
      "outputFile": "./MarineSnapshotTable.txt",  # default output file

      "constantVariable": "TimePeriod",
      "rowVariable": "EditArea",
      "columnVariable": "WeatherElement",

      "beginningText": "MarineSnapshotTable for %TimePeriod. \n\n",
      "endingText": "",

      "defaultEditAreas": [("area1", "Area 1"),
                           ("area2", "Area 2"),
                          ],
      "runTimeEditAreas" : "yes", # if yes, ask user at run time
      "areaType" : "Edit Area", # E.g. City, County, Basin, etc.

      "defaultRanges": [("Today"),
                        ("Tonight"),
                        ("Tomorrow"),
                       ],
        # If runTimeRanges is yes, ask user to choose from defaults
        # at run time.
      "runTimeRanges" : "yes",

      "elementList": [
                ("Wind", "Wind (kt)",
                 "vectorRange",
                 "avgValue",
                 "Vector", 5, None),
                ("WaveHeight","Waves (ft)",
                 "minMax",
                 "range2Value",
                 "Scalar", 1, None),
                ("Swell","Swells (ft)",
                 "vectorAvg",
                 "singleValue",
                 "Vector", 1, None),
                 ],

        }
