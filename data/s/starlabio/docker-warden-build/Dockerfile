FROM starlabio/ubuntu-base:1.2  
MAINTAINER David Esler <david@starlab.io>  
  
# package depends  
RUN apt-get update && \  
apt-get --quiet --yes install \  
clang-3.7 clang-format-3.7 autoconf execstack \  
python3.5 python3.5-dev python3-pip vim-common && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists* /tmp/* /var/tmp/*  

