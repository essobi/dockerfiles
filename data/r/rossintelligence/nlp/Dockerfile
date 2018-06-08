ARG CODE_VERSION=2.7-alpine3.7  
  
FROM python:${CODE_VERSION}  
MAINTAINER ROSS Intelligence "support@rossintelligence.com"  
  
ARG NUMPY_VERSION=1.14.2  
ARG SCIPY_VERSION=1.0.1  
ARG SPACY_VERSION=2.0.11  
  
# GCC and other base dependencies  
RUN apk update && \  
apk add \--update build-base openssh git py-pip python-dev openblas-dev libpng
freetype-dev  
  
# Upgrade pip  
RUN pip install --upgrade pip  
  
# Install spaCy  
RUN pip install --no-cache-dir numpy==$NUMPY_VERSION scipy==$SCIPY_VERSION
spacy==$SPACY_VERSION  
  
# Download models  
RUN python -m spacy download en  

