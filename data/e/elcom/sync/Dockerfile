FROM debian:stretch  
MAINTAINER LWB  
  
ENV TARGET_USER=ADMIN \  
TARGET_PASSWORD=ADMIN \  
TARGET_PATH=/ \  
TARGET_PATH_LOG=/ \  
SOURCE_HOST=/ \  
SOURCE_USER=ADMIN \  
SOURCE_PATH=/ \  
LOG_SERVER=127.0.0.1 \  
LOG_PORT=3000 \  
LOG_PROJECT=sync  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get install -y --force-yes --no-install-recommends ssh rsync cifs-utils &&
\  
rm -rf /var/lib/apt/lists  
  
RUN mkdir -p /root/ssh  
  
VOLUME /root/ssh  
  
USER root  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
CMD ["docker-entrypoint.sh"]  

