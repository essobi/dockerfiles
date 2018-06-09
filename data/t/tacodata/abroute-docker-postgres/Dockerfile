#  
# this container simply runs postgres sql, it expects the volumes  
# to be mounted. the volumes come from the abroute-docker-db  
# container.  
#  
FROM tacodata/abroute-docker-db  
  
MAINTAINER Greg Fausak <greg@tacodata.com>  
  
COPY absql /usr/local/bin/  
  
EXPOSE 5432  
VOLUME ["/var/lib/postgresql"]  
VOLUME ["/etc/postgresql"]  
VOLUME ["/run/postgresql"]  
  
ENTRYPOINT ["absql"]  

