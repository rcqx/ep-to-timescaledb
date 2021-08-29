from rdflib import RDF, RDFS, OWL, Namespace, Graph
from rdflib.term import BNode

g = Graph()

g.parse("./EP_timeseries.ttl", format="ttl")

# Fetch Sensors in zones
site = g.query("""
    SELECT ?zone ?sensor WHERE {
        ?zone a bot:Zone .
        ?zone bot:hasElement ?sensor .
        ?sensor a bot:Element .
    }
""")
for row in site:
    print(row)

# Fetch timeseries
qres = g.query("""
SELECT ?ts ?tsid WHERE {
    ?ts a bot:Element  .
    ?ts bldg:timeseries/bldg:hasTimeseriesId ?tsid .
}""")
for row in qres:
    print(row)