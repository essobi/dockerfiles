FROM alpine:latest  
  
MAINTAINER Sergio Tejón <sergio.tejon@gmail.com>  
  
RUN apk --update add freeradius freeradius-mysql freeradius-redis bash  
  
ADD ./etc/raddb/ /etc/raddb  
  
EXPOSE 1812/udp 1813/udp  
  
ENV DB_HOST=localhost  
ENV DB_PORT=3306  
ENV DB_USER=radius  
ENV DB_PASS=radpass  
ENV DB_NAME=radius  
ENV RADIUS_KEY=testing123  
ENV REDIS_HOST=localhost  
ENV REDIS_PORT=6379  
ADD ./wait-for-it/wait-for-it.sh /usr/local/bin/wait-for-it.sh  
RUN chmod +x /usr/local/bin/wait-for-it.sh  
ADD ./start.sh /start.sh  
RUN chmod +x /start.sh  
  
CMD ["/start.sh"]  

