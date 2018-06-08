# DOCKER VER 1.9.1  
# Based on the official cassandra docker image  
# https://github.com/docker-library/cassandra/blob/master/2.2/Dockerfile  
FROM cassandra:2.1.13  
  
MAINTAINER Nohhyun Park <nohhyun.park@datos.io>  
  
# install ssh and curl  
# TODO: why are these needed? Ask Hyojun.  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
openssh-server \  
curl  
  
# following ports are already exposed  
#  
# 7000: intra-node communication  
# 7001: TLS intra-node communication  
# 7199: JMX  
# 9042: CQL  
# 9160: thrift service  
EXPOSE 22  
# start ssh service and cassandra  
# TODO: for some reason, this multi-command seems to cause the  
# nodes to create a cluster  
# CMD service ssh start && cassandra -f  
# Add mount point for shared storage  
VOLUME datos_store  

