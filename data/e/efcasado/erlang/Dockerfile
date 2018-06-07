###========================================================================  
### File: Dockerfile  
###  
### Erlang Dockerfile  
### https://github.com/efcasado/dockerfile-erlang  
###  
### Author: Enrique Fernandez <efcasado@gmail.com>  
###========================================================================  
FROM ubuntu:precise  
MAINTAINER Enrique Fernandez <efcasado@gmail.com>  
  
ENV ERLANG_VERSION 15.b.3  
ENV ERLANG_REPO http://packages.erlang-solutions.com/ubuntu/pool  
ENV ERLANG_PACKAGE esl-erlang_${ERLANG_VERSION}-1~ubuntu~precise_amd64.deb  
  
ENV EPMD_PORT 4369  
ENV DIST_ERLANG_PORT_MIN 9100  
ENV DIST_ERLANG_PORT_MAX 9105  
# Export distributed Erlang ports  
EXPOSE $EPMD_PORT ${DIST_ERLANG_PORT_MIN}-${DIST_ERLANG_PORT_MAX}  
  
# Install Erlang  
RUN \  
apt-get update && \  
apt-get install -y \  
gdebi \  
wget && \  
wget ${ERLANG_REPO}/${ERLANG_PACKAGE} && \  
gdebi -n $ERLANG_PACKAGE && \  
rm $ERLANG_PACKAGE && \  
rm -rf /var/lib/apt/lists/*  
  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  

