FROM maven:3.3.9-jdk-8-alpine  
MAINTAINER Marcus Slavenas <slavenas@illinois.edu>  
  
# Copy built JAR(s) into image  
COPY . /workspace/  
  
# Set container workdir  
WORKDIR /workspace  
  
# Install ffmpeg  
RUN apk add --update ffmpeg  
  
# Build speech2text with Maven  
RUN mvn package  
  
# Command to run when starting docker  
CMD [ "java", "-jar", "target/speech2text-1.0-SNAPSHOT-jar-with-
dependencies.jar" ]  
  
# Setup environment variables. These are passed into the container. You can
change  
# these to your setup. If RABBITMQ_URI is not set, it will try and use the
rabbitmq  
# server that is linked into the container.  
ENV RABBITMQ_URI="" \  
RABBITMQ_EXCHANGE="clowder" \  
RABBITMQ_VHOST="%2F" \  
RABBITMQ_QUEUE="speech2text"  

