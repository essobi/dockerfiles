FROM java:8-jre-alpine  
MAINTAINER VL  
COPY . /opt/services  
RUN cd /opt/services  
WORKDIR /opt/services  
CMD ["java", "-jar", "bin/loginservice-jar-with-dependencies.jar"]  
##CMD ["bash", "start.sh", "bin/loginservice-jar-with-dependencies.jar"]  

