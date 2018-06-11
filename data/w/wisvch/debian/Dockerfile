FROM debian:jessie  
  
ENV DEBIAN_FRONTEND="noninteractive"  
RUN apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get install -y --no-install-recommends curl ca-certificates && \  
rm -rf /var/lib/apt/lists/*  
RUN curl -so /usr/local/share/ca-certificates/wisvch.crt
https://ch.tudelft.nl/certs/wisvch.crt && \  
chmod 644 /usr/local/share/ca-certificates/wisvch.crt && \  
update-ca-certificates  

