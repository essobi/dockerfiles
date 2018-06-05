FROM debian:jessie  
MAINTAINER Claudio Benvenuti <claudio@hardypress.com>  
  
RUN set -ex; \  
apt-get update; \  
apt-get install -y \  
curl \  
mysql-client  
  
RUN rm -rf /var/lib/apt/lists/*  
  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

