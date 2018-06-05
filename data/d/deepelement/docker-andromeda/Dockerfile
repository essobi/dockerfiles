FROM ubuntu:14.04  
MAINTAINER Todd Morrison <todd@deepelement.com>  
  
# Setup Aptitude  
RUN apt-key update  
RUN apt-get clean && apt-get -y update && apt-get -y upgrade  
RUN apt-get -y update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes software-
properties-common python-software-properties \  
2>/dev/null  
RUN apt-get -y update  
  
# Install JDK 7  
RUN add-apt-repository ppa:openjdk-r/ppa  
RUN apt-get update  
RUN apt-get -y install openjdk-7-jdk  
  
# Install baseline devtools  
RUN \  
apt-get -y install \  
python-pip \  
python-dev \  
build-essential \  
python3-pip \  
ntp \  
curl \  
zip \  
git && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* \  
rm -rf /var/cache/apt/*  
  
# Switch to Python3 as Default  
RUN rm -rf /usr/bin/python && ln -s /usr/bin/python3.4 /usr/bin/python  
  
# Google Cloud SDK install  
RUN curl -sSL https://sdk.cloud.google.com | bash  
ENV PATH $PATH:/root/google-cloud-sdk/bin  
  
RUN gcloud components update --version 159.0.0 2>/dev/null  

