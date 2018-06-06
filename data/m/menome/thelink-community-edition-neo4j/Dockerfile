  
FROM neo4j:3.1.1  
COPY neo4j.conf /var/lib/neo4j/conf/neo4j.conf  
  
# copy demo files into the link import dir  
COPY movieSample/* import/movieSample/  
COPY theLinkBase/* import/theLinkBase/  
COPY wellLocationsExample/* import/wellLocationsExample/  
  
# Note that this shellscript must be run from the host machine to work.  
COPY backupNeo4j.sh import/backupNeo4j.sh  
  
# copy plugins into the neo4j plugins folder  
COPY plugins/* plugins/  
  

