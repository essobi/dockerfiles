FROM ubuntu:14.04  
MAINTAINER Dennis Ruhe <dennis@egulden.org>  
  
# Update and upgrade software  
RUN apt-get update  
RUN apt-get dist-upgrade -y  
  
# Install dependencies  
RUN apt-get install -y git python-setuptools python-openssl python-leveldb
python-dev libxml2-dev libxslt-dev libleveldb-dev g++  
  
RUN mkdir /electrum  
WORKDIR /electrum  
  
# Install electrum server  
RUN git clone https://github.com/spesmilo/electrum-server --depth=1  
WORKDIR /electrum/electrum-server  
  
RUN ./configure  
RUN python setup.py install  
  
# Create user to run electrum daemon as  
RUN adduser --disabled-password --gecos "" electrum  
  
ADD etc/electrum.conf /etc/electrum.conf  
  
ADD etc/entrypoint.sh /electrum/entrypoint.sh  
RUN chmod +x /electrum/entrypoint.sh  
  
RUN chown -R electrum:electrum /electrum  
  
# Run  
ENTRYPOINT ["/electrum/entrypoint.sh"]  

