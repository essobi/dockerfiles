#################################################################  
# Dockerfile  
# Software: Samtools, BFCTools  
# Software Version: 1.3.1  
# Description: Processing sequence alignments in SAM and BAM formats.  
# Website: https://snakemake.readthedocs.io/en/stable/  
# Tags: Sequence|Genomics|General  
# Provides: Samtools V1.3.1  
# Date : 08/2017  
#################################################################  
  
# Base docker image  
FROM ubuntu:17.04  
MAINTAINER test@armadillo.uqam  
  
# Install Samtools and dependencies  
RUN apt-get clean  
  
RUN apt-get --quiet update \  
&& apt-get -qqy install \  
samtools \  
bcftools \  
&& apt-get clean \  
&& apt-get purge \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /data/inputs \  
/data/outputs  
  
WORKDIR /data  

