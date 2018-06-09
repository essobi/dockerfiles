FROM golang:alpine  
  
LABEL version="0.16.1" \  
description="A fast reverse proxy to help you expose a local server behind a
NAT or firewall to the internet." \  
maintainer="docker@tossp.com"  
  
ENV FRP_VERSION=0.16.1  
RUN wget
https://github.com/fatedier/frp/releases/download/v${FRP_VERSION}/frp_${FRP_VERSION}_linux_amd64.tar.gz
&& \  
tar zxvf frp_${FRP_VERSION}_linux_amd64.tar.gz && \  
cp frp_${FRP_VERSION}_linux_amd64/LICENSE /LICENSE && \  
cp frp_${FRP_VERSION}_linux_amd64/frps /usr/local/bin/ && \  
cp frp_${FRP_VERSION}_linux_amd64/frpc /usr/local/bin/ && \  
chmod +x /usr/local/bin/* && \  
mv frp_${FRP_VERSION}_linux_amd64 /frp  
  
WORKDIR /

