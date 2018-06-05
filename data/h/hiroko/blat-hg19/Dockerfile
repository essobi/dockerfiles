# blat  
#  
# VERSION 0.0.1  
# Use ubuntu as a parent image  
FROM ubuntu:16.04  
MAINTAINER Hiroko Tanaka <hiroko@hgc.jp>  
  
LABEL Description="blat with the hg19 2bit-file" \  
Project="Genomon-Project Dockerization" \  
Version="1.0"  
  
# Install required libraries in order to create blat  
RUN apt-get update && apt-get install -y \  
libkrb5-3 \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
# create directories for tools  
RUN mkdir -p tools/src db/hg19  
  
# Install hg19 Human DB for blat  
RUN wget ftp://hgdownload.cse.ucsc.edu/goldenPath/hg19/bigZips/hg19.2bit -P
db/hg19  
  
# Install blat binary  
RUN wget http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/blat/blat -P
tools \  
&& chmod a+x tools/blat  
ENV PATH /tools:$PATH  

