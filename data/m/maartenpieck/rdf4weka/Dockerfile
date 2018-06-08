FROM ubuntu:16.04  
  
MAINTAINER Maarten Pieck <maarten.pieck1@gmail.com>  
  
#install weka  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu vivid main universe" >>
/etc/apt/sources.list  
RUN apt-get update && apt-get install -y openjdk-8-jdk weka maven  
  
ADD . /app  
RUN mkdir config && mv /app/weka-service.ini /config/  
  
  
VOLUME /data  
WORKDIR /data  
  
EXPOSE 80  
  
RUN bash /app/firstTime.sh  
  
ENV SPARQL_ENDPOINT="http://localhost:8890/sparql" \  
GRAPH="http://localhost:8890/DAV" \  
CLASSIFIER_DATA_QUERY="prefix test: <http://test/test> \  
select ?feature1 ?feature2 ?class where { \  
graph <http://localhost:8890/DAV> { \  
?o test:type test:test . \  
?o test:class ?class . \  
?o test:feature1 ?feature1 . \  
?o test:feature2 ?feature2 } \  
} \  
group by ?o " \  
ASSOCIATOR_DATA_QUERY="prefix skosxl: <http://www.w3.org/2008/05/skos-xl#> \  
prefix esco: <http://data.europa.eu/esco/model#> \  
prefix mu: <http://mu.semte.ch/vocabularies/core/> \  
select group_concat(distinct ?skillUuid; separator=\",\") as ?skillUuid where
{ \  
graph <http://localhost:8890/DAV> { \  
?s a esco:Occupation. \  
?relation esco:isRelationshipFor ?s. \  
?relation esco:refersConcept ?skill. \  
?s mu:uuid ?uuid. \  
?s skosxl:prefLabel / skosxl:literalForm ?label. \  
?skill skosxl:prefLabel / skosxl:literalForm ?skilllabel. \  
?skill mu:uuid ?skillUuid. \  
FILTER ( lang(?label) = \"en\" ) \  
FILTER ( lang(?skilllabel) = \"en\" ) \  
} \  
} \  
group by ?uuid " \  
ATTRIBUTES_QUERY="prefix skosxl: <http://www.w3.org/2008/05/skos-xl#> \  
prefix esco: <http://data.europa.eu/esco/model#> \  
prefix mu: <http://mu.semte.ch/vocabularies/core/> \  
select DISTINCT ?skillUuid where { \  
graph <http://localhost:8890/DAV> { \  
?s a esco:Occupation. \  
?relation esco:isRelationshipFor ?s. \  
?relation esco:refersConcept ?skill. \  
?skill skosxl:prefLabel / skosxl:literalForm ?skilllabel. \  
?skill mu:uuid ?skillUuid. \  
FILTER ( lang(?skilllabel) = \"en\" ) \  
} \  
}"  
  
  
CMD ["/bin/bash", "/app/startup.sh"]  

