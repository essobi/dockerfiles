FROM wodby/nginx-alpine  
MAINTAINER Wodby <hello@wodby.com>  
  
RUN export LEGO_VER="v0.3.0" && \  
  
# Install lego  
wget -qO- https://s3.amazonaws.com/wodby-releases/lego/${LEGO_VER}/lego.tar.gz
| tar xz -C /tmp/ && \  
mkdir -p /opt/wodby/bin && \  
mv /tmp/lego /opt/wodby/bin  
  
COPY rootfs /  

