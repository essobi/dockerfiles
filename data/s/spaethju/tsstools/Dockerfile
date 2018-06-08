# Set the base image to CentOS 7  
FROM centos:7  
# Set author/maintainer  
MAINTAINER Team Green <green@qbic.de>  
  
# Set environment variable to data folder  
ENV DATA_DIR=/data  
  
# Update OS and install wget and java  
RUN yum -y update  
RUN yum -y upgrade  
RUN yum -y install wget  
RUN yum -y install java  
  
# Download tsstools  
RUN wget https://lambda.informatik.uni-
tuebingen.de/nexus/content/repositories/releases/org/unituebingen/it/tsstools/1.0beta/tsstools-1.0beta-
dependencies.jar -O tsstools.jar  
  
# Run tsstools with mapper result (normal and enriched)  
ENTRYPOINT java -jar tsstools.jar -i ${DATA_DIR}/${BAM_FILE} -o ${DATA_DIR} -w  

