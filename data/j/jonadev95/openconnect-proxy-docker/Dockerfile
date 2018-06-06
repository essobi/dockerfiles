FROM ubuntu:16.04  
MAINTAINER sauercrowd <jonadev95@posteo.org>  
  
RUN apt-get update && apt-get install -y openconnect squid3  
ADD squid.conf /etc/squid/squid.conf  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT /entrypoint.sh  

