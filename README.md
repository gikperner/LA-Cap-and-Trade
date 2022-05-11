# LA-Cap-and-Trade


## Background and Purpose
___
### **Background**

The state of California utilizes a cap-and-trade program to help reduce CO2 emissions across the state. Administered by the California Air Resources Board (ARB), yearly reports come out at two levels, the entity and facility level. Entities are the overarching organizations, such as Exxon-Mobile or the Los Angeles Department of Water, and have an Entity ID. Each entity is made up of a facility or multiple facilities and are assigned an ARBID. Information is provided yearly at facility levels but not yearly at an entity level.
### **Purpose**
The goal of the project is to:
  * Combine yearly reports into a single dataset
  * Link the data to coordinates from other dataset
  * Calculate total entity emissions for every year
  * Create a geopackage that combines new datasets and the Enviroscreen of LA County
## Inputs
___
All input data is provided in the folder `Input_Data`. All input files are up to date as of 5/11/2022.

To update the data regarding facility level data (ie: 2020-ghg-emissions-2021-11-04.xlsx), go to the [Mandatory GHG Reporting ARB page](https://ww2.arb.ca.gov/mrr-data).

To update entity level data (2019compliancereport.xlsx), for times when there are changes to facilities owned by an entity, go to [Cap-And-Trade Program Data](https://ww2.arb.ca.gov/our-work/programs/cap-and-trade-program/cap-and-trade-program-data) under the heading `Compliance Reports`

To update the file used for geographic information (FacilityEmissions.csv), go to the [Pollution Mapping Tool](https://www.arb.ca.gov/ei/tools/pollution_map/#), go to the `county` field and filter to `Los Angeles`. From there, click on the `Data` tab and use the `Group by` option for facility. Once complete, click `Get Data`

To update the EnviroScreen file, go to [the CalEnviroScreen 4.0 page](https://oehha.ca.gov/calenviroscreen/report/calenviroscreen-40). At the very bottom of the page is the `Downloads` heading, using the SHP file version.

## Scripts
___
The primary scripts are numbered in order of dependency. After running the scripts starting from 1-4, there are two optional scripts, marked opt, that creates base graphs to better understand the data.
### `01-aggregation.py`

This script takes the yearly facility level 
## Outputs
___
aaa
## Results
___
aaa