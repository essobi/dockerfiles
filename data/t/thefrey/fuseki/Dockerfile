FROM ubuntu:14.04  
MAINTAINER Alex Lynham "alex@swirrl.com"  
RUN apt-get update  
  
RUN apt-get -y install tar wget curl openjdk-7-jre-headless  
  
RUN mkdir -p /opt/fuseki  
RUN mkdir /opt/fuseki/config  
  
ADD http://apache.mirror.anlx.net/jena/binaries/jena-
fuseki1-1.1.2-distribution.tar.gz /opt/fuseki/jena-fuseki-1.1.2.tar.gz  
  
RUN tar -xvzf /opt/fuseki/jena-fuseki-1.1.2.tar.gz -C /opt/fuseki  
  
ADD config.ttl /opt/fuseki/config/config.ttl  
  
ADD run-fuseki /opt/fuseki/run-fuseki  
  
RUN chmod +x /opt/fuseki/run-fuseki  
  
RUN mkdir /data  
  
VOLUME ["/data", "/opt/fuseki/config"]  
  
EXPOSE 3030  
CMD ["/opt/fuseki/run-fuseki"]

