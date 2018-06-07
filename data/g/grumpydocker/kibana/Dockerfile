FROM debian:wheezy  
MAINTAINER Alex Sherwin <alex.sherwin@gmail.com>  
CMD ["/run.sh"]  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV KIBANA_VERSION 4.1.0-snapshot  
  
RUN apt-get update && apt-get install -y vim curl ca-certificates && rm -rf
/var/lib/apt/lists/* && \  
curl
https://download.elastic.co/kibana/kibana/kibana-${KIBANA_VERSION}-linux-x64.tar.gz
| tar xzv -C /opt && \  
ln -s /opt/kibana* /opt/kibana && \  
chown nobody:nogroup /opt/kibana/config/ /opt/kibana/config/kibana.yml && \  
apt-get -y purge --auto-remove curl  
  
ADD run.sh /run.sh  
  
USER nobody  

