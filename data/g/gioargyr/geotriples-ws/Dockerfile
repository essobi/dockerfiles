#######################################  
# Dockerfile for Geotriples WS #  
# BigDataEurope #  
# #  
# based on bde2020/sc7pilotbase:1.0.0 # #  
# java 1.8.0_151 #  
# maven 3.0.5 #  
# git 1.9.1 #  
# tomcat 8.0.23 #  
#######################################  
  
FROM bde2020/sc7pilotbase:1.0.0  
  
MAINTAINER Giorgos Argyriou <gioargyr@gmail.com>  
  
# DOWNLOAD AND BUILD  
RUN git clone -b testing-images https://github.com/big-data-europe/pilot-
sc7-geotriples.git \  
&& cd pilot-sc7-geotriples \  
&& mvn clean package  
  
RUN mkdir /resources \  
&& cp /pilot-sc7-geotriples/target/*.war /tomcat/webapps \  
&& cp /pilot-sc7-geotriples/change-mapping.ttl /resources \  
&& cp /pilot-sc7-geotriples/event-mapping.ttl /resources \  
&& cp /pilot-sc7-geotriples/id.txt /resources  
  
CMD ["/bin/bash", "/runtomcat.sh"]

