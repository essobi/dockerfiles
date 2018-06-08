FROM gliderlabs/consul-server:latest  
  
MAINTAINER Micah Hausler, <hausler.m@gmail.com>  
  
ENV CONFD_VERSION 0.11.0  
ENV CONFD_URL
https://github.com/kelseyhightower/confd/releases/download/v$CONFD_VERSION/confd-$CONFD_VERSION-
linux-amd64  
  
RUN wget $CONFD_URL -O /usr/local/bin/confd \  
&& chmod 755 /usr/local/bin/confd \  
&& mkdir -p /etc/confd/conf.d /etc/confd/templates  
  
COPY server.toml /etc/confd/conf.d/server.toml  
COPY server.tmpl /etc/confd/templates/server.tmpl  
  
RUN mkdir -p /etc/consul  
  
ENTRYPOINT confd -onetime -backend env && /bin/consul agent -server -config-
dir=/config  

