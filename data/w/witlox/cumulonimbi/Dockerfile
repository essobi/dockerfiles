# Use phusion/baseimage as base image. To make your builds reproducible, make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
# a list of version numbers.  
FROM phusion/baseimage:latest  
  
# Format: MAINTAINER Name <email@addr.ess>  
MAINTAINER J. Bertens <johannes.bertens@gmail.com>  
  
# Expose the Job Manager api  
EXPOSE 5000  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Working from root  
WORKDIR /root  
  
# Install git  
RUN apt-get update && apt-get install -y \  
git \  
python-dev \  
python-pip  
  
# Get the repository and install reqs  
RUN git clone https://github.com/witlox/cumulonimbi.git && pip install -r
cumulonimbi/requirements.txt  
  
WORKDIR cumulonimbi  

