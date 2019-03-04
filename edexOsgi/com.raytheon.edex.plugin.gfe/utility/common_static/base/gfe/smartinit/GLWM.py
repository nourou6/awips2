##
##

##
# This is a base file that is not intended to be overridden.
#
# This file can be subclassed to override behavior. Please see the 
# Configuration Guides->Smart Initialization Configuration section of the GFE 
# Online Help for guidance on creating a new smart init 
##

from Init import *

##--------------------------------------------------------------------------
## Module that calculates surface weather elements from GLWM model
## output.
##
##--------------------------------------------------------------------------
class GLWMForecaster(Forecaster):
    def __init__(self):
        Forecaster.__init__(self, "GLWM", "GLWM")

##--------------------------------------------------------------------------
##  Calculates Significant wave height of combined wind waves and swells
##--------------------------------------------------------------------------
    def calcSigWaveHgt(self, htsgw_SFC):
        # Convert meters to feet
        grid = htsgw_SFC * 3.281

        # Return the new value
        return grid

##--------------------------------------------------------------------------
##  Calculates Significant wave height of wind waves
##--------------------------------------------------------------------------
    def calcWindWaveHgt(self, wvhgt_SFC):
        # Convert meters to feet
        grid = wvhgt_SFC * 3.281

        # Return the new value
        return grid

##--------------------------------------------------------------------------
##  Calculates Direction of wind waves.
##--------------------------------------------------------------------------
    def calcWindWaveDir(self, wvdir_SFC):
        # use constant speed for display purpose only
        mag = where(logical_and(less(wvdir_SFC, 360), greater(wvdir_SFC, 0)), float32(10.0), float32(-9999.0))
        dir = clip(wvdir_SFC, 0, 360)
        return (mag, dir)

##--------------------------------------------------------------------------
##  Calculates Wind wave peak period
##--------------------------------------------------------------------------
    def calcWindWavePeriod(self, wvper_SFC):
        return clip(wvper_SFC, 0, 100)


def main():
    GLWMForecaster().run()