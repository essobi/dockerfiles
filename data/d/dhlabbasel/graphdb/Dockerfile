FROM dhlabbasel/webapi-base:latest  
  
MAINTAINER Ivan Subotic "ivan.subotic@unibas.ch"  
# Add GraphDB distribution from the Knora repository  
RUN \  
git clone -b develop --single-branch --depth=1 https://github.com/dhlab-
basel/Knora.git /knora && \  
unzip /knora/triplestores/graphdb-se/graphdb-se-8.0.3-dist.zip && \  
mv /graphdb-se-8.0.3 /graphdb && \  
cp /knora/webapi/scripts/KnoraRules.pie /graphdb && \  
rm -rf /graphdb-se-8.0.3-dist.zip && \  
rm -rf /knora  
  
WORKDIR /graphdb  
  
EXPOSE 7200  
# Set GraphDB Max and Min Heap size  
ENV GDB_HEAP_SIZE="2g"  
CMD ["./bin/graphdb", "-Dgraphdb.license.file=/external/GRAPHDB_SE.license"]

