# Author:  Bryon Kenne
# Date: 9/8/2017
# Purpose:  Print the name of the feature class


# Import ArcPy
import arcpy

# Set the workspace
arcpy.env.workspace = r"c:\school\Assignment2\Newark.gdb"

# List all of the feature classes in the Newark geodatabase
datasets = arcpy.ListDatasets(feature_type='feature')
datasets = [''] + datasets if datasets is not None else []

# Iterate through all the feature classes and print the name of each feature class
for ds in datasets:
    for fc in arcpy.ListFeatureClasses(feature_dataset=ds):
        print(fc)

# Print "Complete"
print("Complete")

