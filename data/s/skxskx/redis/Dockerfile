#  
# Build it:  
# sudo docker build -t skxskx/redis .  
#  
# Then launch it:  
# sudo docker run -d -p 11211:11211 skxskx/redis  
#  
# NOTE: There is no local-storage setup.  
#  
FROM ubuntu  
MAINTAINER steve@steve.org.uk  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
RUN apt-get install --yes --force-yes redis-server  
RUN sed -i "/bind 127.0.0.1/d" /etc/redis/redis.conf  
RUN perl -pi -e "s/daemonize yes/daemonize no/g" /etc/redis/redis.conf  
EXPOSE 6379  
CMD /usr/bin/redis-server /etc/redis/redis.conf  

