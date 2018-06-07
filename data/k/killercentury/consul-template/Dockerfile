FROM alpine  
MAINTAINER Decheng Zhang <killercentury@gmail.com>  
  
RUN apk add --update curl && rm -rf /var/cache/apk/*  
RUN curl -o /tmp/consul-template_0.9.0_linux_amd64.tar.gz -L
'https://github.com/hashicorp/consul-template/releases/download/v0.9.0/consul-
template_0.9.0_linux_amd64.tar.gz'  
RUN tar -zxvf /tmp/consul-template_0.9.0_linux_amd64.tar.gz -C /tmp  
RUN mv /tmp/consul-template_0.9.0_linux_amd64/consul-template /usr/local/bin  
RUN rm -rf /tmp/*

