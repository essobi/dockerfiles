FROM outrigger/servicebase  
  
RUN yum -y update && \  
yum -y install memcached && \  
yum clean all  
  
ENV MEMCACHE_PORT 11211  
ENV MEMCACHE_MAX_MEMORY 64  
ENV MEMCACHE_SLAB_SIZE 1M  
ENV MEMCACHE_CONN 1024  
EXPOSE 11211  
CMD /usr/bin/memcached -p $MEMCACHE_PORT -c $MEMCACHE_CONN -l 0.0.0.0 -u root
-m $MEMCACHE_MAX_MEMORY -I $MEMCACHE_SLAB_SIZE  

