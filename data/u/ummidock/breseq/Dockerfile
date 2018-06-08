FROM ubuntu:16.04  
MAINTAINER Miguel Machado <mpmachado@medicina.ulisboa.pt>  
LABEL version="0.32.1"  
  
WORKDIR /NGStools/  
  
# General dependencies  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y wget unzip gzip libunwind-dev  
  
# Dependencies  
# Bowtie2  
RUN wget https://downloads.sourceforge.net/project/bowtie-
bio/bowtie2/2.3.4.1/bowtie2-2.3.4.1-linux-x86_64.zip && \  
unzip bowtie2-2.3.4.1-linux-x86_64.zip && \  
rm bowtie2-2.3.4.1-linux-x86_64.zip  
# R  
RUN apt-get install -y r-base  
  
# breseq  
RUN wget
https://github.com/barricklab/breseq/releases/download/v0.32.1/breseq-0.32.1-Linux-x86_64.tar.gz
&& \  
tar xf breseq-0.32.1-Linux-x86_64.tar.gz && \  
rm breseq-0.32.1-Linux-x86_64.tar.gz  
  
ENV
PATH="/NGStools/breseq-0.32.1-Linux-x86_64/bin:/NGStools/bowtie2-2.3.4.1-linux-x86_64:${PATH}"  
# Clean  
RUN apt-get remove -y wget && \  
apt-get autoclean -y  
  
WORKDIR /data/  

