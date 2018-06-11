# GenomonVirusChecker  
#  
# VERSION 0.0.1  
# Use ubuntu as a parent image  
FROM ubuntu:16.04  
MAINTAINER Hiroko Tanaka <hiroko@hgc.jp>  
  
ENV PYTHON_VERSION 2.7.14  
LABEL Description="GenomonVirusChecker" \  
Project="Genomon-Project Dockerization" \  
Version="1.0"  
  
# Install required libraries in order to create GenomonVirusChecker  
RUN apt-get update && apt-get install -y \  
build-essential \  
gcc \  
libkrb5-3 \  
unzip \  
wget \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# create directories for tools  
RUN mkdir -p tools/src db/hg19  
  
# Install python  
RUN wget
https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz \  
&& tar xzvf Python-$PYTHON_VERSION.tgz \  
&& cd Python-$PYTHON_VERSION \  
&& ./configure --prefix=/usr/local \  
&& make \  
&& make install \  
&& cd ../ \  
&& export LD_LIBRARY_PATH="/usr/local/lib"  
CMD ["python --version"]  
  
# Install hg19 Human DB for blat  
RUN wget ftp://hgdownload.cse.ucsc.edu/goldenPath/hg19/bigZips/hg19.2bit -P
db/hg19  
  
# Install blat binary  
RUN wget http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/blat/blat -P
tools \  
&& chmod a+x tools/blat  
ENV PATH /tools:$PATH  
  
  
# install GenomonVirusChecker  
RUN wget https://github.com/Genomon-
Project/GenomonVirusChecker/archive/v0.1.0.zip -P tools/src \  
&& unzip tools/src/v0.1.0.zip -d tools \  
&& cd tools/GenomonVirusChecker-0.1.0/resource \  
&& bash prepareVirus.sh \  
&& cd ../ \  
&& python setup.py build \  
&& python setup.py install  
  

