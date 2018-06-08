# MEGAHIT on ubuntu 16.04  
#  
# VERSION 1.0  
# Use ubuntu as a parent image  
FROM ubuntu:16.04  
MAINTAINER Hiroko Tanaka <hiroko@hgc.jp>  
  
LABEL Description="MEGAHIT v1.1.2" \  
Project="Genomon-Project Dockerization" \  
Version="1.0"  
  
# Install required libraries in order to create MEGAHIT  
# build-essential package : the set of developement tools (gcc,g++ e.t.c)  
RUN apt-get update && apt-get install -y \  
build-essential \  
git \  
python \  
wget \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /tools  
RUN git clone https://github.com/voutcn/megahit.git \  
&& cd /tools/megahit && make  
ENV PATH /tools/megahit:$PATH  
  
WORKDIR /work  

