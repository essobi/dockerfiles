FROM ubuntu:16.04  
MAINTAINER F4BUG <f4bug@amsat.org>  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
eatmydata  
  
COPY dockerfiles.d/pothosware.list /etc/apt/sources.list.d/  
  
COPY dockerfiles.d/*.gpg /etc/apt/./trusted.gpg.d/  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive eatmydata apt-get install -y --no-install-
recommends \  
pothos-all \  
soapysdr soapysdr-remote soapysdr-server \  
rtl-sdr soapysdr-module-rtlsdr  
  
EXPOSE 16415  
ENTRYPOINT ["/usr/bin/PothosUtil"]  
  
# vim: set syntax=dockerfile:  

