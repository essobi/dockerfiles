FROM kubekit/cassandra:v0.3  
MAINTAINER Dana NicCaluim <dniccaluim@airware.com>  
  
USER root  
RUN apt-get update  
RUN apt-get install -y procps psmisc  
  
ADD https://raw.githubusercontent.com/openzipkin/zipkin/1.5.1/zipkin-
cassandra-core/src/main/resources/cassandra-schema-cql3.txt /schema.txt  
ADD boot.sh /boot.sh  
RUN chmod +x /boot.sh  
ENTRYPOINT ["/boot.sh"]  
  
EXPOSE 9160 7000 7001 9042 7199  

