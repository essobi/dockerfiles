FROM debian:jessie  
  
RUN apt-get update \  
&& apt-get -y install tor tor-geoipdb \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY torrc /etc/tor/  
  
RUN mv /var/lib/tor / && ln -s /tor /var/lib/  
  
CMD /usr/bin/tor  

