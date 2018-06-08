FROM sedsimon/supervisord:latest  
  
MAINTAINER Simon Stanlake <simon.stanlake@gmail.com>  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y redis-
server  
  
ADD redis.sv.conf /etc/supervisor/conf.d/  
  
EXPOSE 6379  
CMD ["supervisord","-c","/etc/supervisor.conf"]  
  

