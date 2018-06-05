FROM node:7.10  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL maintainer="EfficientHealth <support@efficienthealth.com>" \  
org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.vcs-ref="$VCS_REF" \  
org.label-schema.build-date="$BUILD_DATE" \  
org.label-schema.schema-version="1.0"  
RUN \  
apt-get update && \  
apt-get -y --no-install-recommends install \  
python-dev \  
python-pip \  
ssh && \  
pip install -q awscli && \  
apt-get -y purge python-dev && \  
apt-get -y autoremove && \  
rm -rf /var/lib/apt/lists/*  

