# Using Graph Databases for Event Data

## Installation
### PromG
The library can be installed in Python using pip
`pip install promg`.

The source code for PromG can be found [PromG Core Github repository](https://github.com/PromG-dev/promg-core).

### Neo4j
The library assumes that Neo4j is installed.

Install [Neo4j](https://neo4j.com/download/):

- Use the [Neo4j Desktop](https://neo4j.com/download-center/#desktop)  (recommended), or
- [Neo4j Community Server](https://neo4j.com/download-center/#community)

## Get started

### Create a new graph database

- Configuration; `config.yaml`
  - Set the URI in `config.yaml` to the URI of your server. Default value is `bolt://localhost:7687`.
  - Set the password in `config.yaml` to the password of your server. Default value is `12345678`.
  - Set the import directory in `config.yaml` to the import directory of your Neo4j server
    - To determine the import directory of your Neo4j server
      1. Select the database in Neo4j desktop
      2. Click the three dots
      3. Select `Open Folder`
      4. Select `Import`
      5. This opens the import directory, so now you can copy the directory. 
- Ensure to allocate enough memory to your database, advised: `dbms.memory.heap.max_size=5G`
- Install APOC (see https://neo4j.com/labs/apoc/)
  - Install `Neo4j APOC Core library`: 
    1. Select the database in Neo4j desktop 
    2. On the right, click on the `plugins` tab
    3. Open the `APOC` section
    4. Click the `install` button
    5. Wait until a green check mark shows up next to `APOC` - that means it's good to go!
  - Install `Neo4j APOC Extended library`
    1. Download the [appropriate release](https://github.com/neo4j-contrib/neo4j-apoc-procedures/releases) (same version numbers as your Neo4j version)
       1. Look for the release that matches the version number of your Neo4j Database.
       2. Download the file `apoc-[your neo4j version]-extended.jar`
    2. Locate the `plugins` folder of your database
       1. Select the database in Neo4j desktop
       2. Click the three dots
       3. Select `Open Folder`
       4. Select `Plugins`
    3. Put `apoc-[your neo4j version]-extended.jar` into the `plugins` folder of your database
    4. Restart the server (database)
  - Configure extra settings using the configuration file `$NEO4J_HOME/conf/apoc.conf`
    1. Locate the `conf` folder of your database
         1. Select the database in Neo4j desktop
         2. Click the three dots
         3. Select `Open Folder`
         4. Select `Conf`
    2. Create the file `apoc.conf`
    3. Add the following line to `apoc.conf`: `apoc.import.file.enabled=true`.

## Data set specific information
We provide data and scripts for BPI Challenge 2017; store the original data in CSV format in the directory `/data`.
The datasets are available from:

            Esser, Stefan, & Fahland, Dirk. (2020). Event Data and Queries
            for Multi-Dimensional Event Data in the Neo4j Graph Database
            (Version 1.0) [Data set]. Zenodo. 
            http://doi.org/10.5281/zenodo.3865222

## JSON 
- **json_files/BPIC17.json** - json file that contains the semantic header for BPIC17
- **json_files/BPIC17_DS.json** - json file that contains a description for the different datasets for BPIC17 (event
  tables etc)

Furthermore, we provide: 

- **file_preparation/bpic17_prepare.py** - normalizes the original CSV data to an event table in CSV
  format required for the import and stores the output in the directory `ROOT/data/prepared/`

### main script
There is one script that creates the Event knowledge graph: **main.py**

This script imports normalized event table of BPIC17 from CSV files and executes several data modeling queries to construct an event knowledge graph using the semantic header.

How to use
----------

For data import

1. Set the configuration in `config.yaml`. 
   - For database settings, see [Create a new graph database](### Create a new graph database).
   - Set `use_sample` to True/False
2. start the Neo4j server
3. run main.py

