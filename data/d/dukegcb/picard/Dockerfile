FROM ubuntu:16.04  
LABEL maintainer="john.bradley@duke.edu"  
  
# picard requires java  
RUN apt-get update && apt-get install -y \  
wget \  
openjdk-8-jre-headless  
  
# Installs fastqc from compiled java distribution into /opt/FastQC  
ENV PICARD_VERSION="2.10.7"  
ENV PICARD_URL
https://github.com/broadinstitute/picard/releases/download/${PICARD_VERSION}/picard.jar  
  
WORKDIR /opt/picard  
RUN wget $PICARD_URL  
  
CMD ["java", "-jar", "picard.jar"]  

