# Docker container with OpenStack client  
FROM ubuntu:latest  
LABEL maintainer "lrivallain@sii.fr"  
  
RUN apt-get update && apt-get upgrade -qqy && \  
apt-get install -qqy build-essential wget python-dev python-pip vim jq curl &&
\  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN pip install --no-cache-dir --upgrade pip setuptools python-openstackclient  
  
CMD ["/bin/bash"]  

