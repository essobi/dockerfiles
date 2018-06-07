# osul/solr:latest  
FROM solr:6.2  
MAINTAINER Corey Hinshaw <hinshaw.25@osu.edu>  
  
USER root  
  
RUN apt-get update && \  
apt-get -y install git && \  
rm -rf /var/lib/apt/lists/*  
  
USER $SOLR_USER  
  
COPY scripts/create_ci_core.sh /docker-entrypoint-initdb.d/  

