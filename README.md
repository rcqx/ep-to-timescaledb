# E+ timeseries to timescaleDB

Time series in EnergyPlus facilitate data exchange of simulation outputs. However, persistent file-based approaches
hinder integration of BPS/AECO data. This is reflected
in the inhability of sim outputs to be retrieved by stakeholders 
during different stages of a building life cycle. This makes BPS practice a repetitive and bulky task. 

Thus, as migration from files to integrated data-based approaches is increasing data-level interoperability within different systems,
the use of Semantic Web Technologies (SWT) is gainining traction in the AECO. 
SWT permit the creation of linked-data models over the web under W3C standards 
(RDF, OWL, SPARQL, SKOS); facilitating understanding among 
disperse and heterogenous data sources.

BPS community can take advantage of SWT to transfer BPS data
to linked building representations (semantic models) for establishing more
efficient approaches to BPS/AECO data exchange. In other words, thru linked-data
models BPS information can be retrieved by the involved actors during different stages
of a building development.

This repo is based on [brick's data retrieval demo](https://github.com/gtfierro/brick-data-retrieval-demo) by [gtfierro](https://github.com/gtfierro);
which uses BMS points data, [brickschema](https://brickschema.org/) and jupyter/timescaledb docker images.

In this particular example:

* An [EnergyPlus](https://energyplus.net/) model of an single storey
office with 5 HVAC zones is simulated to report every zone temperature during the hottest day of the
year. 
* An ``Output:Variable`` object report the timeseries corresponding to the temperatures of every zone in the model.
* Timeseries data allocated in .csv file is then post-process to report time, zone temperature and an id corresponding to the simulated zone.
* Then a semantic representation of the office is created using [bot](https://w3c-lbd-cg.github.io/bot/) schema for describing the office topology 
* Timeseries ids corresponding to .csv files are mapped into the semantic model. 
* Time series data is loaded to timescaledb
* Semantic model and its relationships to timeseries data  are discovered, arrange and plotted. 

More info on the energy model can be found on e+ "./ExampleFiles/BasicFiles/exercise2.idf" and
on the ["Getting Started"](https://energyplus.net/sites/default/files/pdfs_v8.3.0/GettingStarted.pdf) guide.

To gain access to exercise, first start docker containers:

```
# start docker containers
./scripts/start_docker_containers.sh
```

Then load energyplus timseries data 

```
# load energyplus timeseries data
./scripts/setup.sh
```









 
