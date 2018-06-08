FROM alpine:3.7  
LABEL maintainer="gmblar+github@gmail.com"  
  
EXPOSE 11211  
ENV MEMCACHED_MEMORY_LIMIT=64  
COPY src /  
RUN memcached-setup  
  
ENTRYPOINT ["memcached-entrypoint"]  
CMD ["memcached"]  

