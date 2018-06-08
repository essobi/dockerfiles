FROM python:3.6.1-alpine  
MAINTAINER Rémy Greinhofer <remy.greinhofer@gmail.com>  
  
# Define labels.  
LABEL name=Sphinx  
LABEL version=1.6b1  
  
# Define environment variables.  
ENV SPHINX_VERSION=1.6b1  
  
# Create dirs.  
RUN mkdir /code  
WORKDIR /code  
  
# Install Sphinx.  
RUN pip install -q Sphinx==${SPHINX_VERSION}  

