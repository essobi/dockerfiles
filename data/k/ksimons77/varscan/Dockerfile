#http://varscan.sourceforge.net/  
FROM java:8u111-jre  
  
# Install VarScan  
ENV VARSCAN_VERSION v2.3.9  
RUN curl -SL
https://sourceforge.net/projects/varscan/files/VarScan.$VARSCAN_VERSION.jar/download
--output varscan.jar  
  
ENTRYPOINT ["java", "-jar", "varscan.jar"]  

