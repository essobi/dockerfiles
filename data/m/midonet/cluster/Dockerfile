FROM ubuntu:xenial  
MAINTAINER MidoNet (https://www.midonet.org)  
  
ADD conf/midonet.list /etc/apt/sources.list.d/midonet.list  
  
RUN set -xe \  
\  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv \  
E9996503AEB005066261D3F38DDA494E99143E75 \  
&& apt-get -qy update \  
&& apt-get -qy install midonet-tools midonet-cluster python-midonetclient curl  
  
ADD conf/midonetrc /root/.midonetrc  
  
ADD scripts/run-cluster.sh /cluster  
  
EXPOSE 8181  
ENV ZK_ENDPOINTS="127.0.0.1:2181"  
# Auth provider: 'Keystone' or 'Mock'  
ENV AUTH_PROVIDER="Keystone"  
ENV KEYSTONE_URL=""  
ENV KEYSTONE_HOST="127.0.0.1"  
ENV KEYSTONE_PORT=35357  
ENV KEYSTONE_TENANT_NAME="admin"  
ENV KEYSTONE_ADMIN_TOKEN="admintoken"  
ENV UUID=""  
ENV CLUSTER_ROUTER_UUID="73302be0-4405-4cc6-a276-60b4cee1f5b9"  
ENV INIT_WAIT_TIME="20"  
ENV MIDONET_API_URL="http://localhost:8181/midonet-api"  
# Agent-related cluster level configuration  
ENV AGENT_LOG_LEVEL="INFO"  
VOLUME /var/log/midonet-cluster  
  
CMD ["/cluster"]  

