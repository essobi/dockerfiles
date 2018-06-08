FROM ubuntu:16.04  
MAINTAINER Flywheel <support@flywheel.io>  
  
RUN apt-get update && apt-get install -y dcmtk jq unzip  
  
# Make directory for flywheel spec (v0)  
ENV FLYWHEEL /flywheel/v0  
RUN mkdir -p ${FLYWHEEL}  
COPY run ${FLYWHEEL}/run  
COPY manifest.json ${FLYWHEEL}/manifest.json  
  
RUN chmod +x ${FLYWHEEL}/run  

