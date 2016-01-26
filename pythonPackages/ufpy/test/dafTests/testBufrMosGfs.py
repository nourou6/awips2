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

import baseBufrMosTest
import dafTestsUtil
import sys
import unittest

class TestBufrMosGfs(baseBufrMosTest.BaseBufrMosTest):
    """
    Tests that bufrmosGFS data can be retrieved through the DAF, simply ensuring
    that no unexpected exceptions are thrown while retrieving it and that the
    returned data is not None.
    """

    datatype = "bufrmosGFS"

    @classmethod
    def setUpClass(cls):
        print("STARTING BUFRMOSGFS TESTS\n\n")

    # All tests inherited from superclass
    
    @classmethod
    def tearDownClass(cls):
        print("BUFRMOSGFS TESTS COMPLETE\n\n\n")

if __name__ == '__main__':
    dafTestsUtil.parseAndHandleArgs()
    unittest.main(argv=sys.argv[:1])
