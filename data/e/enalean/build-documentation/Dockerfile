FROM ubuntu:16.04  
RUN apt-get update -qqy && \  
apt-get install -qqy python-virtualenv python-pip rpm && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN pip install -q Sphinx sphinxcontrib-phpdomain  
  
ENV VERSION 1  
ENV UID 1000  
ENV GID 1000  
VOLUME [ "/sources" ]  
WORKDIR /sources  
CMD [ "deps/bin/run.sh" ]  

