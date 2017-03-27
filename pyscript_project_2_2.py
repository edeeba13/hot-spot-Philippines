#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      deeba
#
# Created:     27/03/2017
# Copyright:   (c) deeba 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# AddField

import arcpy

# Set environment settings
arcpy.env.workspace = r"E:\P in GIS\Project_2_2\Project_2_Option_2.gdb"

# Set local variables
inFeatures = "Philippines"
fieldName1 = "Date"
fieldType = "DATE"

arcpy.AddField_management(inFeatures, fieldName1, fieldType)


import numpy

in_fc = r"E:\P in GIS\Project_2_2\Project_2_Option_2.gdb\Philippines"
field1 = "iday"
field2 = "imonth"
field3 = "iyear"

import arcpy.da
array1 = arcpy.da.FeatureClasstoNumPyArray(in_fc, [field1, field2, field3])

sr = arcpy.SpatialReference()
outFC = r"E:\P in GIS\Project_2_2\Project_2_Option_2.gdb\Philippines\date"



arcpy.da.NumPyArrayToFeatureClass(array1, outFC, ['Date'], sr)


try:

    # Create Space Time Cube
output_cube = r"E:\P in GIS\Project_2_2\Project_2_Option_2.gdb\Philippines.nc

#from above, populated FC with "Date"
time_field = outFC

#not sure if SPACE_TIME_NEIGHBORS is an appropriate summary field
cube = CreateSpaceTimeCube_stpm(in_fc, output_cube, time_field, SPACE_TIME_NEIGHBORS)

    # Create a polygon that defines where incidents are possible
    # Process: Minimum Bounding Geometry of homicide incident data
arcpy.MinimumBoundingGeometry_management("Philippines.shp", "bounding.shp", "CONVEX_HULL",
                                             "ALL", "#", "NO_MBG_FIELDS")
#i don't think i need the code below
##    # Emerging Hot Spot Analysis of homicide incident cube using 5 Miles neighborhood
##    # distance and 2 neighborhood time step to detect hot spots
##    # Process: Emerging Hot Spot Analysis
##cube = arcpy.EmergingHotSpotAnalysis_stpm("Homicides.nc", "COUNT", "EHS_Homicides.shp",
##                                              "5 Miles", 2, "bounding.shp")
##
##except arcpy.ExecuteError:
##    # If any error occurred when running the tool, print the messages
##    print(arcpy.GetMessages())