#################################################################  
# Dockerfile  
# Software: Vienna  
# Software Version: 2.2.0a-1  
# Description: The prediction and comparison of RNA secondary structures.  
# Website: http://www.tbi.univie.ac.at/RNA/  
# Tags: Proteomics|Genomics|General  
# Provides: Vienna V2.2.0a-1  
# Date : 02/2016  
#################################################################  
  
# Base docker image  
FROM ubuntu:14.04  
MAINTAINER test@armadillo.uqam  
  
# Install miRdup and dependencies  
RUN apt-get clean  
  
# Prepare installation  
RUN apt-get --quiet update \  
&& apt-get -qqy install \  
\--no-install-recommends \  
software-properties-common \  
&& apt-get clean \  
&& apt-get purge \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Create rep  
RUN mkdir /data  
  
RUN apt-add-repository -y ppa:j-4/vienna-rna \  
&& apt-get --quiet update \  
&& apt-get -qqy install \  
vienna-rna \  
&& apt-get clean \  
&& apt-get purge \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /data/inputs \  
/data/outputs  
  
WORKDIR /data  

