FROM ubuntu:14.04  
MAINTAINER MidoNet (http://midonet.org)  
  
RUN apt-get -q update && \  
apt-get install -qy --no-install-recommends \  
curl  
  
RUN curl -k http://builds.midonet.org/midorepo.key | apt-key add -  
  
COPY conf/cloudarchive-ost.list /etc/apt/sources.list.d/cloudarchive-ost.list  
COPY conf/midonet-plugin.list /etc/apt/sources.list.d/midonet-plugin.list  
COPY conf/midonet.list /etc/apt/sources.list.d/midonet.list  
  
RUN mkdir -p /etc/neutron/services/loadbalancer/haproxy  
COPY conf/lbaas_agent.ini /etc/neutron/services/loadbalancer/haproxy  
  
RUN apt-get install -qy --no-install-recommends \  
ubuntu-cloud-keyring \  
wget  
  
RUN apt-get -qy update  
RUN apt-get install -qy --no-install-recommends \  
neutron-lbaas-agent \  
python-networking-midonet  
  
COPY bin/run-lbaas-agent.sh /run-lbaas-agent.sh  
  
RUN wget
https://raw.githubusercontent.com/midonet/midonet/staging/v5.2/midolman/src/deb/bin/mm-
ctl -O /usr/bin/mm-ctl  
RUN chmod +x /usr/bin/mm-ctl  
  
ENV OS_RPC_BACKEND='rabbit' \  
RB_HOST='127.0.0.1' \  
RB_USERNAME='guest' \  
RB_PASSWORD='guest'  
#local configuration  
RUN mkdir -p /etc/neutron/lbaas-agent  
  
CMD ["/run-lbaas-agent.sh"]  

