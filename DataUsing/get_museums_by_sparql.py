from SPARQLWrapper import SPARQLWrapper

sparql = SPARQLWrapper('http://ko.dbpedia.org/sparql')

sparql.setQuery('''
SELECT * WHERE {
    ?s rdf:type dbpedia-owl:Museum .
    ?s prop-ko:소재지 ?address .
    OPTIONAL { ?s rdfs:label ?label . }
} ORDER BY ?s
''')

sparql.setReturnFormat('json')

response = sparql.query().convert()
for result in response['results']['bindings']:
    print(result['s']['value'], result['address']['value'])