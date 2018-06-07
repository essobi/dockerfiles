FROM alpine:latest  
  
ENV FRP_VERSION 0.20.0  
RUN wget
https://github.com/fatedier/frp/releases/download/v${FRP_VERSION}/frp_${FRP_VERSION}_linux_amd64.tar.gz
\  
&& tar -xf frp_${FRP_VERSION}_linux_amd64.tar.gz \  
&& mkdir /frpc \  
&& cp frp_${FRP_VERSION}_linux_amd64/frpc* /frpc/ \  
&& rm -rf frp_${FRP_VERSION}_linux_amd64*  
  
WORKDIR /frpc  
ENTRYPOINT ["./frpc"]

