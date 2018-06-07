############################################################  
# Dockerfile - Spring Boot Runner  
############################################################  
  
# Set the base image to java8  
FROM openjdk:8  
  
# File Author / Maintainer  
MAINTAINER Jorge Acetozi  
  
# Define default environment variables  
ENV ARTIFACT_HOME=/opt/spring-boot-app  
ENV ARTIFACT_BINARIES=$ARTIFACT_HOME/bin  
ENV ARTIFACT_LOGS=/var/log/spring-boot-app  
  
# Create directories  
RUN mkdir -p $ARTIFACT_BINARIES && \  
mkdir -p $ARTIFACT_LOGS  
  
# Set default directory  
WORKDIR $ARTIFACT_HOME  
  
# Volume for artifact logs  
VOLUME $ARTIFACT_LOGS  
  
# Expose default servlet container port  
EXPOSE 8080  
  
# Add artifact initialization script  
ADD start.sh $ARTIFACT_BINARIES/start.sh  
  
# Give permissions  
RUN chmod 755 $ARTIFACT_BINARIES/start.sh  
  
# Main command  
ENTRYPOINT $ARTIFACT_BINARIES/start.sh  

