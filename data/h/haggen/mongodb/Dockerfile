FROM debian:jessie  
  
MAINTAINER Arthur Corenzan <arthur@corenzan.com>  
  
RUN apt-get update && apt-get install -y --no-install-recommends mongodb && rm
-rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/data/db"]  
  
EXPOSE 27017  
CMD ["mongod", "--logpath", "/dev/stdout"]  

