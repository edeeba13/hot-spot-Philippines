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
import arcpy
#import numpy

# Set environment settings
arcpy.env.workspace = r"C:\Users\greg6750\Documents\hot-spot-Philippines-emily\Project_2_Option_2.gdb"#r"E:\P in GIS\Project_2_2\Project_2_Option_2.gdb"
in_fc = r"C:\Users\greg6750\Documents\hot-spot-Philippines-emily\Project_2_Option_2.gdb\Philippines"#r"E:\P in GIS\Project_2_2\Project_2_Option_2.gdb\Philippines"
outFC = r"C:\Users\greg6750\Documents\hot-spot-Philippines-emily\Project_2_Option_2.gdb\Philippines_wDate"#r"E:\P in GIS\Project_2_2\Project_2_Option_2.gdb\Philippines\date"
output_cube = r"C:\Users\greg6750\Documents\hot-spot-Philippines-emily\spacetimecube.nc" #r"E:\P in GIS\Project_2_2\Project_2_Option_2.gdb\Philippines.nc"


# Set local variables
fieldName1 = "Date"
fieldType = "DATE"
field1 = "iday"
field2 = "imonth"
field3 = "iyear"

##Dont need this
##array1 = arcpy.da.FeatureClassToNumPyArray(in_fc, [field1, field2, field3]) #arcpy.da.FeatureClassToNumPyArray
##sr = arcpy.Describe(in_fc).SpatialReference
##arcpy.da.NumPyArrayToFeatureClass(array1, outFC, ['Date'], sr)

#If field exists, add field
try:
    field = arcpy.ListFields(fieldName1)
except:
    field = fieldName1

if len(field)>0:
    arcpy.AddField_management(in_fc, fieldName1, fieldType)

#field calculation to populate time field
expression = "time.strftime(' !iday! / !imonth! / !iyear! ')"
newTerrorData = arcpy.CalculateField_management(in_fc, fieldName1, expression, "PYTHON")

# Create Space Time Cube
#not sure if SPACE_TIME_NEIGHBORS is an appropriate summary field
cube = arcpy.CreateSpaceTimeCube_stpm(in_fc, output_cube, fieldName1) #,"","6 Months","END_TIME", "","","")

# Create a polygon that defines where incidents are possible
# Process: Minimum Bounding Geometry of homicide incident data
#arcpy.MinimumBoundingGeometry_management("Philippines.shp", "bounding.shp", "CONVEX_HULL",
                                             #"ALL", "#", "NO_MBG_FIELDS")
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