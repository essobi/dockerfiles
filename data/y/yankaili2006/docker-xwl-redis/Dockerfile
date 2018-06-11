FROM zokeber/redis:latest  
MAINTAINER coola58 "yankaili2006@gmail.com"  
#update system timezone  
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
#update application timezone  
RUN echo "Asia/Shanghai" >> /etc/timezone  
  
ADD redis.conf /etc/redis.conf  
  
CMD ["/usr/bin/redis-server", "/etc/redis.conf"]  

