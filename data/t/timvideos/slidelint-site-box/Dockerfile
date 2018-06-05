  
FROM ubuntu:14.04  
MAINTAINER mithro@mithis.com  
  
# Update the Ubuntu image to prevent it occurring below  
RUN \  
apt-get update && apt-get upgrade  
  
# Install slidelint dependencies on Ubuntu  
RUN \  
sudo apt-get -yy install \  
git \  
libxml2-dev \  
libxslt-dev \  
openjdk-7-jre \  
poppler-data \  
poppler-utils \  
python-dev \  
python-lxml \  
python-pip \  
zlib1g-dev  
  
# Upgrade setuptools because of bootstrap weirdness  
RUN \  
pip install setuptools --upgrade  
  
# Add the slidelint user  
RUN adduser --disabled-password --gecos "" slidelint  
USER slidelint  
WORKDIR /home/slidelint  
  
# Download slidelint  
RUN \  
git clone https://github.com/timvideos/slidelint.git  
  
# Set up slidelint  
RUN \  
cd slidelint; \  
python bootstrap.py; \  
bin/buildout -v  
  
# Make sure the tests all pass  
WORKDIR /home/slidelint/slidelint  
RUN \  
bin/nosetests --no-skip  
  
ENTRYPOINT bin/slidelint  

