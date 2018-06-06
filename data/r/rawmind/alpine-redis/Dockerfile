FROM rawmind/alpine-base:0.3.3-2  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
# Install redis  
RUN apk add --update redis && \  
rm -rf /var/cache/apk/* && \  
mkdir /data && \  
chown -R redis:redis /data && \  
echo -e "include /etc/redis-local.conf\n" >> /etc/redis.conf  
  
# Add the files  
ADD root /  
  
# Expose the ports for redis  
EXPOSE 6379  
ENTRYPOINT ["redis-server","/etc/redis.conf"]  

