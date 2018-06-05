FROM ubuntu  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get update  
  
# install memcached  
RUN apt-get install -y memcached  
  
# run memcached as the daemon user  
USER daemon  
  
# expose memcached port  
EXPOSE 11211  
  
# Launch memcached when launching the container  
CMD ["memcached"]  

