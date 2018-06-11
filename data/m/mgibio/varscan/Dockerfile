FROM ubuntu:xenial  
MAINTAINER Thomas B. Mooney <tmooney@genome.wustl.edu>  
  
LABEL \  
version="v2.4.2" \  
description="Varscan image for use in Workflows"  
  
RUN apt-get update && apt-get install -y \  
default-jre \  
wget  
  
ENV VARSCAN_INSTALL_DIR=/opt/varscan  
  
WORKDIR $VARSCAN_INSTALL_DIR  
RUN wget
https://github.com/dkoboldt/varscan/releases/download/2.4.2/VarScan.v2.4.2.jar
&& \  
ln -s VarScan.v2.4.2.jar VarScan.jar  
  
WORKDIR /  
ENTRYPOINT ["java", "-jar", "/opt/varscan/VarScan.jar"]  

