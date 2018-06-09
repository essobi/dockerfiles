FROM java:latest  
  
MAINTAINER Camilo Cota <camilocot@gmail.com>  
WORKDIR /opt/titan-1.0.0-hadoop1  
RUN curl -o /opt/titan.zip
http://s3.thinkaurelius.com/downloads/titan/titan-1.0.0-hadoop1.zip  
RUN unzip /opt/titan.zip -d /opt/ && rm /opt/titan.zip  
  
EXPOSE 8182  
EXPOSE 8184  
ADD gremlin-server.yaml /opt/titan-1.0.0-hadoop1/conf/gremlin-server/gremlin-
server.yaml  
ADD cassandra.properties /opt/titan-1.0.0-hadoop1/conf/gremlin-
server/cassandra.properties  
ADD run.sh /opt/titan-1.0.0-hadoop1/bin/run.sh  
  
CMD ["/bin/sh", "/opt/titan-1.0.0-hadoop1/bin/run.sh"]  

