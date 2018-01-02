# This Python 2.x script assumes 
# - you downloaded california-latest-free.shp.zip # from Geofabrik.
# (http://download.geofabrik.de/north-america/us/california-latest-free.shp.zip)
# - You used the OSGEO4W installation of QGIS

import os, zipfile, subprocess

#Set the current working folder
thisfolder = os.getcwd()

# Extracts only the roads shapefile
geofabrik = zipfile.ZipFile("california-latest-free.shp.zip")
geofabrik.extract("gis.osm_roads_free_1.cpg")
geofabrik.extract("gis.osm_roads_free_1.dbf")
geofabrik.extract("gis.osm_roads_free_1.prj")
geofabrik.extract("gis.osm_roads_free_1.shp")
geofabrik.extract("gis.osm_roads_free_1.shx")

geofabrik.close()

# rename the shapefile to prep for geoprocessing
os.rename('gis.osm_roads_free_1.cpg', 'osm_roads_free_1.cpg')
os.rename('gis.osm_roads_free_1.dbf', 'osm_roads_free_1.dbf')
os.rename('gis.osm_roads_free_1.prj', 'osm_roads_free_1.prj')
os.rename('gis.osm_roads_free_1.shp', 'osm_roads_free_1.shp')
os.rename('gis.osm_roads_free_1.shx', 'osm_roads_free_1.shx')

# set your CMD environment to run GDAL geoprocessing scripts
subprocess.call('C:/OSGeo4W64/bin/o4w_env.bat')

# Use ogr2ogr to convert your shapefile to a geopackage
# First, create a string to run...
callstring = 'C:/OSGeo4W64/bin/ogr2ogr.exe -f GPKG osm_roads.gpkg '
callstring += '-nln roads osm_roads_free_1.shp -sql '
callstring += '"SELECT * FROM osm_roads_free_1 WHERE name is not null"'

# Now call the string
subprocess.call(callstring)

# Use ogr2ogr to replace your shapefile with only streets with names
# Create a string to run...
callstring_shp = 'C:/OSGeo4W64/bin/ogr2ogr.exe osm_roads.shp '
callstring_shp += 'osm_roads_free_1.shp -sql '
callstring_shp += '"SELECT * FROM osm_roads_free_1 WHERE name is not null"'

# Now call the string
subprocess.call(callstring_shp)

# Remove shapefiles that have no street names
os.remove('osm_roads_free_1.cpg')
os.remove('osm_roads_free_1.dbf')
os.remove('osm_roads_free_1.prj')
os.remove('osm_roads_free_1.shp')
os.remove('osm_roads_free_1.shx')
