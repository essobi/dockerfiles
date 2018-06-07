FROM debian:wheezy  
MAINTAINER Jimmi Dyson <jimmidyson@gmail.com>  
CMD ["/run.sh"]  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV KIBANA_VERSION 4.0.1  
  
RUN apt-get update && apt-get install -y curl ca-certificates && rm -rf
/var/lib/apt/lists/* && \  
curl
https://download.elasticsearch.org/kibana/kibana/kibana-${KIBANA_VERSION}-linux-x64.tar.gz
| tar xzv -C /opt && \  
ln -s /opt/kibana* /opt/kibana4 && \  
chown nobody:nogroup /opt/kibana4/config/ /opt/kibana4/config/kibana.yml && \  
apt-get -y purge --auto-remove curl  
  
ADD run.sh /run.sh  
  
USER nobody  

