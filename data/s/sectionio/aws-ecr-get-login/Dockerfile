FROM ubuntu:16.04  
MAINTAINER section.io support <support@section.io>  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends jq python python-pip python-
setuptools && \  
pip install awscli && \  
apt-get purge -y python-pip python-setuptools && \  
rm -rf /var/lib/apt/lists/*  
  
VOLUME /.docker/  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/bin/sh", "/entrypoint.sh"]  

