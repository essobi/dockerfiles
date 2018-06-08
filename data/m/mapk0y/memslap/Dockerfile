FROM debian:latest  
MAINTAINER mapk0y "mapk0y@gmail.com"  
RUN apt-get update \  
&& apt-get --no-install-recommends -y install \  
libmemcached-tools \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists  
  
ENTRYPOINT ["memcslap"]  
CMD ["--help"]  
  

