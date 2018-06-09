FROM debian:latest  
  
MAINTAINER Philipp Schmitt <philipp@schmitt.co>  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends stunnel && \  
rm -rf /etc/stunnel && \  
ln -s /config /etc/stunnel && \  
rm -rf /var/lib/apt/lists/*  
  
VOLUME ["/config", "/certs"]  
WORKDIR /config  
EXPOSE 443  
CMD ["stunnel"]  

