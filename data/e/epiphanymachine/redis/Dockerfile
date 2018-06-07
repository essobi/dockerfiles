# Run redis server(s) for local development  
  
# docker volume create -d local hint-redis-data  
# docker run -d \  
# \--restart always \  
# -v hint-redis-data:/data \  
# -p 6888:6379 \  
# \--name hint-redis \  
# epiphanymachine/redis  
  
# docker volume create -d local hint-redis-cache-data  
# docker run -d \  
# \--restart always \  
# -v hint-redis-cache-data:/data \  
# -p 6889:6379 \  
# \--name hint-redis-cache \  
# epiphanymachine/redis  
  
FROM ubuntu:16.04  
MAINTAINER EpiphanyMachine@gmail.com  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
redis-server  
  
EXPOSE 6379  
  
VOLUME ["/data"]  
  
CMD ["/usr/bin/redis-server"]  

