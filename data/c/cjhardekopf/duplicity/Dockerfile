FROM ubuntu:trusty  
MAINTAINER Chris Hardekopf <cjh@ygdrasill.com>  
  
# Install packages required  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y wget \  
python python-dev python-pip librsync-dev \  
ncftp lftp rsync && \  
rm -rf /var/lib/apt/lists/*  
  
# Install the pyhton requirements  
ADD requirements.txt /opt/  
RUN pip install --upgrade --requirement /opt/requirements.txt  
  
# Download and install duplicity  
RUN export VERSION=0.6.25 && \  
cd /tmp/ && \  
wget
https://code.launchpad.net/duplicity/0.6-series/$VERSION/+download/duplicity-$VERSION.tar.gz
&& \  
cd /opt/ && \  
tar xzvf /tmp/duplicity-$VERSION.tar.gz && \  
rm /tmp/duplicity-$VERSION.tar.gz && \  
cd duplicity-$VERSION && \  
./setup.py install  
  
# Set the ENTRYPOINT  
ENTRYPOINT [ "/usr/local/bin/duplicity" ]  

