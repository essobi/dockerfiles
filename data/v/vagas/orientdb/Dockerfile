############################################################  
# Dockerfile to run an OrientDB (Graph) Container  
# http://crosbymichael.com/dockerfile-best-practices.html  
# http://crosbymichael.com/dockerfile-best-practices-take-2.html  
############################################################  
  
FROM vagas/orientdb-base:2.0.9  
  
MAINTAINER Ronie Uliana (ronie.uliana@vagas.com.br)  
  
# Update the default application repository sources list  
RUN apt-get update  
  
# Install supervisord  
RUN apt-get -y install supervisor  
RUN mkdir -p /var/log/supervisor  
  
# use supervisord to start orientdb  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD orientdb-server-config.xml /opt/orientdb/config/orientdb-server-config.xml  
ADD https://github.com/orientechnologies/orientdb-
lucene/releases/download/2.0-SNAPHOST/orientdb-lucene-2.0-SNAPSHOT-dist.jar
/opt/orientdb/plugins/  
  
EXPOSE 2424  
EXPOSE 2480  
  
# Set the user to run OrientDB daemon  
USER root  
  
# Default command when starting the container  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  

