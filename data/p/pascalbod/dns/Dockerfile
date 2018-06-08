FROM pascalbod/ubuntu:14.04.1-20141221  
RUN apt-get update \  
&& apt-get install -y bind9 dnsutils \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD start /start  
RUN chmod 755 /start  
  
EXPOSE 53/udp  
  
CMD ["/start"]

