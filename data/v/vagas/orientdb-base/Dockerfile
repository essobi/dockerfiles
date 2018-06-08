############################################################  
# Dockerfile with OrientDB installed (but not configured)  
#  
# Base image to other OrientDB installations.  
#  
# http://crosbymichael.com/dockerfile-best-practices.html  
# http://crosbymichael.com/dockerfile-best-practices-take-2.html  
############################################################  
  
FROM java:7  
  
MAINTAINER Ronie Uliana (ronie.uliana@gmail.com)  
  
# Update the default application repository sources list  
RUN apt-get update  
  
# OrientDB dependencies  
# https://www.digitalocean.com/community/tutorials/how-to-install-and-use-
orientdb-on-an-ubuntu-12-04-vps  
RUN apt-get -y install git ant  
  
ENV ORIENTDB_VERSION 2.0.9  
  
# Build OrientDB cleaning up afterwards  
RUN cd && \  
git clone https://github.com/orientechnologies/orientdb.git --single-branch
--depth 1 --branch $ORIENTDB_VERSION && \  
cd orientdb && \  
ant clean installg && \  
mv /root/releases/orientdb-community-* /opt/orientdb && \  
rm -rf /opt/orientdb/databases/* ~/orientdb  
  
# Add support to Full Text Search indexes using Lucene  
ADD https://github.com/orientechnologies/orientdb-
lucene/releases/download/2.0-SNAPHOST/orientdb-lucene-2.0-SNAPSHOT-dist.jar
/opt/orientdb/plugins/  

