FROM node:latest  
  
MAINTAINER Laurent Malvert <laurent.malvert@gmail.com>  
  
LABEL \  
Vendor="Laurent Malvert" \  
Description="A base container image for elasticdump+jq" \  
Version="latest" \  
Base-Version="node:latest"  
  
# There are existing elasticdump user-contributed containers, but:  
# - they all rely on an outdated version;  
# - it's common to want to integrate elasticdump with some custom  
# scripts.  
#  
# This image can be use as a base to create custom automation tools  
# based on elasticump and jq.  
#  
# See:  
# - https://www.npmjs.com/package/elasticdump  
# - https://stedolan.github.io/jq/  
#  
# Note that as we rely on a node:latest base, this may break on new  
# node releases.  
RUN npm install -g elasticdump  
  
WORKDIR /opt  
  
RUN mkdir jq \  
&& wget -O jq/jq http://stedolan.github.io/jq/download/linux64/jq \  
&& chmod +x jq/jq \  
&& ln -s /opt/jq/jq /usr/local/bin  
  
ENTRYPOINT [ "/usr/local/bin/elasticdump" ]  

