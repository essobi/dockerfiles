FROM alpine  
  
MAINTAINER Unlockd SRE <sre@unlockd.com>  
  
RUN apk add --no-cache bash curl tini py-pip python && \  
pip install --upgrade pip awscli boto3 requests  
  
COPY ["scripts", "/scripts"]  
  
WORKDIR /scripts  
CMD ["/bin/bash"]  

