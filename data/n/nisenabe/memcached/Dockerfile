FROM debian  
MAINTAINER nise_nabe <nise.nabe@gmail.com>  
  
RUN apt-get install -y --force-yes memcached  
RUN sed -i "s/^\\-l 127\\.0\\.0\\.1/#-l 127.0.0.1/" /etc/memcached.conf  
  
USER daemon  
EXPOSE 11211  
  
CMD memcached  

