FROM debian:wheezy  
MAINTAINER Konstantin Burykin <burkostya@gmail.com>  
  
ENV POLIPO_VERSION 1.1.1-2  
RUN echo "deb http://http.us.debian.org/debian testing main non-free contrib"
\  
>> /etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y polipo="$POLIPO_VERSION" && \  
apt-get clean  
  
ADD polipo.conf /etc/polipo/config  
  
EXPOSE 3111  
ADD init /app/init  
RUN chmod 755 /app/init  
  
VOLUME ["/var/cache/polipo"]  
  
ENTRYPOINT ["/app/init"]  
CMD ["app:start"]  

