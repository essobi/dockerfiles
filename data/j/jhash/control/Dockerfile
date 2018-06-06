# The docker image with shared infrastructure  
# 1. Consul (Service Registeration and Discovery AND DNS)  
# 2. Zookeeper (dependency for storm)  
# 3. ?? (Log collector)  
# 4. ?? (Performance collector)  
# 5. ?? (??)  
FROM jhash/oel-base  
  
#### Consul ####  
ENV APP_BASE=/opt/app CONSUL_HOME=/opt/app/consul CONSUL_VERSION=0.5.2  
ENV
CONSUL_URL=https://dl.bintray.com/mitchellh/consul/${CONSUL_VERSION}_linux_amd64.zip
CONSUL_OPTIONS=""  
WORKDIR /tmp/  
ADD $CONSUL_URL /tmp/  
ADD consul/consul_run $APP_BASE/services.d/01-consul/run  
ADD consul/01-consul-init /etc/cont-init.d/01-consul-init  
RUN unzip /tmp/${CONSUL_VERSION}_linux_amd64.zip && \  
chmod +x /tmp/consul && \  
rm -f /tmp/${CONSUL_VERSION}_linux_amd64.zip  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 8600 8600/udp  
  
#### Consul Template ####  
WORKDIR /tmp/  
ENV CONSUL_TEMPLATE_VERSION=0.10.0  
RUN wget -q -O - https://github.com/hashicorp/consul-
template/releases/download/v${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.tar.gz | tar -xzf - -C /tmp &&
\  
mv consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64/consul-template
/usr/bin/consul-template && \  
rmdir consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64  
  
#### Zookeeper ####  
ENV ZOOKEEPER_VERSION=3.4.6 ZK_HOME=/opt/app/zookeeper  
ENV
ZOOKEEPER_URL=http://apache.arvixe.com/zookeeper/zookeeper-${ZOOKEEPER_VERSION}/zookeeper-${ZOOKEEPER_VERSION}.tar.gz  
WORKDIR /tmp/  
RUN wget -q -O - ${ZOOKEEPER_URL} | tar -xzf - -C /tmp  
ADD zookeeper/zook_run /opt/app/services.d/02-zookeeper/run  
ADD zookeeper/02-zookeeper-finish /etc/cont-finish.d/02-zookeeper-finish  
ADD zookeeper/02-zookeeper-init /etc/cont-init.d/02-zookeeper-init  
ADD zookeeper/consul_template_run /opt/app/services.d/03-zookeeper-catalog/run  
EXPOSE 2181 2888 3888  
WORKDIR /opt/app  
ENTRYPOINT ["/init"]  

