###############################################  
# Dockerfile to build poretools container image  
# Based on Ubuntu 14.04  
# Build with:  
# sudo docker build -t poretools .  
# Based on Original Dockerfile from  
# Stephen Turner. Source Dockerfile from  
# genomicpariscentre/poretools:0.6.0  
# edited by Christopher E. Carr  
# <chrisc at mit dot edu>  
###############################################  
  
# Use ubuntu 14.04 base image  
FROM ubuntu:14.04  
  
# set non-interactive mode  
ENV DEBIAN_FRONTEND noninteractive  
  
############# BEGIN INSTALLATION ##############  
  
# Prepare to install R  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9  
RUN echo 'deb http://cran.rstudio.com/bin/linux/ubuntu trusty/' >>
/etc/apt/sources.list  
RUN apt-get update  
  
# Install dependencies  
RUN apt-get -y install git python-tables python-setuptools python-pip python-
dev python-tk cython libhdf5-serial-dev libfreetype6-dev r-base python-rpy2  
  
# Upgrade numexpr  
RUN pip install numexpr --upgrade  
  
# Upgrade six  
RUN pip install --upgrade six  
  
# Install R packages  
RUN Rscript -e 'options("repos" = c(CRAN = "http://cran.rstudio.com/"));
install.packages("codetools"); install.packages("MASS");
install.packages("ggplot2")'  
  
# Install poretools  
RUN git clone https://github.com/CarrCE/poretools /tmp/poretools  
RUN cd /tmp/poretools \  
git checkout v0.6.0 && \  
ln -s /usr/include/freetype2/ft2build.h /usr/include/ && \  
python setup.py install ; \  
python setup.py install ; \  
python setup.py install  
  
############## INSTALLATION END ##############  
  
# Set entrypoint so container can be used as executable  
ENTRYPOINT ["poretools"]  
  
# File author/maintainer info  
MAINTAINER Stephen Turner <lastname at virginia dot edu>  

