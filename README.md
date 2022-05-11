# LA-Cap-and-Trade


## Background and Purpose
### **Background**

The state of California utilizes a cap-and-trade program to help reduce CO2 emissions across the state. Administered by the California Air Resources Board (ARB), yearly reports come out at two levels, the entity and facility level. Entities are the overarching organizations, such as Exxon-Mobile or the Los Angeles Department of Water, and have an Entity ID. Each entity is made up of a facility or multiple facilities and are assigned an ARBID. Information is provided yearly at facility levels but not yearly at an entity level.
### **Purpose**
The goal of the project is to:
  * Combine yearly reports into a single dataset
  * Link the data to coordinates from other dataset
  * Calculate total entity emissions for every year
  * Create a geopackage that combines new datasets and the Enviroscreen of LA County
## Inputs
All input data is provided in the folder `Input_Data`. All input files are up to date as of 5/11/2022.

To update the data regarding facility level data (ie: 2020-ghg-emissions-2021-11-04.xlsx), go to the [Mandatory GHG Reporting ARB page](https://ww2.arb.ca.gov/mrr-data).

To update entity level data (2019compliancereport.xlsx), for times when there are changes to facilities owned by an entity, go to [Cap-And-Trade Program Data](https://ww2.arb.ca.gov/our-work/programs/cap-and-trade-program/cap-and-trade-program-data) under the heading `Compliance Reports`


To update the file used for geographic information (FacilityEmissions.csv), go to the [Pollution Mapping Tool](https://www.arb.ca.gov/ei/tools/pollution_map/#), go to the `county` field and filter to `Los Angeles`. From there, click on the `Data` tab and use the `Group by` option for facility. Once complete, click `Get Data`

To update the EnviroScreen file, go to [the CalEnviroScreen 4.0 page](https://oehha.ca.gov/calenviroscreen/report/calenviroscreen-40). At the very bottom of the page is the `Downloads` heading, using the SHP file version.

## Scripts
The primary scripts are numbered in order of dependency. After running the scripts starting from 1-4, there are two optional scripts, marked opt, that creates base graphs to better understand the data. Detailed information about output files will be discussed in the **Outputs** section.
### `01-aggregation.py`

This script takes the yearly facility level data and merges it to create one unified dataset. To do so, it requires a dictionary of each file name and how many rows it needs to go down until the header row starts.
```
files = {
    '2011-ghg-emissions-2018-11-05.xlsx': {'header':8},
    '2012-ghg-emissions-2019-11-04.xlsx': {'header':8},
    '2013-ghg-emissions-2019-11-04.xlsx': {'header':8},
    '2014-ghg-emissions-2019-11-04.xlsx': {'header':8}, 
    '2015-ghg-emissions-2019-11-04.xlsx': {'header':8},
    '2016-ghg-emissions-2020-11-04.xlsx': {'header':8},
    '2017-ghg-emissions-2020-11-04.xlsx': {'header':8},
    '2018-ghg-emissions-2021-11-04.xlsx': {'header':8},
    '2019-ghg-emissions-2021-11-04.xlsx': {'header':9},
    '2020-ghg-emissions-2021-11-04.xlsx': {'header':8}
    }
```
If any files are added, it would need to be added to this dictionary as well and the header is 0-indexed. The script will interpret what year the data is from beginning of the file name, which is needed for the corresponding sheet. The script also cleans all heading columns, removing new lines and renaming columns for ease of use later. It also filters down data to just aggregate CO2 information and other identifiers in the output file `Stack_Ag_Emit.csv`.

### `02-percentage.py`

This script utilizes the output of `01-aggregation.py` and `2019compliancereport.xlsx` to calculate total entity emissions for every year. To do so, the `ARB GHG ID` column of `2019compliancereport.xlsx` is needed. All white space is removed then split on commas to create a list of ARBIDs. While not used in this project again, this version of the DataFrame is saved as `Entities_ARBID.csv`. The DataFrame is then exploded on `ARBID` then merged on to the emission data to sum, which allows the script to sum the total of each entity each year. Each facility total is associated with each one of its entities, which allows for a percentage of the facility emissions and the entity emissions to be found. The resulting data is saved to `Pct_Data.csv`.

### `03-merging`

This script utilizes the output of `02-percentage.py` and the file `FacilityEmissions.csv` to add geographic data onto the existing data. It does so by dropping most of the data from `FacilityEmissions.csv` except for a few columns to verify the information matches and the coordinates. It also filters out any facility that is not subject to cap-and-trade. The resulting output file is `geo_merged.csv`.

### `04-mapping`

This script utilizes the `calenviroscreen40shpf2021shp.zip` input file and the output of `03-merging`. The script first filters LA County out of the shape file and writes it to the `Enviroscreen_LA` layer of the output file. It then converts all of the data to GeoDataFrames to then write it to the `All Year Data` layer. Finally, the script does a similar process for every year and creates a separate year for emissions to its corresponding layer.
___
### `opt-analyze` and `opt-percentage_math`
These scripts serve similar functions. Each script determines either the highest emitter in terms of total covered emissions or the facilities with the lowest share of total emissions and outputs corresponding bar graphs.
## Outputs
### `Stack_Ag_Emit.csv`

### `Pct_Data.csv`

## Results
aaa
