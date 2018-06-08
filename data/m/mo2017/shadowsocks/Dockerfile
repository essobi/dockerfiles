FROM alpine:3.4  
MAINTAINER "Cloth Mo" <root@buxiaomo.com>  
  
ENV PASS **NULL**  
  
COPY repositories /etc/apk/repositories  
  
RUN apk add --no-cache curl py-pip python curl python-dev pwgen \  
&& pip install shadowsocks setuptools \  
&& mkdir /etc/shadowsocks  
  
COPY Start /Start  
  
EXPOSE 8388  
CMD ["sh","/Start"]  

