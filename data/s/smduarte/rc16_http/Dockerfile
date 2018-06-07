FROM openjdk  
  
MAINTAINER smd@fct.unl.pt  
  
  
COPY pygmy-httpd.jar /jar/  
COPY file1M /data/file1M  
COPY earth.jpg /data/  
COPY huge.jpg /data/  
  
WORKDIR /data  
  
CMD ["java", "-jar", "/jar/pygmy-httpd.jar"]  

