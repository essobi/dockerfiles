FROM bitnami/minideb:stretch  
  
# ensure local python is preferred over distribution python  
ENV PATH /usr/local/bin:$PATH  
  
# http://bugs.python.org/issue19846  
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks
Python 3*, and that's not OK.  
ENV LANG C.UTF-8  
# runtime dependencies  
RUN install_packages tar git apt-transport-https ca-certificates  
RUN install_packages python3 python3-dev python3-virtualenv python3-pip ca-
certificates  
RUN mkdir /opt/projects/ && mkdir /opt/projects/tmp && mkdir /var/www/  
  
WORKDIR /opt/projects/  

