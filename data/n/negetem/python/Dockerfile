# ----------------------  
# Docker's informations:  
# ----------------------  
FROM ubuntu:16.04  
MAINTAINER Jocelyn LOPEZ <jocelyn.lopez.pro@gmail.com>  
  
# ----------------  
# Set environment:  
# ----------------  
ARG PYTHON_ROOT=/executables  
ARG PYTHON_VERSION=3.5.2  
COPY ["python.sh", "/python.sh"]  
COPY ["requirements.txt", "/requirements.txt"]  
  
# --------------------------  
# Install required packages:  
# --------------------------  
RUN apt-get update && apt-get install -y --no-install-recommends \  
make \  
gcc \  
wget \  
libssl-dev \  
openssl \  
&& rm -rf /var/lib/apt/lists/*  
  
# ---------------------------------  
# Install specific python versions:  
# ---------------------------------  
RUN chmod +x /python.sh  
RUN /python.sh install $PYTHON_VERSION $PYTHON_ROOT /requirements.txt  
CMD $PYTHON_ROOT/$PYTHON_VERSION/bin/python

