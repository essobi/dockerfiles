FROM redis:latest  
  
RUN apt-get -y update && \  
apt-get install -y --no-install-recommends --no-install-suggests ruby
supervisor rubygems && \  
rm -rf /var/lib/apt/lists/* && \  
gem install redis  
  
RUN wget https://raw.githubusercontent.com/antirez/redis/3.2.9/src/redis-
trib.rb -O /redis-trib.rb && \  
chmod +x /redis-trib.rb  
  
COPY start.sh /  
COPY supervisord.conf /  
COPY redis.conf /  
  
VOLUME /data  
WORKDIR /  
RUN chmod +x ./start.sh  
EXPOSE 7000 7001 7002 7003 7004 7005  
CMD ["./start.sh"]  

