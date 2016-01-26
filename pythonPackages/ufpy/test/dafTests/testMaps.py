##
# This software was developed and / or modified by Raytheon Company,
# pursuant to Contract DG133W-05-CQ-1067 with the US Government.
# 
# U.S. EXPORT CONTROLLED TECHNICAL DATA
# This software product contains export-restricted data whose
# export/transfer/disclosure is restricted by U.S. law. Dissemination
# to non-U.S. persons whether in the United States or abroad requires
# an export license or other authorization.
# 
# Contractor Name:        Raytheon Company
# Contractor Address:     6825 Pine Street, Suite 340
#                         Mail Stop B8
#                         Omaha, NE 68106
#                         402.291.0100
# 
# See the AWIPS II Master Rights File ("Master Rights File.pdf") for
# further licensing information.
##

from __future__ import print_function
from ufpy.dataaccess import DataAccessLayer as DAL

import dafTestsUtil
import sys
import unittest

class TestMaps(unittest.TestCase):
    """
    Tests that maps data can be retrieved through the DAF, simply ensuring
    that no unexpected exceptions are thrown while retrieving it and that the
    returned data is not None.
    """

    datatype = "maps"

    site = "OAX"

    @classmethod
    def setUpClass(cls):
        print("STARTING MAPS TESTS\n\n")

    def testParameters(self):
        req = DAL.newDataRequest(self.datatype)
        req.addIdentifier("table", "mapdata.county")
        req.addIdentifier("geomField", "the_geom")

        dafTestsUtil.testParameters(req)

    def testLocations(self):
        req = DAL.newDataRequest(self.datatype)
        req.addIdentifier("table", "mapdata.county")
        req.addIdentifier("geomField", "the_geom")
        req.addIdentifier("locationField", "cwa")

        dafTestsUtil.testLocations(req)

    def testGeometryData(self):
        req = DAL.newDataRequest(self.datatype)
        req.addIdentifier("table", "mapdata.county")
        req.addIdentifier("geomField", "the_geom")
        req.addIdentifier("inLocation", "true")
        req.addIdentifier("locationField", "cwa")
        req.setLocationNames(self.site)
        req.addIdentifier("cwa", self.site)
        req.setParameters("countyname", "state", "fips")

        dafTestsUtil.testGeometryData(req)

    @classmethod
    def tearDownClass(cls):
        print("MAPS TESTS COMPLETE\n\n\n")

def getArgs():
    parser = dafTestsUtil.getParser()
    parser.add_argument("-s", action="store", dest="site", default=TestMaps.site,
                        help="site to retrieve data for",
                        metavar="siteID")
    return parser.parse_args()

if __name__ == '__main__':
    args = getArgs()
    dafTestsUtil.handleArgs(args)
    TestMaps.site = args.site
    unittest.main(argv=sys.argv[:1])
