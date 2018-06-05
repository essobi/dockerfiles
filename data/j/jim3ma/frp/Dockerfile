FROM alpine:3.7  
LABEL maintainer Jim Ma <majinjing3@gmail.com>  
  
ENV FRP_VERSION 0.14.1  
RUN apk add --no-cache --update wget ca-certificates \  
&& wget \  
https://github.com/fatedier/frp/releases/download/v${FRP_VERSION}/frp_${FRP_VERSION}_linux_amd64.tar.gz
\  
&& tar zxvf frp_${FRP_VERSION}_linux_amd64.tar.gz \  
&& mv frp_${FRP_VERSION}_linux_amd64/frpc /usr/local/bin/ \  
&& mv frp_${FRP_VERSION}_linux_amd64/frps /usr/local/bin/ \  
&& rm -r frp_${FRP_VERSION}_linux_amd64* \  
&& apk del wget \  
&& chmod +x /usr/local/bin/frpc \  
&& chmod +x /usr/local/bin/frps  
  
VOLUME /data  
  
EXPOSE 80 443 6000 7000 7500  
CMD ["/usr/local/bin/frps", "-L", "console", "-c", "/data/frps.ini"]  

