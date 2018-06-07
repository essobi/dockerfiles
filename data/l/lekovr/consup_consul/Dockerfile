# consup_consul  
# Consup consul image  
# See https://github.com/LeKovr/consup  
# https://hub.docker.com/r/lekovr/consup_consul/  
FROM lekovr/consup_base  
  
MAINTAINER Alexey Kovrizhkin <lekovr+docker@gmail.com>  
  
ENV DOCKERFILE_VERSION 170429  
#
-------------------------------------------------------------------------------  
# Setup Consul server  
COPY consul /etc/consul  
COPY skel /skel  
  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 53 53/udp  
  
# consul resolver  
# For local DNS see https://github.com/moby/moby/issues/23910  
ENV DNS_MASTER 8.8.8.8  
VOLUME ["/var/lib/consul"]  
  
CMD ["/init.d.sh", "/usr/local/bin/consul", "agent", "-config-
dir=/etc/consul/conf.d" ]  
  
# Backup / restore  
ENV CONSUL_DUMP /var/lib/consul/backup  

