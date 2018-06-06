FROM debian:jessie  
MAINTAINER "Sascha Marcel Schmidt" <docker@saschaschmidt.net>  
  
RUN apt-get update && \  
apt-get install --no-install-recommends -y \  
openssl && \  
rm -r /var/lib/apt/lists/*  
  
COPY bin/ /usr/local/lib/ssl/  
COPY template/ /usr/local/etc/ssl/template/  
RUN chmod +x -R /usr/local/lib/ssl/  
  
VOLUME ["/usr/local/share/ca-certificates/certs/", "/usr/local/share/ca-
certificates/ca/"]  
ENTRYPOINT ["/usr/local/lib/ssl/entrypoint.sh"]  

