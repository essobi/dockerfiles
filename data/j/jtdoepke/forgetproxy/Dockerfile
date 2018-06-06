FROM debian:jessie-slim  
  
ENTRYPOINT ["/root/redsocks"]  
  
RUN apt-get -q update && apt-get -qy install \  
iptables \  
redsocks \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD redsocks.conf /tmp/  
ADD redsocks /root/  

