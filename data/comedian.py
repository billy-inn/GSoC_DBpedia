from SPARQLWrapper import SPARQLWrapper, JSON

endpoint = SPARQLWrapper("http://dbpedia.org/sparql")
endpoint.setReturnFormat(JSON)

infile = open("comedian.txt")
outfile1 = open("comedianClass.txt", "w")
outfile2 = open("comedianFeature.txt", "w")
dbo = "http://dbpedia.org/ontology/"
yago = "http://dbpedia.org/class/yago/"
count = 0
for line in infile.readlines():
	if count % 10 == 0:
		print count
	entity = line.strip()
	endpoint.setQuery('''
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?attr
WHERE
{
	<%s> rdf:type ?attr .
}
''' % entity)
	results = endpoint.query().convert()
	outfile1.write("%s" % entity)
	outfile2.write("%s" % entity)
	for res in results["results"]["bindings"]:
		attr = res["attr"]["value"]
		if dbo in attr:
			outfile1.write("\t%s" % attr)
		elif yago in attr:
			outfile2.write("\t%s" % attr)
	outfile1.write("\n")
	outfile2.write("\n")
	count += 1
		

