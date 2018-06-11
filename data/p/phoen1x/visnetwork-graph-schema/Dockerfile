FROM neo4j:3.1.3  
  
# add R programming language  
RUN apk add --no-cache R R-dev R-doc curl libressl-dev curl-dev libxml2-dev
gcc g++ git coreutils bash ncurses  
  
# R package visNetwork  
RUN Rscript -e 'install.packages("visNetwork",repos =
"http://cran.r-project.org")'  
  
# R package RNeo4j  
RUN Rscript -e 'install.packages("RNeo4j",repos =
"http://cran.r-project.org")'  
  
# import Neo4j demo data  
COPY ./initial-database.cql /initial-database.cql  
RUN cat /initial-database.cql \  
| /var/lib/neo4j/bin/neo4j-shell -path /data_demo/databases/graph.db  
  
# set path to graph databse  
RUN cat /var/lib/neo4j/conf/neo4j.conf > /var/lib/neo4j/conf/neo4j.conf.org \  
&& echo "dbms.directories.data=/data_demo" >> /var/lib/neo4j/conf/neo4j.conf \  
&& echo "dbms.directories.import=/import" >> /var/lib/neo4j/conf/neo4j.conf \  
&& echo "dbms.security.allow_csv_import_from_file_urls=true" >>
/var/lib/neo4j/conf/neo4j.conf \  
&& echo "dbms.shell.enabled=true" >> /var/lib/neo4j/conf/neo4j.conf  
  
# set import directory  
RUN mkdir /import \  
&& rm -rf /var/lib/neo4j/import \  
&& ln -s /import /var/lib/neo4j/import  
  
VOLUME /import  

