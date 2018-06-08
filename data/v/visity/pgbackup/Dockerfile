#  
FROM postgres:9.4  
MAINTAINER https://github.com/muccg/  
  
RUN mkdir /data \  
&& chown postgres:postgres /data  
  
COPY pg_backup_rotated.sh /  
COPY docker-entrypoint.sh /  
  
USER postgres  
ENV HOME /data  
WORKDIR /data  
VOLUME /data  
  
CMD ["backup"]  

