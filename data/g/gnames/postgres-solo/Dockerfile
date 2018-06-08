FROM postgres:9.6.2  
MAINTAINER Dmitry Mozzherin  
ENV LAST_FULL_REBUILD 2017-03-08  
RUN apt-get update \  
&& apt-get install -y gettext-base  
  
ENV MAX_CONNECTIONS 100  
ENV SHARED_BUFFERS 128MB  
ENV WORK_MEM 4MB  
ENV MAINTENANCE_WORK_MEM 64MB  
ENV WAL_BUFFERS -1  
ENV MAX_WALL_SIZE 1GB  
ENV MIN_WALL_SIZE 80MB  
ENV CHECKPOINT_COMPLETION_TARGET 0.5  
ENV EFFECTIVE_CACHE_SIZE 4GB  
ENV DEFAULT_STATISTICS_TARGET 100  
COPY bin/init.sh /docker-entrypoint-initdb.d/init.sh  
COPY bin/gn-entrypoint.sh /  
COPY config/postgresql.conf.template /  
  
EXPOSE 5432  
ENTRYPOINT ["/gn-entrypoint.sh"]  
  
CMD ["postgres"]  

