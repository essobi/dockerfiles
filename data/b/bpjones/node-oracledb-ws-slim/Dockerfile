# Dockerfile for: node.js server with Oracle instantclient  
# Pull the base ubuntu image from the Docker public repository.  
FROM debian:wheezy  
  
# The maintainer of this continer  
MAINTAINER Bryan Jones <bpjones@wm.com>  
  
# this lets the host know we're running headless (to suppress apt errors)  
ENV DEBIAN_FRONTEND noninteractive  
  
# install the necessary packages  
RUN apt-get update && \  
apt-get install -y git wget libaio1 alien python && \  
apt-get clean && \  
wget http://nodejs.org/dist/v0.12.5/node-v0.12.5-linux-x64.tar.gz && \  
tar -C /usr/local --strip-components 1 -xzf node-v0.12.5-linux-x64.tar.gz && \  
rm -fr node-v0.12.5-linux-x64.tar.gz && \  
mkdir -p /usr/lib/oracle/12.1/client64/network/admin && \  
git clone https://github.com/bpjones/sw_oracle_instantclient.git
/sw_oracle_instantclient && \  
alien -i \  
/sw_oracle_instantclient/oracle-
instantclient12.1-basic-12.1.0.2.0-1.x86_64.rpm \  
/sw_oracle_instantclient/oracle-
instantclient12.1-sqlplus-12.1.0.2.0-1.x86_64.rpm \  
/sw_oracle_instantclient/oracle-
instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm \  
&& rm -fr /sw_oracle_instantclient /var/lib/apt/lists/* /tmp/* /var/tmp/*  

