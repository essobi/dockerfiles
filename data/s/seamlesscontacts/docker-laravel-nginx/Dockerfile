FROM debian:jessie  
  
MAINTAINER "Granville Schmidt" <granville.schmidt@yahoo.com>  
  
WORKDIR /tmp  
  
# Install Nginx  
RUN apt-get update -y && \  
apt-get install -y nginx ruby && \  
gem install tiller  
  
COPY config/tiller /tmp/tiller  
  
# Copy over self signed SSL for dev environment  
COPY config/ssl/server.crt /etc/ssl/certs/ssl-cert.crt  
COPY config/ssl/server.key /etc/ssl/private/ssl-cert.key  
  
# Nginx startup script  
COPY config/nginx-start.sh /opt/bin/nginx-start.sh  
RUN chmod u=rwx /opt/bin/nginx-start.sh  
  
RUN mkdir -p /data /data/logs  
RUN touch /data/logs/access.log  
VOLUME ["/data"]  
  
# PORTS  
EXPOSE 80  
EXPOSE 443  
WORKDIR /opt/bin  
ENTRYPOINT ["/opt/bin/nginx-start.sh"]  

