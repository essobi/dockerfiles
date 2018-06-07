FROM insideo/uc-linux:hydrogen  
MAINTAINER ccondit@randomcoder.com  
  
RUN \  
opkg update && \  
opkg install locale-utils locale-data && \  
echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \  
locale-gen && \  
opkg remove locale-data && \  
export LC_ALL=en_US.UTF-8 && \  
opkg install ncurses-base runas postgresql-server && \  
opkg clean && \  
addgroup -S -g 100 postgres && \  
adduser -h /var/lib/postgresql -g "PostgreSQL user" -s /bin/sh -G postgres -S
-D -u 100 postgres && \  
mkdir -p /docker-entrypoint-initdb.d /init  
  
COPY docker-entrypoint.sh /init  
  
VOLUME /pgdata  
  
ENV PGDATA=/pgdata LC_ALL=en_US.UTF-8  
ENTRYPOINT ["/init/docker-entrypoint.sh"]  
  
EXPOSE 5432  
CMD ["postgres"]  

