  
FROM sscheffler/jdk  
  
MAINTAINER Stefan Scheffler (stefan-scheffler@web.de)  
  
# Update the default application repository sources list  
RUN apt-get update  
  
RUN apt-get -y install git ant maven  
  
ENV ORIENTDB_VERSION 2.0.1  
ENV JAVA_HOME /opt/jdk8  
  
# Build OrientDB cleaning up afterwards  
RUN git clone https://github.com/orientechnologies/orientdb.git --single-
branch --depth 1 --branch $ORIENTDB_VERSION  
RUN cd orientdb && \  
ant clean installg  
RUN mv /releases/orientdb-community-* /opt/orientdb && \  
rm -rf /opt/orientdb/databases/* ~/orientdb  
  
EXPOSE 2424  
EXPOSE 2480  
# Set the user to run OrientDB daemon  
USER root  
  
CMD ["/opt/orientdb/bin/server.sh"]  

