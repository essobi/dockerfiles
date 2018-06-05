#################################################################  
# Dockerfile  
# Software: BWA  
# Software Version: 0.7.12  
# Description: Burrows-Wheeler Aligner  
# Website: http://bio-bwa.sourceforge.net/  
# Tags: Sequence|Genomics|General  
# Provides: BWA V0.7.12  
# Date : 08/2017  
#################################################################  
  
# Base docker image  
FROM ubuntu:16.04  
MAINTAINER test@armadillo.uqam  
  
# Install Samtools and dependencies  
RUN apt-get clean  
  
RUN apt-get --quiet update \  
&& apt-get -qqy install \  
samtools \  
bwa \  
&& apt-get clean \  
&& apt-get purge \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /data/inputs \  
/data/outputs  
  
WORKDIR /data  

