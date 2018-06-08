#  
# Rabbitmq Dockerfile  
# git@github.com:monsieurchico/docker-rabbitmq.git  
#  
FROM ubuntu:latest  
MAINTAINER Romain Derocle "rderocle@gmail.com"  
# prevent debian errors  
ENV DEBIAN_FRONTEND noninteractive  
  
# install  
RUN \  
apt-get install -y wget && \  
wget -qO - https://www.rabbitmq.com/rabbitmq-signing-key-public.asc | apt-key
add - && \  
echo "deb http://www.rabbitmq.com/debian/ testing main" >
/etc/apt/sources.list.d/rabbitmq.list && \  
apt-get update && \  
apt-get install -y rabbitmq-server && \  
rm -rf /var/lib/apt/lists/* && \  
echo "[rabbitmq_management]." > /etc/rabbitmq/enabled_plugins && \  
echo "[{rabbit, [{loopback_users, []}]}]." > /etc/rabbitmq/rabbitmq.config  
  
# expose ports  
EXPOSE 5672  
EXPOSE 15672  
# Define environment variables.  
ENV RABBITMQ_LOG_BASE /data/log  
ENV RABBITMQ_MNESIA_BASE /data/mnesia  
  
# volumes  
VOLUME ["/data/mnesia", "/data/log"]  
  
# add launch script  
COPY ./resources/startup.sh /startup.sh  
  
# define entrypoint  
ENTRYPOINT ["/bin/bash", "/startup.sh"]

