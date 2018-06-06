FROM debian:jessie  
MAINTAINER dev@chialab.it  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y
memcached \  
&& apt-get purge -y --auto-remove $buildDeps \  
&& rm -r /var/lib/apt/lists/*  
  
USER memcache  
EXPOSE 11211  
CMD ["memcached"]  

