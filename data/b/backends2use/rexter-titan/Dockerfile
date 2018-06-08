# Tinkerpop Rexster Server  
#  
FROM centos  
  
# Install unzip so we later can unpack  
RUN yum install -y java unzip  
  
ADD http://s3.thinkaurelius.com/downloads/titan/titan-0.5.3-hadoop2.zip /  
RUN unzip titan-0.5.3-hadoop2.zip  
RUN rm titan-0.5.3-hadoop2.zip  
RUN mv titan-0.5.3-hadoop2 /opt/  
RUN ln -s /opt/titan-0.5.3-hadoop2 /opt/titan  
  
ADD titan-cassandra.properties /opt/titan/conf/titan-cassandra.properties  
ADD rexster-cassandra.xml /opt/titan/rexhome/config/rexster-cassandra.xml  
  
# Server listening port  
EXPOSE 80:8182  
# RexPro port  
EXPOSE 8184  
# Shutdown listener port  
EXPOSE 8183  
WORKDIR /opt/titan  
  
## Entrypoint  
ENTRYPOINT ["bin/rexster.sh", "--start", "-c",
"/opt/titan/rexhome/config/rexster-cassandra.xml"]  

