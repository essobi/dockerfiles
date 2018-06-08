#################################################################  
# Dockerfile to build TopHat 2.1.0 with Bowtie 2.2.6 container  
# images  
# Based on Ubuntu  
##################################################################  
# Set the base image to Ubuntu  
FROM ubuntu:14.04  
# File/Author / Maintainer  
MAINTAINER Hartmut Schultze  
# Update the repository sources list, install wget, unzip, python  
RUN apt-get update && apt-get install --yes wget unzip \  
build-essential \  
curl \  
python \  
python2.7-dev \  
python-pip \  
python-numpy \  
python-matplotlib  
# Working directory in /bin  
WORKDIR /bin  
# Download TopHat2  
RUN wget
http://ccb.jhu.edu/software/tophat/downloads/tophat-2.1.0.Linux_x86_64.tar.gz  
# Download Bowtie2  
RUN wget --default-page=bowtie2-2.2.6-linux-x86_64.zip
http://sourceforge.net/projects/bowtie-
bio/files/bowtie2/2.2.6/bowtie2-2.2.6-linux-x86_64.zip/  
# Unzip the archive  
RUN tar zxvf tophat-2.1.0.Linux_x86_64.tar.gz  
# Remove the archive  
RUN rm tophat-2.1.0.Linux_x86_64.tar.gz  
# Unzip the archive  
RUN unzip bowtie2-2.2.6-linux-x86_64.zip  
# Remove the archive  
RUN rm bowtie2-2.2.6-linux-x86_64.zip  
# Working directory in Bowtie2  
WORKDIR /bin/bowtie2-2.2.6  
# Symbolic link from "bowtie" to "bowtie2"  
RUN ln -s bowtie2 bowtie  
# Change in PATH  
ENV PATH $PATH:/bin/tophat-2.1.0.Linux_x86_64  
ENV PATH $PATH:/bin/bowtie2-2.2.6  
  
WORKDIR /tmp  
#Install HtSeq  
RUN curl
https://pypi.python.org/packages/source/H/HTSeq/HTSeq-0.6.1.tar.gz#md5=b7f4f38a9f4278b9b7f948d1efbc1f05
> HTSeq-0.6.1.tar.gz && \  
tar -xzf HTSeq-0.6.1.tar.gz && \  
rm HTSeq-0.6.1.tar.gz && \  
cd HTSeq-0.6.1 && \  
ls && \  
python setup.py install --user  
  
# Remove wget and unzip  
RUN apt-get purge --yes wget unzip  
# Working directory  
WORKDIR /  

