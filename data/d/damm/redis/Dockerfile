FROM damm/ubuntu:14.04  
MAINTAINER <scott@likens.us>  
RUN apt-get update  
RUN apt-get install wget -y  
RUN apt-get install build-essential -y  
ENV VERSION 3.0.2  
RUN wget http://download.redis.io/releases/redis-${VERSION}.tar.gz -O
/tmp/redis-${VERSION}.tar.gz && cd /tmp;tar zxf redis-${VERSION}.tar.gz  
RUN cd /tmp/redis-${VERSION};make && make install  
RUN mkdir /etc/redis && mkdir -p /data/  
ADD redis.conf /etc/redis/redis.conf  
ADD run /run.sh  
RUN chmod +x /run.sh  
RUN useradd -m redis  
EXPOSE 6379  
ENTRYPOINT ["/run.sh"]  

