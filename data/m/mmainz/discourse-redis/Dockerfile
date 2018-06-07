FROM ubuntu  
MAINTAINER Mario Mainz  
  
# install redis  
RUN apt-get update  
RUN apt-get install -y redis-server  
  
EXPOSE 6379  
CMD ["/usr/bin/redis-server"]  

