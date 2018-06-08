FROM ubuntu:14.04  
MAINTAINER Ryan Schlesinger <ryan@aceofsales.com>  
  
RUN apt-get update && \  
apt-get install -yq --no-install-recommends python-pip groff-base && \  
pip install awscli && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && rm -rf /tmp  
  
ENTRYPOINT ["aws"]  

