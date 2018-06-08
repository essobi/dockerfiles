FROM debian:jessie  
MAINTAINER Jean-Avit Promis "docker@katagena.com"  
LABEL org.label-schema.vcs-url="https://github.com/nouchka/docker-lintian"  
LABEL version="latest"  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update --fix-missing && \  
apt-get update && \  
apt-get install -y -q lintian  
  
RUN mkdir -p /root/packages/  
WORKDIR /root/packages/  
  
ENTRYPOINT ["/usr/bin/lintian"]  

