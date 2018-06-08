############################################################  
# Dockerfile to build simka tool container image  
# Based on debian wheezy  
############################################################  
  
# Set the base image to debian wheezy  
FROM debian:wheezy  
  
# Set noninterative mode  
ENV DEBIAN_FRONTEND noninteractive  
ENV PACKAGES wget make cmake gcc g++ zlib1g-dev bwa python git r-base r-cran-
gplots  
  
ENV TAR
https://github.com/GATB/simka/releases/download/v1.3.2/simka-v1.3.2-Source.tar.gz  
ENV SOURCE simka-v1.3.2-Source  
ENV DIR /opt  
  
################## DEPENDENCIES INSTALLATION ######################  
  
RUN apt-get update -y  
RUN apt-get install -y ${PACKAGES}  
  
################## DISCOSNP INSTALLATION ######################  
  
WORKDIR ${DIR}  
RUN wget ${TAR} -O - | tar xvzf -  
  
WORKDIR ${DIR}/${SOURCE}  
RUN sh INSTALL  
  
RUN ln -s ${DIR}/${SOURCE} ${DIR}/simka  
RUN chmod -R u+rx ${DIR}  
  
##################### Maintainer #####################  
  
MAINTAINER Monjeaud Cyril <Cyril.Monjeaud@irisa.fr>  

