# VERSION 0.1  
#  
# Installs SCALEIO 2.0  
# Packages: EMC-ScaleIO-gateway-2.0-5014.0.x86_64  
FROM victorock/scaleio2:base  
MAINTAINER "Victor da Costa" <victorockeiro@gmail.com>  
  
ENV GATEWAY_ADMIN_PASSWORD "${PASSWORD}"  
ENV SIO_GW_JAVA "/usr/lib/jvm/jre/"  
ENV MDM1 ""  
ENV MDM2 ""  
ENV MDM3 ""  
COPY config/scaleio-gateway-wd.service /etc/systemd/system/  
COPY scripts /usr/local/scripts  
RUN chmod +x /usr/local/scripts/*  
  
EXPOSE 80 443  
VOLUME /dev/shm  

