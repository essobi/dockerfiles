############################################################  
# Dockerfile to run a Rexster server linked to OrientDB database  
# http://crosbymichael.com/dockerfile-best-practices.html  
# http://crosbymichael.com/dockerfile-best-practices-take-2.html  
############################################################  
  
FROM debian:jessie  
  
MAINTAINER Ronie Uliana (ronie.uliana@gmail.com)  
  
# Install Rexster dependencies  
RUN apt-get update && apt-get -y install openjdk-7-jdk git maven  
  
# Rexster versior  
ENV VERSION 2.6.0  
  
# Build Rexster and cleaning up afterwards  
RUN cd && \  
git clone https://github.com/tinkerpop/rexster --single-branch --depth 1
--branch $VERSION && \  
cd rexster && \  
mvn clean install && \  
mv rexster-server/target/rexster-server-*.zip .. && \  
cd .. && \  
unzip rexster-server-*.zip && \  
rm rexster-server-*.zip && \  
mv rexster-server-* /opt/rexster && \  
find /opt/rexster -type d -exec chmod 755 {} \; && \  
rm -rf rexster && \  
rm /opt/rexster/config/rexster.xml  
  
# Config for Rexster linked to OrientDB container  
ADD rexster.xml /opt/rexster/config/  
  
# Start script (replace variables in linked container)  
ADD run.sh /opt/rexster/bin/  
  
ADD orientdb-client-2.0.3.jar /opt/rexster/ext/  
ADD orientdb-core-2.0.3.jar /opt/rexster/ext/  
ADD orientdb-enterprise-2.0.3.jar /opt/rexster/ext/  
ADD orientdb-graphdb-2.0.3.jar /opt/rexster/ext/  
  
# HTTP (REST and Web console)  
EXPOSE 8182  
# Shutdown port (from localhost only)  
EXPOSE 8183  
# Rexpro (binary)  
EXPOSE 8184  
  
# Set the user to run Rexster  
USER root  
  
# Default command when starting the container  
WORKDIR /opt/rexster  
CMD ["/bin/sh", "-e", "./bin/run.sh"]  

