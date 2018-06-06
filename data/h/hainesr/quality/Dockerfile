#------------------------------------------------------------------------------  
# Copyright (c) 2016, The University of Manchester, UK.  
#  
# BSD licenced. See LICENCE for details.  
#  
# Author: Robert Haines  
#------------------------------------------------------------------------------  
FROM continuumio/anaconda:latest  
MAINTAINER Robert Haines <robert.haines@manchester.ac.uk>  
  
RUN apt-get update -q && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -qy \  
fontconfig \  
\--no-install-recommends && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY ["data/project data", "/opt/analysis/data/"]  
COPY ["scripts", "/opt/analysis/scripts/"]  
  
WORKDIR /opt/analysis  
  
ENTRYPOINT /bin/bash  

