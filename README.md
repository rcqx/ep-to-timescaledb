# EP timeseries 

### Rationale

Time series data in EnergyPlus 
is given in CVS, TAB or TXT files. These outputs come from the 
``Output:Variable`` input object to facilitate readability an data exchange 
among different stakeholders. However, as AECO industry is currently constrainted 
to file-based methodologies, interoperability at data-level still 
represents an obstacle. In the BEM community, specifically, this is reflected
by the lack of integration of simulation outputs into 
different stages of a building life cycle. 

To address AECO heterogeinity, the use of Semantic Web Technologies (SWT)
is gaining traction. SWT permit the 
creation of linked-data models over the web, these flexible models are created 
under W3C standards (RDF, OWL, SPARQL, SKOS) and facilitate data integration of 
disperse and heterogenous sources.

BEM community can take advantage of these technologies and transfer data outputs 
from simulations to linked building data models, and thus, establish more
integrated approaches to BEM/AECO practice. These outputs can be
embedded into semantic descriptions and then data can then retrieved/queried 
by other stakeholders. Hence, in this repo, an example of how to transform an 
[EnergyPlus](https://energyplus.net/) simulation output of an unconditioned 
single zone building is showcased.

The exercise uses the unconditioned single zone file in EnergyPlus 9.5 ExampleFiles folder
and all the information in regard of the used model can be found on the .idf file. Finally,
the exercise is inspired and uses some of the scripts provided in 
[Gabe Fierro's data retrieval demo] (https://github.com/gtfierro/brick-data-retrieval-demo). 







 
