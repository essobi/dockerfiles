FROM ubuntu:trusty  
  
MAINTAINER support@lastbackend.com  
  
# Install redis  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv C7917B12 && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y redis-server pwgen && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Add scripts  
ADD init.sh /init.sh  
RUN chmod +x /*.sh  
  
ENV REDIS_DIR /data  
  
VOLUME ["/data"]  
  
EXPOSE 6379  
CMD ["/init.sh"]

