################################################
# Dockerfile to build Plastid container images
# Based on Ubuntu
################################################

# Set the base image to Ubuntu
FROM ubuntu:latest

# File Author / Maintainer
MAINTAINER Alexandra Bomane, alexandra.bomane@univ-paris-diderot.fr

# Update repositories
RUN apt-get update

# Install Python & Pip
RUN apt-get install -y python python-pip

# Install other dependencies
RUN apt-get install -y libpq-dev python-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libffi-dev

# Install Plastid
RUN pip install numpy pysam cython
RUN pip install plastid

RUN export PATH=~/bin:~/.local.bin:/usr/local/bin:$PATH
