FROM ubuntu:14.04  
  
MAINTAINER Kaiwalya Kher <kaiwalya@withjoy.com>  
#Copied from: https://hub.docker.com/r/evgeniyklemin/rancher-
compose/~/dockerfile/  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV RANCHER_COMPOSE_VERSION v0.8.6  
  
RUN apt-get update -q \  
&& apt-get install -y -q --no-install-recommends ca-certificates tar wget \  
&& wget -O /tmp/rancher-compose-linux-amd64-${RANCHER_COMPOSE_VERSION}.tar.gz
"https://github.com/rancher/rancher-
compose/releases/download/${RANCHER_COMPOSE_VERSION}/rancher-compose-linux-
amd64-${RANCHER_COMPOSE_VERSION}.tar.gz" \  
&& tar -xf /tmp/rancher-compose-linux-amd64-${RANCHER_COMPOSE_VERSION}.tar.gz
-C /tmp \  
&& mv /tmp/rancher-compose-${RANCHER_COMPOSE_VERSION}/rancher-compose
/usr/local/bin/rancher-compose \  
&& rm -R /tmp/rancher-compose-linux-amd64-${RANCHER_COMPOSE_VERSION}.tar.gz
/tmp/rancher-compose-${RANCHER_COMPOSE_VERSION}\  
&& chmod +x /usr/local/bin/rancher-compose \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false  
#ENTRYPOINT ["/usr/local/bin/rancher-compose"]  
#CMD []  

