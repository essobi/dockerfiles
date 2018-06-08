FROM alpine  
MAINTAINER littleqz@gmail.com  
LABEL description="A lightweight redis image based on alpine linux."  
  
ENV TERM xterm  
  
RUN apk update && apk add redis  
  
ADD ./redis.conf /etc/  
  
WORKDIR /data/redis  
EXPOSE 6379  
CMD ["redis-server"]  

