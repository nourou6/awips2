##
##
########################################################################
# PeriodTable
#
#   Type: table
#   Edit Areas: solicited from user
#   To Run:
#      Set GFE Time Range
#      Products-->Generate Products
#      Choose Edit Areas
#      Select OK
#
########################################################################
##  EXAMPLE OUTPUT

##    Period Table for Feb 29 00 17:00:00 GMT - Mar 01 00 07:00:00 GMT.

##    Edit Area    Sky (%)  Wind (mph)  Max Temp  Min Temp  Precip (%)

##    COAdams         10      NW  10       53        38          0
##    COArapahoe      10      NW  10       53        38          0
##    COBoulder       5-30    NW  10       46        34          0
##    CODenver        5-20    NW  10       54        39          0
##    CODouglas       5-20    NW  10       52        36          0

########################################################################
Definition =  {

     ## General Set-Up
      "type": "table",
      "displayName": "TEST_Period Table", # for Product Generation Menu
      "outputFile": "./PeriodTable.txt",  # default output file

     ## Table Layout
      "constantVariable": "TimePeriod",
      "rowVariable": "EditArea",
      "columnVariable": "WeatherElement",

      "beginningText": "Period Table for %TimePeriod. \n\n",
      "endingText": "",

      "defaultEditAreas": [("area1", "Area 1"),
                           ("area2", "Area 2"),
                          ],
     ## Edit Areas
      "runTimeEditAreas" : "yes", # if yes, ask user at run time
      "areaType" : "Edit Area", # E.g. City, County, Basin, etc.

      "defaultRanges": [("Today"),
                        ("Tonight"),
                        ("Tomorrow"),
                       ],
        # If runTimeRanges is yes, ask user to choose from defaults
        # at run time.
      "runTimeRanges" : "yes",

     ## Weather Elements
        # Name     , Label    , Analysis Method , ReportAs Method ,
        # DataType , Rounding , Conversion

      "elementList": [
                ("Sky", "Sky (%)",
                 "minMax",
                 "range2Value",
                 "Scalar", 5, None),

                ("Wind","Wind (mph)",
                 "vectorRange",
                 "avgValue",
                 "Vector", 5, "ktToMph"),

                ("MaxT","Max Temp",
                 "avg",
                 "singleValue",
                 "Scalar", 1, None),

                ("MinT","Min Temp",
                 "avg",
                 "singleValue",
                 "Scalar", 1, None),

                ("PoP", "Precip (%)",
                 "avg",
                 "singleValue",
                 "Scalar", 5, None),
                 ],


    }
