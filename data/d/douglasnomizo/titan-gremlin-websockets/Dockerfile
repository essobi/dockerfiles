FROM java:latest  
  
MAINTAINER Douglas Nomizo <douglasnomizo@outlook.com>  
  
LABEL Description="Fork of @davebshow's repo that uses sockets" Version="1.0"
Tags="cassandra,elasticsearch,graph,gremlin,websockets,titan"  
  
WORKDIR /opt/titan-1.0.0-hadoop1  
  
RUN curl -o /opt/titan.zip
http://s3.thinkaurelius.com/downloads/titan/titan-1.0.0-hadoop1.zip  
  
RUN unzip /opt/titan.zip -d /opt/ && \  
rm /opt/titan.zip  
  
ADD run.sh /opt/titan-1.0.0-hadoop1/  
  
EXPOSE 8182  
EXPOSE 8184  
CMD ["/bin/sh", "-e", "/opt/titan-1.0.0-hadoop1/run.sh"]  

