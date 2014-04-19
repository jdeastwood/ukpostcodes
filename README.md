This readme explains how to use Ordinance survey open data to generate postcode district maps of the UK using QGIS, and how to use the generated maps to create choropleth maps on google Fusion Tables.

Specifically it covers:
* Where to get Ordinance Survey open data and which products you will need.
* How to use the scripts in this repo to prepare the Ordinance Survey data for use in QGIS.
* How to use QGIS to create postcode district maps from the Ordinance Survey data.
* How to export the postcode area maps from QGIS for use with Google Fusion Tables.
* How to prepare data for use in Fusion Tables, and how to create a choropleth map.


## Get the Ordinance Survey Data
Go to the [OS OpenData Download page](https://www.ordnancesurvey.co.uk/opendatadownload/products.html) and select the Boundary-Line™ and Code-Point® Open products for download. You will need to fill out a form stating you agree to the terms of use and provide an email to which download links will be sent. 

When the email arrives download the two files, clone this repo, and extract bdline_gb.zip and codepo_gb.zip into the Boundary_line and Codepoint directories respectively.

## Prepare the OS CodePoint data for QGIS
The Codepoint data isn't entirely consistent in it's formatting and also contains a few less interesting columns. The data is found in Codepoint/Data/CSV/ and is organized into csv files for each postcode area (e.g. EH). combine.py will combine these csvs as well as clean up the postcodes, and remove columns other than the northings and eastings (British National grid coordinates). See combine.py for example usage, for the first run I recommend using only a small set of postcode areas as generating the maps can take some time! The rest of this readme will assume you have done the following:
```bash
./combine.py ./Codepoint/Data/CSV/eh.csv > eh_clean.csv
``` 

## Generate district maps

First [download QGIS](http://www.qgis.org/en/site/) and install it. Open QGIS and creat a new project, save the project as postcode_districts.

You fisrt need to add a map to work on; in QGIS select Layer > Add Vector Layer and enter Boundary_line/Data/european_region_region.shp as the source dataset. This will add a UK map layer.

Now add the postcode data. Select Layer > Add Delimited Text Layer and set eh_clean.csv as the filename. N.B that you may need to change the X Field And Y field in the geometry definition section to X = northing and Y = easting. Otherwise you can just press OK. This will bring up a window asking you to set a Coordinate Reference System, you want **OSGB 1936 / British National Grid**. Click OK and points corresponding to the postcodes will be added to the map.

Next select Vector > Geometry Tools > Voroni Polygons. Set the output file to unmerged.shp and check the "add result to canvas option". Click OK and when the coordinate system selector appears, select British National Grid.

This will add a later to the map with a polygon for each postcode, these now need to be merged together by district. Select Vector > Geoprocessing Tools > Dissolve. Select unmerged as the input layer, set the output file to districts.shp, and check the "add result to canvas option".
