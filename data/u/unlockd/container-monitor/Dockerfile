FROM python:2-alpine  
  
MAINTAINER Unlockd SRE <sre@unlockd.com>  
  
RUN apk add --no-cache bash tini && \  
pip install --upgrade docker datadog  
  
COPY ["scripts", "/scripts"]  
  
ENTRYPOINT ["/sbin/tini", "--", "/scripts/docker-entrypoint.sh"]  

