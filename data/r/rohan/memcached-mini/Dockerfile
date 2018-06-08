FROM uggedal/alpine  
MAINTAINER Rohan Singh "rohan@washington.edu"  
RUN apk update && apk add memcached  
  
EXPOSE 11211  
  
USER daemon  
ENTRYPOINT ["memcached"]  

