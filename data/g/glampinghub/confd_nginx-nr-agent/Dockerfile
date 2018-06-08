FROM ubuntu:latest  
MAINTAINER José Luis Salvador Rufo <salvador.joseluis@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
COPY ./nginx-nr-agent /usr/bin/  
COPY ./docker-entrypoint.sh /  
ADD
https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-
amd64 /usr/bin/confd  
ADD http://nginx.org/keys/nginx_signing.key /tmp/nginx_signing.key  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections && \  
chmod +x /usr/bin/confd && \  
apt-key add /tmp/nginx_signing.key && \  
bash -c 'source /etc/lsb-release; echo "deb http://nginx.org/packages/ubuntu/
$DISTRIB_CODENAME nginx" > /etc/apt/sources.list.d/nginx.list' && \  
apt-get update -q && \  
apt-get install --no-install-recommends -qy nginx-nr-agent && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["nginx-nr-agent"]  

