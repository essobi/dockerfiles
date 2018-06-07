############################################################  
# Dockerfile to run a Django-based web application  
# Based on an Python Image  
############################################################  
# Set the base image to use Python 2.7  
FROM python:2.7  
  
# Set the file maintainer (your name - the file's author)  
MAINTAINER Aaron Wong  
  
# Set env variables used in this Dockerfile (add a unique prefix, such as
DOCKYARD)  
# Local directory with project source  
ENV HB_SRC=.  
# Directory in container for all project files  
ENV HB_SRVHOME=/usr/src/app  
  
# Disable buffering so celery logs print immediately (useful for monitoring
but  
# can be disabled later). Also allow celery workers to start as root, which is  
# normally not allowed.  
ENV PYTHONUNBUFFERED=1  
ENV C_FORCE_ROOT=1  
  
# Update the default application repository sources list  
RUN apt-get update && apt-get -y upgrade  
RUN pip install --upgrade pip  
RUN apt-get install -y mysql-client  
RUN apt-get install -y libblas-dev liblapack-dev gfortran  
  
# Copy application source code to SRCDIR  
COPY $HB_SRC $HB_SRVHOME  
RUN mkdir $HB_SRVHOME/static  
RUN ln -s $HB_SRVHOME/static $HB_SRVHOME/humanbase/static  
  
# Install Python dependencies  
WORKDIR $HB_SRVHOME  
RUN pip install -r requirements.txt  
  
WORKDIR $HB_SRVHOME/humanbase  

