# JPL_Dashboard_UCR_Fellowship_2022

## Table of Contents
- [Overview](#overview)
- [How To Run](#how-to-run)
- [Usage](#usage)
- [Diagrams](#diagrams)
- [Dependencies](#dependencies)
- [Authors and Acknowledgment](#authors-and-acknowledgment)

## Overview
In recent years, there has been a significant increase in groundwater pumping in the Central Valley area. This area is known as an agricultural hub that now suffers from land subsidence due to the excess pumping of groundwater. NASA JPL has been tracking the land deformation from 2014 to 2019. We were given snapshots of data for every two weeks within the five year period. The data provided to us includes longitude, latitude, displacement, and precipitation of the Central Valley region. With this data, our goal is to analyze the data and create animated heatmaps and graphs that show changes over time. We want to show the relationship between all the facts and clearly show the effect of groundwater pumping on land subsidence. All the maps, graphs, and animations will be added to a local website that will display the dashboard.

## Team
* Corona, Jason; BS in Computer Science at UCR (https://github.com/JasonC-tech)
* Darch, Lili; BS in Computer Science at RCCD (https://github.com/LiliD001)
* Miyazaki, Haruki; BS in Computer Science at UCR (https://github.com/HarukiMiya)
* Rakesh, Ishika; BS in Computer Science with Business Applications at UCR (https://github.com/rakishika)


## How To Run
* First, download and install all the necessary tools/software listed under the dependencies. 
* Next, clone the github repository and run the code: ```python manage.py runserver```
* This will start up a development server for this django project.
* Lastly, Open a web browser with the given url link: ```http://127.0.0.1:8000/```

## Usage

## Diagrams

## Dependencies
Install Django. The documentation can be found on their website [here](https://docs.djangoproject.com/en/4.0/topics/install/).\
Install PostgreSQL 14. It can be found directly on their website [here](https://www.postgresql.org/download/).\
Install pgAdmin 4. This can also be found directly on their website [here](https://www.pgadmin.org/download/).\
Download the CSV file "InSAR_classification.csv". This can be found [here](https://drive.google.com/file/d/16-IoFQkVOHvRwyuKz8qgV-cgfmFcNwL8/view?usp=sharing) and move it in static folder.\
Download the CSV file "InSAR_20190122.csv". This can be found [here](https://drive.google.com/file/d/1XOCf7DHEuD0aVvRPsYFjhilpGFu1g3JH/view?usp=sharing) and move it in static folder.\
Download the CSV file "InSAR_waterground.csv". This can be found [here](https://drive.google.com/file/d/1zw-rAUJE5hARRGc-clkY2xYNgDYQoZ-_/view?usp=sharing) and move it in static folder.\
Download the CSV file "InSAR_Data.csv". This can be found [here](https://drive.google.com/file/d/1VssVSU-Ijm6YoDmv3syT4DZZoeiAIQhV/view?usp=sharing).

Open pgAdmin 4 and when prompted set the password to "binary0111".
In pgAdmin 4, follow the path dashboard_db -> Schemas -> public -> Tables.
Right click on Tables and click Query tool.
Create a table titled "time_series_data" by running the following code in Query tool:
```
CREATE TABLE time_series_data 
(
    lon character varying(140),
    lat character varying(140),
    "20141108" real,
    "20141202" real,
    "20141226" real,
    "20150212" real,
    "20150308" real,
    "20150401" real,
    "20150425" real,
    "20150519" real,
    "20150612" real,
    "20150706" real,
    "20150730" real,
    "20150823" real,
    "20150916" real,
    "20151010" real,
    "20151103" real,
    "20151127" real,
    "20151209" real,
    "20151221" real,
    "20160114" real,
    "20160126" real,
    "20160207" real,
    "20160219" real,
    "20160302" real,
    "20160314" real,
    "20160326" real,
    "20160407" real,
    "20160419" real,
    "20160501" real,
    "20160513" real,
    "20160525" real,
    "20160606" real,
    "20160630" real,
    "20160724" real,
    "20160817" real,
    "20160910" real,
    "20160922" real,
    "20161004" real,
    "20161016" real,
    "20161028" real,
    "20161109" real,
    "20161121" real,
    "20161203" real,
    "20161215" real,
    "20161227" real,
    "20170108" real,
    "20170114" real,
    "20170120" real,
    "20170126" real,
    "20170201" real,
    "20170213" real,
    "20170225" real,
    "20170309" real,
    "20170321" real,
    "20170402" real,
    "20170414" real,
    "20170426" real,
    "20170508" real,
    "20170520" real,
    "20170601" real,
    "20170613" real,
    "20170625" real,
    "20170707" real,
    "20170719" real,
    "20170731" real,
    "20170812" real,
    "20170824" real,
    "20170905" real,
    "20170917" real,
    "20170929" real,
    "20171011" real,
    "20171023" real,
    "20171104" real,
    "20171116" real,
    "20171128" real,
    "20171210" real,
    "20171222" real,
    "20180103" real,
    "20180115" real,
    "20180127" real,
    "20180208" real,
    "20180220" real,
    "20180304" real,
    "20180316" real,
    "20180328" real,
    "20180409" real,
    "20180421" real,
    "20180503" real,
    "20180515" real,
    "20180527" real,
    "20180608" real,
    "20180620" real,
    "20180702" real,
    "20180714" real,
    "20180726" real,
    "20180807" real,
    "20180819" real,
    "20180831" real,
    "20180912" real,
    "20180924" real,
    "20181006" real,
    "20181018" real,
    "20181030" real,
    "20181111" real,
    "20181117" real,
    "20181123" real,
    "20181205" real,
    "20181217" real,
    "20181229" real,
    "20190110" real,
    "20190122" real
)
```
This will create all the necessary columns for the dataset.

Now, right click on the newly created table and Import the CSV file "InSAR_Data.csv".

Now, run the following code on Query tool:
```
  SELECT * FROM time_series_data
```
You should now be able to see all the data.

## Authors and Acknowledgment
