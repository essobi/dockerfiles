#######################################  
# Dockerfile for Lookup Service #  
# BigDataEurope #  
# #  
# based on bde2020/sc7pilotbase:1.0.0 #  
# java 1.8.0_151 #  
# maven 3.0.5 #  
# git 1.9.1 #  
# tomcat 8.0.23 #  
#######################################  
  
FROM bde2020/sc7pilotbase:1.0.0  
  
MAINTAINER Giorgos Argyriou <gioargyr@gmail.com>  
  
RUN git clone https://github.com/big-data-europe/pilot-sc7-lookup-service.git
\  
&& cd pilot-sc7-lookup-service \  
&& mvn clean package  
  
RUN cp /pilot-sc7-lookup-service/target/*.war /tomcat/webapps  
  
ADD gadm28.zip /gadm28.zip  
RUN unzip gadm28.zip  
  
CMD ["/bin/bash", "/runtomcat.sh"]  

