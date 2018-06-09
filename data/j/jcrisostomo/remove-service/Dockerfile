FROM java:8-jre-alpine  
MAINTAINER Interware  
COPY . /opt/services  
RUN cd /opt/services  
WORKDIR /opt/services  
CMD ["java", "-jar", "bin/removeservice-jar-with-dependencies.jar"]  

