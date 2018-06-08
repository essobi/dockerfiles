FROM debian:jessie  
MAINTAINER Purpose Industries <dev@purposeindustries.co>  
RUN groupadd -r sinopia && \  
useradd -r -g sinopia sinopia && \  
mkdir -p /opt/sinopia && \  
chown -R sinopia:sinopia /opt/sinopia  
VOLUME /opt/sinopia  

