FROM ashsat/redis-base-3.2.3:latest  
  
# copied from https://github.com/HVF/docker-
pub/blob/master/redis/standalone/Dockerfile  
# and then modified  
EXPOSE 6379  
VOLUME ["/data"]  
RUN sysctl vm.overcommit_memory=1  
#COPY redis.conf /usr/local/etc/redis/redis.conf  
#ENTRYPOINT ["/usr/local/bin/redis-server", "/usr/local/etc/redis/redis.conf",
"--dir", "/data", "--protected-mode", "no"]  
ENTRYPOINT ["/usr/local/bin/redis-server", "--dir", "/data", "--protected-
mode", "no"]  
  
#  
# build: docker build -t aashsat/redis-server-3.2.3 .  
# run: docker run -d -P -v ~/data/redis0:/data -name=redis0 ashsat/redis-
server-3.2.3  
#  

