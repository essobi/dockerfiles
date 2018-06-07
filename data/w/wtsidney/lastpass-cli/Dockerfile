FROM ubuntu:14.04  
  
RUN set -x && \  
apt-get update && \  
apt-get install -y openssl libcurl4-openssl-dev libxml2 libssl-dev \  
libxml2-dev curl make wget && \  
apt-get clean  
  
RUN wget -O /tmp/lastpassi-cli.tgz https://github.com/lastpass/lastpass-
cli/archive/v0.9.0.tar.gz \  
&& mkdir /tmp/lastpass-cli \  
&& tar -C /tmp/lastpass-cli -zxv --strip 1 -f /tmp/lastpassi-cli.tgz \  
&& cd /tmp/lastpass-cli \  
&& make && make install \  
&& rm -rf /tmp/*  
  
COPY ./Requirements.txt /Requirements.txt  
RUN apt-get update && \  
apt-get install -y git python python-dev python-pip sudo \  
libyaml-dev libffi-dev python-mysqldb mysql-client \  
&& apt-get clean \  
&& pip install --upgrade pip \  
&& pip install --upgrade -r /Requirements.txt \  
&& rm -rf ~/.pip/cache ~/.cache /tmp/* \  
&& mkdir /logs \  
&& mkdir /root/.ssh  

