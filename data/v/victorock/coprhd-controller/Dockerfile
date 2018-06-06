# VERSION 0.2  
#  
# Build CoprHD-Controller  
FROM victorock/coprhd-base:latest  
MAINTAINER "Victor da Costa" <victorockeiro@gmail.com>  
  
## ENV Variables  
ENV IP 172.17.0.2  
ENV NETMASK 255.255.0.0  
ENV GATEWAY 172.17.0.1  
ENV VIP 172.17.0.2  
ENV HOSTNAME vipr1  
ENV COUNT 1  
## Add Scripts  
COPY scripts /scripts  
  
## Build && Install  
RUN chmod +x /scripts/* && \  
/scripts/build && \  
/scripts/install  
  
#RUN rm -rf coprhd-controller  
VOLUME /data  

