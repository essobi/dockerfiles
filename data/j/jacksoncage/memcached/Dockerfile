# Memcached container  
#  
# docker run -rm -i -d \  
# -p 11211 \  
# -v /etc/localtime:/etc/localtime \  
# jacksoncage/memcached  
FROM debian:jessie  
MAINTAINER Love Nyberg "love.nyberg@lovemusic.se"  
ENV REFRESHED_AT 2015-12-11  
# Update the package repository and install memcached  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y wget curl memcached  
  
# Clean image  
RUN apt-get -yqq clean && \  
apt-get -yqq purge && \  
rm -rf /tmp/* /var/tmp/* && \  
rm -rf /var/lib/apt/lists/*  
  
USER daemon  
EXPOSE 11211  
COPY start.sh /start.sh  
CMD ["bash", "start.sh"]  

