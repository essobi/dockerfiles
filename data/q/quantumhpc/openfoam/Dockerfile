FROM ubuntu:trusty  
MAINTAINER quantumhpc  
  
RUN echo deb http://www.openfoam.com/download/ubuntu trusty main >>
/etc/apt/sources.list.d/openfoam.list  
  
RUN apt-get update && apt-get install -y --force-yes \  
openfoam30 \  
paraviewopenfoam44  

