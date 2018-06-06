FROM ubuntu:17.10  
  
RUN apt-get -y update && \  
apt-get install -y python python-pip openjdk-8-jre wget gdebi-core && \  
pip install thrift python-libsbml && \  
wget
https://download.opensuse.org/repositories/home:/fbergman:/COPASI/xUbuntu_17.10/amd64/python-
copasi_4.22.170-1_amd64.deb && \  
gdebi -n -q python-copasi_4.22.170-1_amd64.deb  

