# DisasterEvacuations
This is a very brief guide for identifying evacuated areas with <a href="https://www.openstreetmap.org/about">OpenStreetMap</a> data.

Disasters, like wildfires, are at times the most dangerous and unpredictable in their early stages. In a rush, the only way to get polygons of evacuated areas quickly is to select multiple sets of streets using desktop software like QGIS or <a href="https://pro.arcgis.com/en/pro-app/">ArcGIS Pro</a>.

1. Install <a href="https://qgis.org/en/site/index.html">QGIS</a> (OSGEO4W installation).
2. Download your state's OpenStreetMap data from Geofabrik. This example and GDAL Python script uses <a href="http://download.geofabrik.de/north-america/us/california.html">California</a> (California-latest-free.shp.zip, about 1.3 GB).
3. Create a folder on your local drive (e.g. C:\myfiles\gisdata\osm) and move your downloaded ZIP file there.
4. Download extract_roads.py from this repository to your local folder.
5. Running extract_roads.py should create a statewide geopackage from road features in your download that have street names. Unnamed road featrues are filtered out.
6. Add the geopackage to your QGIS, ArcMap or ArcGIS Pro just like you would any feature class. Chose any basemap you wish.
7. Selecting multiple streets to get patterns is simple, e.g. "name" in ('Imperial Highway', 'Norwalk Boulevard', 'Bloomfield Avenue') Consult your desktop GIS docs.
8. When you are confident you see the pattern of the area to be evacuated, create and draw a new polygon shapefile, WinZip, and send it in to whoever may need it.

<p>Note the small file size and speed of the geopackage file format, which includes spatial indexing.</p>
<p>Geopackage Home Page: <a href="http://www.geopackage.org/">http://www.geopackage.org/</a></p>
<p>Gepackage GDAL Reference: <a href="http://www.gdal.org/drv_geopackage.html">http://www.gdal.org/drv_geopackage.html</a><p/>
