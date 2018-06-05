FROM base  
MAINTAINER Arcus "http://arcus.io"  
RUN apt-get update  
RUN apt-get install -y make gcc wget  
RUN wget http://redis.googlecode.com/files/redis-2.6.14.tar.gz -O
/tmp/redis.tar.gz  
RUN (cd /tmp && tar zxf redis.tar.gz && cd redis-* && make install && cp
redis.conf sentinel.conf /etc/)  
RUN rm -rf /tmp/*  
EXPOSE 6379  
ENTRYPOINT ["/usr/local/bin/redis-server"]  
CMD ["/etc/redis.conf"]  

