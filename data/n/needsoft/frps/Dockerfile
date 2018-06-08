FROM alpine  
MAINTAINER n0trace,<n0trace@protonmail.com>  
  
WORKDIR /var/frp  
  
ADD
https://github.com/fatedier/frp/releases/download/v0.13.0/frp_0.13.0_linux_amd64.tar.gz
/var/frp/frp_0.13.0_linux_amd64.tar.gz  
RUN tar -zxf frp_0.13.0_linux_amd64.tar.gz \  
&& mv frp_0.13.0_linux_amd64/* . \  
&& rm -rf frpc* \  
&& rm -rf frp_0.13.0_linux_amd64*  
  
COPY conf/frps.ini /var/frp/conf/frps.ini  
  
VOLUME /var/frp/conf  
  
EXPOSE 80 443 7000 7500  
CMD ./frps -c ./conf/frps.ini  

