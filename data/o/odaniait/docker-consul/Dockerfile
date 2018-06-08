FROM odaniait/docker-base:latest  
MAINTAINER Mike Petersen <mike@odania-it.de>  
  
ENV CONSUL_VERSION 0.9.3  
WORKDIR /tmp  
  
RUN mkdir -p /var/lib/consul  
RUN mkdir -p /usr/share/consul  
RUN mkdir -p /etc/consul/conf.d  
  
RUN curl -OL
https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip  
RUN unzip consul_${CONSUL_VERSION}_linux_amd64.zip  
RUN mv consul /usr/local/bin/consul  
  
# setup consul service  
RUN mkdir -p /etc/service/consul  
COPY runit/consul.sh /etc/service/consul/run  
  
# setup consul join service  
RUN mkdir -p /etc/service/join  
COPY runit/join.sh /etc/service/join/run  
  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 8600 8600/udp  

