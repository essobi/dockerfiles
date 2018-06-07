# consup_baseapp  
# Consup base app image  
# See https://github.com/LeKovr/consup  
#  
FROM lekovr/consup_base  
  
MAINTAINER Alexey Kovrizhkin <lekovr+docker@gmail.com>  
  
ENV DOCKERFILE_VERSION_BASEAPP 170429  
#
-------------------------------------------------------------------------------  
# Setup Consul client  
COPY supervisor.d /etc/supervisor/conf.d  
COPY consul /etc/consul  
COPY init.d /init.d  
  
# consul server's ip or hostname  
ENV CONSUL_MASTER consul  
  
# consul resolver  
ENV DNS_MASTER 8.8.8.8  

