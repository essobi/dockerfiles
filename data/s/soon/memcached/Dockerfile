#  
# A simple memchache server  
#  
FROM debian:wheezy  
MAINTAINER SOON_ <dorks@thisissoon.com>  
  
RUN apt-get update && apt-get install --no-install-recommends -y -q \  
memcached \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 11211  
CMD ["memcached", "-u", "daemon", "-v"]  

