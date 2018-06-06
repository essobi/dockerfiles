# tcloud/redis-commander  
# VERSION 0.1  
FROM tcloud/nodejs:latest  
MAINTAINER tcloud  
  
USER root  
  
RUN npm install -g redis-commander  
  
VOLUME /data  
  
EXPOSE 5202  
# We use the "sh -c" to turn around
https://github.com/docker/docker/issues/5509 - variable not expanded  
ENTRYPOINT ["sh", "-c"]  
  
CMD ["redis-commander --redis-host localhost --redis-port 6379 --port 5202"]

