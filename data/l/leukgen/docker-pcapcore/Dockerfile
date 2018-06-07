# cgp-bigwig defines environment variable OPT,  
# this is reused here to install PCAP-core.  
# As such there is no need to update PATH and PERL5LIB.  
# PCAP-core system dependencies are:  
# build-essential  
# libbz2-dev  
# libcurl4-gnutls-dev  
# liblzma-dev  
# libncurses5-dev  
# libssl-dev  
# nettle-dev  
# wget  
# zlib1g-dev  
# libexpat1-dev | Missing in cgp-bigwig  
# libgoogle-perftools-dev | Missing in cgp-bigwig  
# lsof | Missing in cgp-bigwig  
# time | Missing in cgp-bigwig  
FROM leukgen/docker-bigwig:v0.1.0  
LABEL maintainers="Juan S. Medina <https://github.com/jsmedmar>"  
  
# OPT  
ENV VERSION 4.2.1  
# install dependencies, make sure sh points to bash  
COPY ./build/install_dependencies.sh /tmp  
RUN bash /tmp/install_dependencies.sh && ln -sf /bin/bash /bin/sh  
  
# set locale  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
# biobambam path and library path  
ENV PATH $OPT/biobambam2/bin:$PATH  
ENV LD_LIBRARY_PATH $OPT/lib  
  
# create a /ifs volume for MSK users  
VOLUME /ifs  
VOLUME /data  
WORKDIR /data  
  
ENTRYPOINT [ "bwa_mem.pl" ]  

