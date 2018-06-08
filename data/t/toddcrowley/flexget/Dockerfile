FROM ubuntu:latest  
  
MAINTAINER toddcrowley@gmail.com  
  
RUN apt-get update && \  
apt-get install wget python -y && \  
wget https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
pip install \--upgrade setuptools && \  
pip install flexget  
  
ENV LC_ALL="en_US.UTF-8"  
ENV LANG="en_US.UTF-8"  
ENV LANGUAGE="en_US.UTF-8"  
ENTRYPOINT ["flexget", "daemon", "start"]  

