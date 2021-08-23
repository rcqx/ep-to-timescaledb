# EP timeseries 

Time series data in EnergyPlus 
is given in CVS, TAB or TXT files. These outputs come from the 
``Output:Variable`` object to facilitate readability an data exchange.
However, as AECO industry is currently constrainted 
to file-based methodologies, interoperability at data-level still 
represents an obstacle. In the BEM community, specifically, this is reflected
by the lack of integration of simulation outputs into 
different stages of a building life cycle. 

To address this, the use of Semantic Web Technologies (SWT)
is gaining traction in the construction industry. SWT permit the 
creation of linked-data models over the web, these flexible models are created 
under W3C standards (RDF, OWL, SPARQL, SKOS) and facilitate data integration of 
disperse and heterogenous sources.

BEM community can take advantage of these technologies and transfer simulated data
to linked models, and thus, establish more
integrated approaches to BEM/AECO practice. These outputs can be
embedded into semantic descriptions to be  retrieved/queried 
by other stakeholders. 

This repo contains an example of how [EnergyPlus](https://energyplus.net/) simulation 
outputs can be extracted and shared thru linked data models.

############

 #################
and all the information in regard of the used model can be found on the .idf file. Finally,
the exercise is inspired and uses some of the scripts provided in 
[Gabe Fierro's data retrieval demo](https://github.com/gtfierro/brick-data-retrieval-demo). 







 
