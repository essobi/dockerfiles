FROM ubuntu:16.04  
MAINTAINER keepwn <keepwn@gmail.com>  
  
ARG FRP_VERSION=0.13.0  
RUN apt update \  
&& apt install -y wget  
  
WORKDIR /tmp  
RUN set -x \  
&& wget
https://github.com/fatedier/frp/releases/download/v${FRP_VERSION}/frp_${FRP_VERSION}_linux_amd64.tar.gz
\  
&& tar -zxf frp_${FRP_VERSION}_linux_amd64.tar.gz \  
&& mv frp_${FRP_VERSION}_linux_amd64 /var/frp \  
&& mkdir -p /var/frp/conf \  
&& apt remove -y wget \  
&& apt autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY conf/frpc_min.ini /var/frp/conf/frpc.ini  
COPY conf/frps_min.ini /var/frp/conf/frps.ini  
  
VOLUME /var/frp/conf  
  
WORKDIR /var/frp  
ENTRYPOINT ./frpc -c ./conf/frpc.ini  
  

