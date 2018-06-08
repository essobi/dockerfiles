#  
# Build it:  
# sudo docker build -t skxskx/memcached .  
#  
# Then launch it:  
# sudo docker run -d -p 11211:11211 skxskx/memcached  
#  
FROM ubuntu  
MAINTAINER steve@steve.org.uk  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
RUN apt-get install --yes --force-yes memcached  
RUN sed -i "/127.0.0.1/d" /etc/memcached.conf  
EXPOSE 11211  
CMD ["/usr/bin/memcached","-u","memcache"]  

