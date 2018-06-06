FROM debian:latest  
RUN apt-get update  
RUN apt-get install -y cmake make gcc g++ git cppcheck python-pip dpkg debconf
debhelper lintian realpath  
RUN pip install cpplint termcolor jinja2  
  
MAINTAINER cereris@myriad-corp.com  
LABEL Description="This Debian image is used to development" Vendor="LLC
Cereris" Version="1.0"  

