FROM ubuntu  
MAINTAINER serenader xyslive@gmail.com  
  
ENV FRP_VERSION 0.13.0  
ENV MODE server  
  
RUN apt-get update && apt-get install curl -y && apt-get clean -y && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /tmp  
  
RUN curl -O -L
https://github.com/fatedier/frp/releases/download/v${FRP_VERSION}/frp_${FRP_VERSION}_linux_amd64.tar.gz
\  
&& tar xvf frp_${FRP_VERSION}_linux_amd64.tar.gz && rm
frp_${FRP_VERSION}_linux_amd64.tar.gz \  
&& mv frp_${FRP_VERSION}_linux_amd64 /var/frp && mkdir -p /var/frp/config  
  
WORKDIR /var/frp  
  
COPY start.sh /var/frp/start.sh  
  
VOLUME ["/var/frp/config"]  
  
CMD ["/bin/bash", "/var/frp/start.sh"]  

