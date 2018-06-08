FROM java:openjdk-8-alpine  
MAINTAINER Rahul Somasunderam <rahul.som@gmail.com>  
  
WORKDIR /opt  
RUN wget http://www-eu.apache.org/dist/tika/tika-app-1.17.jar  
  
WORKDIR /local  
ENTRYPOINT ["java", "-jar", "/opt/tika-app-1.17.jar"]  

