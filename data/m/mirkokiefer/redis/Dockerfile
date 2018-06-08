  
FROM mirkokiefer/ubuntu-base  
  
RUN echo deb http://archive.ubuntu.com/ubuntu precise main universe >
/etc/apt/sources.list  
RUN echo deb http://archive.ubuntu.com/ubuntu precise-updates main universe >>
/etc/apt/sources.list  
RUN apt-get update  
  
RUN apt-get install -y build-essential tcl  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl http://download.redis.io/releases/redis-2.8.5.tar.gz >
redis-2.8.5.tar.gz  
  
RUN tar xzf redis-2.8.5.tar.gz  
  
RUN mv redis-2.8.5 /redis  
RUN cd /redis && make  
  
RUN cd /redis/src && \  
cp redis-server /usr/local/bin/ && \  
cp redis-cli /usr/local/bin/  
  
EXPOSE 6379  
CMD ["redis-server"]  

