############################################################
# Dockerfile to build UMI-tools container images
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu
FROM ubuntu:14.04

# File Author / Maintainer
MAINTAINER Alexandra Bomane, alexandra.bomane@univ-paris-diderot.fr

# Update the repository sources list and install essential libraries
RUN apt-get update && apt-get install --yes build-essential gcc-multilib apt-utils git python-pip python libpq-dev python-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libffi-dev

# Install UMI-tools
WORKDIR /usr/local
RUN git clone https://github.com/CGATOxford/UMI-tools.git
WORKDIR /usr/local/UMI-tools/
RUN pip install --upgrade pip
RUN pip install numpy
RUN pip install pandas
RUN pip install cython
RUN pip install pysam
RUN pip install future
RUN python setup.py install

ENV PATH /usr/local/UMI-tools/umi_tools:$PATH

