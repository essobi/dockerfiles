FROM jongoks/docker-zookeeper  
  
MAINTAINER Jongoks <jongoks@gmail.com  
  
# Druid  
RUN wget -q http://static.druid.io/artifacts/releases/druid-0.10.1-bin.tar.gz  
RUN tar -xzf druid-0.10.1-bin.tar.gz -C /opt  
RUN mv /opt/druid-0.10.1 /opt/druid  
  
# Tranquility  
RUN curl -O http://static.druid.io/tranquility/releases/tranquility-
distribution-0.8.0.tgz  
RUN tar -xzf tranquility-distribution-0.8.0.tgz -C /opt  
  
WORKDIR /opt/druid  
  
# Entrypoint  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
EXPOSE 8081 8082 8083 8090 8091 8200  
ENTRYPOINT ["/entrypoint.sh"]  

