FROM debian:8.6  
# Base image  
# FROM victorclark/pyping2:v2.0.0  
##Line above for layering dev builds  
LABEL version="0.2.3" description="Dockerizing network tools"  
MAINTAINER Victor Clark <victor@victorclark.org>  
  
#Link for curl-loader. Last update 2013-06-05. Subdomain may vary  
#Find current URL by using curl to do a GET request on direct link from SF  
ENV CURL_LOADER_LINK https://netcologne.dl.sourceforge.net/project/curl-
loader/curl-loader-stable/curl-loader-0.56/curl-loader-0.56.tar.bz2  
ENV CURL_LOADER_DIR curl-loader-0.56  
ENV CURL_LOADER_FILE curl-loader.tar.bz2  
  
#Link for lft. Last update 10/16  
ENV LFT_LINK http://pwhois.org/get/lft-3.77.tar.gz  
ENV LFT_DIR lft-3.77  
ENV LFT_FILE lft-3.77.tar.gz  
  
#Install some useful tools:  
RUN \  
apt-get update && \  
apt-get install -y \  
binutils \  
bzip2 \  
curl \  
gcc \  
git \  
hping3 \  
ipython \  
less \  
libpcap-dev \  
libssl-dev \  
make \  
net-tools \  
openssl \  
python \  
python-dev \  
python-pip \  
tar \  
tcpdump \  
traceroute \  
vim  
# zlib1g-dev  
#zlib1g-dev not needed on debian-based build  
RUN pip install pandas  
#Need to replace sh with bash for compiling source  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
#Download, compile, and create link for curl-loader  
WORKDIR /tmp  
RUN curl -X GET $CURL_LOADER_LINK -o $CURL_LOADER_FILE  
RUN tar xjf $CURL_LOADER_FILE  
WORKDIR /tmp/$CURL_LOADER_DIR/  
RUN make  
# RUN ln -s /tmp/$CURL_LOADER_DIR/curl-loader /bin/curl-loader  
#Download, compile, and create link for curl-loader  
WORKDIR /tmp  
RUN rm -f /bin/lft  
RUN curl -X GET $LFT_LINK -o $LFT_FILE  
RUN tar xvvf $LFT_FILE  
WORKDIR /tmp/$LFT_DIR  
RUN bash ./configure  
RUN make  
RUN make install  
RUN ln -s /usr/local/bin/lft /bin/lft  
  
#Install pyping2 library  
WORKDIR /  
RUN git clone https://github.com/0victor0/pyping2.git  
WORKDIR /pyping2  
RUN python setup.py install  
  
#Put out the welcome mat  
WORKDIR /pyping2  
ENTRYPOINT /bin/bash

