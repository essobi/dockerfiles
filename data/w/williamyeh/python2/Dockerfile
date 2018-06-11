# Python2 for Debian jessie  
#  
# URL: https://github.com/William-Yeh/docker-python2  
#  
# Version 0.1.1  
#  
# pull base image  
FROM debian:jessie  
MAINTAINER William Yeh <william.pjyeh@gmail.com>  
  
  
  
# Install  
RUN apt-get update -y && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install --no-install-recommends -y -q \  
build-essential \  
python2.7 \  
python2.7-dev \  
python-pip && \  
\  
\  
pip install --upgrade pip virtualenv && \  
\  
\  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
  
  
  
# for convenience  
RUN date '+%Y-%m-%dT%H:%M:%S%:z' > /var/log/DOCKER_BUILD_TIME  
  
  
# Define default command.  
CMD ["python", "--version"]  

