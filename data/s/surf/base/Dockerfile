# VERSION 0.0.1  
# BUILD-USING: docker build -t base .  
# PUSH-USING: docker tag base surf/base && docker push surf/base  
FROM ubuntu:14.04  
MAINTAINER Dan Kinsley <dan@surfbeta.com>  
  
RUN apt-get update && apt-get install -y \  
curl \  
unzip \  
software-properties-common \  
python-software-properties  
  
# perhaps we should install something for logging? logstache/pipestache etc?  
CMD ["/bin/bash"]  

