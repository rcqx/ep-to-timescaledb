# EP timeseries 

### Rationale

Time series data in [EnergyPlus](https://energyplus.net/sites/all/modules/custom/nrel_custom/pdfs/pdfs_v9.5.0/EnergyPlusEssentials.pdf) 
is given in CVS, TAB or TXT files. These outputs come from the 
``Output:Variable`` input object to facilitate readability an data exchange 
among different stakeholders. 

However, as AECO industry is currently constrainted 
to document-based methodologies, interoperability at a data-level still 
represents an obstacle. In the BEM community, specifically, this is reflected
by the lack of integration of valuable information into 
different stages of a building life cycle. 

To address this, the use of Semantic Web Technologies (SWT)
is gaining traction in the AECO industry. SWT permit the 
creation of linked-data models over the web, these flexible models, created 
under W3C standards (RDF, OWL, SPARQL, SKOS), facilitate data integration of 
disperse and heterogenous sources.

BEM community can take advantage of these technologies and transfer data outputs 
from simulations to linked building data models, and thus, establish more
integrated approaches to BEM/AECO practice. These simulation outputs can be
embedded into semantic descriptions and then data can then retrieved/queried 
by other stakeholders. Hence, in this repo, an example of how to transform an 
[EnergyPlus](https://energyplus.net/) simulation output of an unconditioned 
single zone building is proposed.

The exercise is inspired by [Gabe Fierro's data retrieval demo] (https://github.com/gtfierro/brick-data-retrieval-demo) 


 
