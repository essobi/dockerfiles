FROM redis:3.2  
RUN apt-get update  
RUN apt-get install -y ruby vim wget redis-tools  
RUN gem install redis  
RUN cd / && wget http://download.redis.io/redis-stable/src/redis-trib.rb &&
chmod 755 redis-trib.rb  
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint.sh"]

