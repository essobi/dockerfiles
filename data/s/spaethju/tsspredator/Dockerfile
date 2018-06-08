# Set the base image to centos  
FROM centos:7  
# Set author/maintainer  
MAINTAINER Team Green <green@qbic.de>  
  
# Upgrading system  
RUN yum -y update  
RUN yum -y upgrade  
  
RUN yum -y install wget  
  
# Downloading amd installing Java  
RUN yum -y install java  
  
# Downloading and installing TSSPredator  
RUN wget https://lambda.informatik.uni-
tuebingen.de/nexus/content/repositories/releases/org/uni-
tuebingen/it/TSSpredator/1.06/TSSpredator-1.06.jar -O TSSpredator-1.06.jar  
  
ENTRYPOINT java -Xmx${SPACE} -jar TSSpredator-1.06.jar /data/${CONFIG}  

