##########################################################  
# Dockerfile which builds a base image with oracle-java8.  
##########################################################  
FROM dockerfile/java:oracle-java8  
  
ADD . /home  
  
WORKDIR /home/src/main/java  
  
RUN javac HelloWorld.java  

