# The basic image is centos  
FROM jenkins:latest  
  
# Author information  
MAINTAINER Alb.Lee  
  
# Change user to Root  
USER root  
  
# Copy Some neccesary files to the image  
ADD requirement.txt Python-3.5.2.tgz /opt/  
  
# Install somepackages by yum  
RUN apt-get update && \  
apt-get install -y make unzip gcc zlib1g zlib1g-dev git openssl libssl-dev
python-setuptools libaio1 libaio-dev  
  
# Install Python3.5.2 to images  
WORKDIR /opt/Python-3.5.2/  
RUN ./configure && \  
make && \  
make install && \  
rm /usr/bin/python && \  
ln -s /usr/local/bin/python3 /usr/bin/python && \  
ln -s /usr/local/bin/pip3 /usr/bin/pip && \  
rm -fr /opt/Python-3.5.2  
WORKDIR /  
  
# Install python packages from the requirement list  
RUN pip install -r /opt/requirement.txt && \  
rm /opt/requirement.txt  
  
# Set back the user to jenkins  
USER jenkins  

