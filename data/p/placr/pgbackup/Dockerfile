#  
FROM postgres:9.3  
MAINTAINER https://github.com/muccg/  
  
RUN mkdir /data \  
&& chown postgres:postgres /data  
  
COPY pg_backup_rotated.sh /  
COPY docker-entrypoint.sh /usr/local/bin/  
  
USER postgres  
ENV HOME /data  
WORKDIR /data  
VOLUME /data  
  
CMD ["backup"]  

