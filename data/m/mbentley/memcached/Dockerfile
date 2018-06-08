FROM debian:jessie  
MAINTAINER Matt Bentley <mbentley@mbentley.net>  
  
RUN apt-get update && apt-get install -y memcached && rm -rf
/var/lib/apt/lists/*  
USER memcache  
EXPOSE 11211 11211/udp  
ENTRYPOINT ["memcached"]  
CMD ["-v","-m 256","-p 11211","-c 1024"]  

