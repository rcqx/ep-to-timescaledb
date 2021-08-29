from rdflib import RDF, RDFS, OWL, Namespace, Graph, Literal
from rdflib.term import BNode

g = Graph()

XSD = Namespace("http://www.w3.org/2001/XMLSchema")
g.bind("xsd", XSD)
BLDG = Namespace("http://example.com/5ZoneOffice#")
g.bind("bldg", BLDG)
BOT = Namespace("https://w3c-lbd-cg.github.io/bot#")
g.bind("bot", BOT)
UNIT = Namespace("http://qudt.org/vocab/unit/")
g.bind("unit", UNIT)

# site
g.add((BLDG.Site, RDF.type, BOT.Site))
# building
g.add((BLDG.office_building, RDF.type, BOT.Building))
# story
g.add((BLDG.office, RDF.type, BOT.Storey))
# rooms
g.add((BLDG.office_N, RDF.type, BOT.Space))
g.add((BLDG.office_S, RDF.type, BOT.Space))
g.add((BLDG.office_E, RDF.type, BOT.Space))
g.add((BLDG.office_W, RDF.type, BOT.Space))
g.add((BLDG.office_C, RDF.type, BOT.Space))
# zones
g.add((BLDG.ZONE_N, RDF.type, BOT.Zone))
g.add((BLDG.ZONE_S, RDF.type, BOT.Zone))
g.add((BLDG.ZONE_E, RDF.type, BOT.Zone))
g.add((BLDG.ZONE_W, RDF.type, BOT.Zone))
g.add((BLDG.ZONE_C, RDF.type, BOT.Zone))
# window
g.add((BLDG.window, RDF.type, BOT.Element))
# glassdoor
g.add((BLDG.glassdoor, RDF.type, BOT.Element))
# wall
g.add((BLDG.wall, RDF.type, BOT.Element))
# ceiling
g.add((BLDG.ceiling, RDF.type, BOT.Element))

# thermostats
g.add((BLDG["TS_North"], RDF.type, BOT.Element))
g.add((BLDG["TS_South"], RDF.type, BOT.Element))
g.add((BLDG["TS_East"], RDF.type, BOT.Element))
g.add((BLDG["TS_West"], RDF.type, BOT.Element))
g.add((BLDG["TS_Core"], RDF.type, BOT.Element))

# RELATIONSHIPS
# Relationships of Building
g.add((BLDG.Site, BOT.hasBuilding, BLDG.office_building))
g.add((BLDG.office_building, BOT.hasStorey, BLDG.office))

# relations for North zone
g.add((BLDG.office, BOT.hasSpace, BLDG.office_N))
g.add((BLDG.ZONE_N, BOT.hasSpace, BLDG.office_N))
g.add((BLDG.ZONE_N, BOT.hasElement, BLDG["TS_North"]))
g.add((BLDG["TS_North"], RDFS.label, Literal("Room temperature measure in North Office")))
g.add((BLDG["TS_North"], UNIT.applicableUnit, UNIT.DEG_C))
ts_ref_N = BNode()
g.add((ts_ref_N, BLDG.hasTimeseriesId, Literal("northZone")))
g.add((BLDG["TS_North"], BLDG.timeseries, ts_ref_N))

# relations for South zone
g.add((BLDG.office, BOT.hasSpace, BLDG.office_S))
g.add((BLDG.ZONE_S, BOT.hasSpace, BLDG.office_S))
g.add((BLDG.ZONE_S, BOT.hasElement, BLDG["TS_South"]))
g.add((BLDG["TS_South"], RDFS.label, Literal("Room temperature measure in South Office")))
g.add((BLDG["TS_South"], UNIT.applicableUnit, UNIT.DEG_C))
ts_ref_S = BNode()
g.add((ts_ref_S, BLDG.hasTimeseriesId, Literal("southZone")))
g.add((BLDG["TS_South"], BLDG.timeseries, ts_ref_S))

# relations for East zone
g.add((BLDG.office, BOT.hasSpace, BLDG.office_E))
g.add((BLDG.ZONE_E, BOT.hasSpace, BLDG.office_E))
g.add((BLDG.ZONE_E, BOT.hasElement, BLDG["TS_East"]))
g.add((BLDG["TS_East"], RDFS.label, Literal("Room temperature measure in East Office")))
g.add((BLDG["TS_East"], UNIT.applicableUnit, UNIT.DEG_C))
ts_ref_E = BNode()
g.add((ts_ref_E, BLDG.hasTimeseriesId, Literal("eastZone")))
g.add((BLDG["TS_East"], BLDG.timeseries, ts_ref_E))

# relations for West zone
g.add((BLDG.office, BOT.hasSpace, BLDG.office_W))
g.add((BLDG.ZONE_W, BOT.hasSpace, BLDG.office_W))
g.add((BLDG.ZONE_W, BOT.hasElement, BLDG["TS_West"]))
g.add((BLDG["TS_West"], RDFS.label, Literal("Room temperature measure in West Office")))
g.add((BLDG["TS_West"], UNIT.applicableUnit, UNIT.DEG_C))
ts_ref_W = BNode()
g.add((ts_ref_W, BLDG.hasTimeseriesId, Literal("westZone")))
g.add((BLDG["TS_West"], BLDG.timeseries, ts_ref_W))

# relations for Core zone
g.add((BLDG.office, BOT.hasSpace, BLDG.office_C))
g.add((BLDG.ZONE_C, BOT.hasSpace, BLDG.office_C))
g.add((BLDG.ZONE_C, BOT.hasElement, BLDG["TS_Core"]))
g.add((BLDG["TS_Core"], RDFS.label, Literal("Room temperature measure in Core Office")))
g.add((BLDG["TS_Core"], UNIT.applicableUnit, UNIT.DEG_C))
ts_ref_C = BNode()
g.add((ts_ref_C, BLDG.hasTimeseriesId, Literal("coreZone")))
g.add((BLDG["TS_Core"], BLDG.timeseries, ts_ref_C))

with open("EP_timeseries.ttl", "wb") as f:
    f.write(g.serialize(format="ttl", encoding='UTF-8'))