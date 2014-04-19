This readme explains how to use Ordinance survey open data to generate postcode area maps of the UK using QGIS, and how to use the generated maps to create choropleth maps on google Fusion Tables.

Specifically it covers:
* Where to get Ordinance Survey open data and which products you will need.
* How to use the scripts in this repo to prepare the Ordinance Survey data for use in QGIS.
* How to use QGIS to create postcode area maps from the Ordinance Survey data.
* How to export the postcode area maps from QGIS for use with Google Fusion Tables.
* How to prepare data for use in Fusion Tables, and how to create a choropleth map.


## Get the Ordinance Survey Data
Go to the [OS OpenData Download page](https://www.ordnancesurvey.co.uk/opendatadownload/products.html) and select the Boundary-Line™ and Code-Point® Open products for download. You will need to fill out a form stating you agree to the terms of use and provide an email to which download links will be sent. 

When the email arrives download the two files, clone this repo, and extract bdline_gb.zip and codepo_gb.zip into the Boundary_line and Codepoint directories respectively.
