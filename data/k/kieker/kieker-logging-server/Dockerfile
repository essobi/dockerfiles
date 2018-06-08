FROM anapsix/alpine-java  
  
WORKDIR /opt  
  
EXPOSE 8080  
ADD https://github.com/kieker-monitoring-docker/kieker-logging-
server/releases/download/0.1.1/kieker-logging-server-0.1.1.jar /opt/kls.jar  
ADD ziptool.sh /opt/ziptool.sh  
  
CMD java -Dorg.apache.activemq.SERIALIZABLE_PACKAGES=* -jar kls.jar  

