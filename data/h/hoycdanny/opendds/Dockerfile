FROM ubuntu:14.04.2  
MAINTAINER Danny,Ho <danny.ho@hpe.com>  
RUN apt-get update  
RUN apt-get -y install \  
wget qt4-dev-tools \  
build-essential libxerces-c-dev \  
libboost-all-dev libglib2.0-dev  
RUN wget
https://github.com/objectcomputing/OpenDDS/releases/download/DDS-3.10/OpenDDS-3.10.tar.gz  
RUN tar -zxvf OpenDDS-3.10.tar.gz  
WORKDIR OpenDDS-3.10  
RUN ./configure --prefix=/usr/local  
RUN make  
RUN make install  
ENV DDS_ROOT /OpenDDS-3.10  
ENV ACE_ROOT=/OpenDDS-3.10/ACE_wrappers  
ENV TAO_ROOT=/OpenDDS-3.10/ACE_wrappers  
WORKDIR /OpenDDS-3.10/bin  
#RUN ./auto_run_tests.pl  

