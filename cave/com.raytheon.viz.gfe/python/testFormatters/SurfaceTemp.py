##
##
########################################################################
# SurfaceTemp
#
#   Type: table
#   Edit Areas: solicited from user
#   To Run:
#      Products-->Generate Products
#      Choose Edit Areas and Period (default is every 3 hours)
#      Select OK
#
########################################################################
## EXAMPLE OUTPUT

##    Experimental Surface Temperature Guidance Product

##    Edit Area      12Z/29  18Z/29  0Z/1  6Z/1  12Z/1  18Z/1  0Z/2

##    COAdams          39      39     39    39     39     39    39
##    COArapahoe       39      39     39    39     39     39    39
##    COBoulder        28      28     28    28     28     28    28
##    COClearCreek     21      21     21    21     21     21    21
##    CODenver         37      37     37    37     37     37    37
##    CODouglas        34      34     34    34     34     34    34
##    COElbert         39      39     39    39     39     39    39



########################################################################
Definition =  {

      "type": "table",
      "displayName": "TEST_Surface Temperature Table", # for Product Generation Menu

        # Output file for product results
      "outputFile": "./SurfaceTemp.txt",  # default output file

      "constantVariable": "WeatherElement",
      "rowVariable": "EditArea",
      "columnVariable": "TimePeriod",

      "beginningText": "Experimental Surface Temperature Guidance Product \n\n",
      "endingText": "",

      # Edit Areas
      "defaultEditAreas" : [("area1","Area 1"),("area2","Area 2")],
      "runTimeEditAreas": "yes",
      "areaType" : "Edit Area", # E.g. City, County, Basin, etc.

      # Time Ranges
      "defaultRanges":["Today"],
      "runTimeRanges": "no",

      "elementList": [
                ("T","Temp",
                 "avg",
                 "singleValue",
                 "Scalar", 1, None),
                 ],


      "timePeriod": 3,
      "runTimePeriod": "yes",  # If yes, ask user at run time for period
    }
