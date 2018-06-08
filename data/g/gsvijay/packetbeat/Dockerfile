FROM debian:jessie-slim  
  
MAINTAINER gsvijay  
  
RUN apt-get update \  
&& apt-get install -y libpcap0.8 curl \  
&& curl -L -O
https://artifacts.elastic.co/downloads/beats/packetbeat/packetbeat-5.1.1-amd64.deb
\  
&& dpkg -i packetbeat-5.1.1-amd64.deb  
  
COPY entrypoint.sh /  
  
CMD ["/bin/sh","entrypoint.sh"]  

