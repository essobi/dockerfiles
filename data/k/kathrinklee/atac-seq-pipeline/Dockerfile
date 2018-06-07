############################################################  
# Dockerfile to build container images for ATAC-seq pipeline  
# including Bowtie1, samtools and Picard  
# Based on Ubuntu  
############################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu:14.04  
  
# File Author / Maintainer  
MAINTAINER Kathrin Klee <klee@uni-bonn.de>  
  
# Update the repository sources list and install samtools  
RUN apt-get update && apt-get -y install samtools=0.1.19-1  
  
# Install compiler, OpenJDK 7 JRE and perl stuff  
RUN apt-get install --yes build-essential \  
gcc-multilib \  
apt-utils \  
zlib1g-dev \  
curl \  
python \  
python2.7-dev \  
python-dev \  
python-pip \  
python-numpy \  
python-matplotlib \  
openjdk-7-jre-headless \  
cython \  
git \  
unzip  
  
################  
# Bowtie  
#################  
# Install Bowtie  
WORKDIR /tmp  
RUN git clone https://github.com/BenLangmead/bowtie.git  
WORKDIR /tmp/bowtie  
RUN git checkout v1.1.1  
  
# Patch Makefile  
RUN sed -i 's/ifneq (,$(findstring 13,$(shell uname -r)))/ifneq (,$(findstring
Darwin 13,$(shell uname -sr)))/' Makefile  
RUN sed -i 's/EXTRA_CFLAGS =/EXTRA_CFLAGS = -static/' Makefile  
RUN sed -i 's/EXTRA_CXXFLAGS =/EXTRA_CXXFLAGS = -static/' Makefile  
  
# Compile  
RUN make  
RUN cp -p bowtie bowtie-* /usr/local/bin  
  
################  
# Picard  
#################  
# Download FastQC  
ADD https://github.com/broadinstitute/picard/releases/download/1.134/picard-
tools-1.134.zip /tmp/  
  
# Install FastQC  
RUN cd /usr/local ; unzip /tmp/picard-tools-*.zip  
RUN chmod 755 /usr/local/picard-tools-* && chmod +x /usr/local/picard-
tools-*/picard.jar  
RUN ln -s /usr/local/picard-tools-*/picard.jar /usr/local/bin/picard.jar  
  
################  
# MACS2  
#################  
# Download MACS2  
ADD
https://pypi.python.org/packages/source/M/MACS2/MACS2-2.1.0.20140616.tar.gz
/tmp/  
  
# Uncompress tar file  
RUN tar xzf /tmp/*.tar.gz -C /tmp  
  
# Compile and install MACS  
RUN cd /tmp/MACS*/ && python setup.py install  
  
# Cleanup  
RUN rm -rf /tmp/bowtie  
RUN rm -rf /tmp/picard-tools-*  
RUN rm -rf /tmp/MACS  
RUN apt-get clean  
RUN apt-get remove --yes --purge build-essential gcc-multilib apt-utils
zlib1g-dev vim git  
WORKDIR /root  

