##########################################################  
# Dockerfile which builds a base image with oracle-java8.  
##########################################################  
FROM dockerfile/java:oracle-java8  
  
ADD . /home  
  
RUN apt-get update && apt-get install -y maven  
  
WORKDIR /home/  
  
RUN mvn clean install  

