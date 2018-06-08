FROM debian:jessie  
MAINTAINER toughiq@gmail.com  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y rinetd \  
&& apt-get clean \  
&& rm -rf /var/lib/cache/apt/lists/*  
  
# Listen on all addresses  
ENV SRC=0.0.0.0  
# Typically used for webservers, so we use port 80 as default  
ENV SRCPORT=80  
# Swarm service name. Override via ENV at startup  
ENV DEST=myservice  
# Portnumber/portname of service. Eg. 80(www), 6379(redis), 3306(mysql)  
ENV DESTPORT=myserviceport  
  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["rinetd"]  

