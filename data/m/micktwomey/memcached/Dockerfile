FROM ubuntu:14.04  
MAINTAINER Michael Twomey, mick@twomeylee.name  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
memcached \  
&& apt-get autoremove \  
&& apt-get clean  
  
USER daemon  
  
EXPOSE 11211  
  
CMD ["-v"]  
ENTRYPOINT ["/usr/bin/memcached"]  

