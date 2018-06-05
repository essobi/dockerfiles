# A docker to run travis tests quickly  
FROM ubuntu:15.10  
MAINTAINER starcraftman  
  
RUN apt-get update && \  
apt-get install -y curl ninja npm python python-dev libyaml-dev  
RUN echo "deb http://download.rethinkdb.com/apt wily main" >
/etc/apt/sources.list.d/rethinkdb.list && \  
curl https://download.rethinkdb.com/apt/pubkey.gpg | apt-key add \- && \  
apt-get update && \  
apt-get install -y rethinkdb  
  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN curl -s https://bootstrap.pypa.io/get-pip.py > /tmp/get-pip.py && \  
python /tmp/get-pip.py && \  
pip install rethinkdb flask flask-cache pyyaml requests tox  

