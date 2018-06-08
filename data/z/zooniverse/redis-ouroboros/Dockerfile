FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN apt-get update && apt-get -y upgrade  
  
ADD ./ /redis  
  
RUN apt-get install -y automake build-essential && \  
cd /redis && make && make install && \  
cd / && rm -rf redis && apt-get remove -y automake build-essential && \  
apt-get autoremove -y && apt-get clean  
  
WORKDIR /data  
VOLUME /data  
  
COPY redis.conf /etc/redis.conf  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 6379  
CMD [ "redis-server", "/etc/redis.conf" ]  

