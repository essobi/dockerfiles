FROM ubuntu:latest  
MAINTAINER T. Schuetz <t.schuetz@itservice-schuetz.de>  
  
RUN useradd -u 1000 mumble-serv \  
&& apt-get update \  
&& apt-get upgrade \  
&& apt-get install -y mumble-server \  
&& mkdir /data && chown 1000 /data  
  
ADD mumble-server.ini /config/mumble-server.ini  
  
VOLUME ["/data", "/config"]  
EXPOSE 64738/udp  
  
USER mumble-serv  

