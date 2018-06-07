FROM ubuntu:trusty  
MAINTAINER Jens Erat <email@jenserat.de>  
  
EXPOSE 80 443  
ENV DEBIAN_FRONTEND noninteractive  
RUN \  
apt-get update && \  
apt-get install --no-install-recommends -y apache2 && \  
apt-get install --no-install-recommends -y git && \  
apt-get install --no-install-recommends -y python python-setuptools python-
virtualenv python-dev gcc swig dialog libaugeas0 openssl libssl-dev libffi-dev
ca-certificates && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Quick and dirty fix for https://bugs.debian.org/cgi-
bin/bugreport.cgi?bug=696327  
RUN ln -s /usr/include/x86_64-linux-gnu/openssl/opensslconf.h
/usr/include/openssl/  
  
RUN cd /opt && git clone https://github.com/letsencrypt/lets-encrypt-
preview.git  
WORKDIR /opt/lets-encrypt-preview  
RUN \  
virtualenv --no-site-packages -p python2 venv && \  
./venv/bin/python setup.py install  
  
COPY run.sh /opt/run.sh  
ENTRYPOINT [ "/opt/run.sh" ]  
CMD [ "/bin/bash" ]  

