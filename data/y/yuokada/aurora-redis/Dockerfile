# FROM redis:4.0.2  
# Pull base image.  
FROM ubuntu:16.04  
# Install Redis.  
RUN apt-get update && apt-get install -y redis-server  
ADD redis_elector.py /usr/local/bin/redis_elector.py  
RUN chmod +x /usr/local/bin/redis_elector.py  
RUN sed -i 's/^\\(bind .*\\)$/# \1/' /etc/redis/redis.conf && \  
sed -i 's/^\\(daemonize .*\\)$/# \1/' /etc/redis/redis.conf && \  
sed -i 's/^\\(dir .*\\)$/# \1\ndir \/data/' /etc/redis/redis.conf && \  
sed -i 's/^\\(logfile .*\\)$/# \1/' /etc/redis/redis.conf  
# ADD redis.conf /etc/redis/redis.conf  
# Expose ports.  
EXPOSE 6379  
# Define mountable directories.  
VOLUME ["/data"]  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["redis-server", "/etc/redis/redis.conf"]  

