FROM alpine:3.4  
MAINTAINER ChasonTang <chasontang@gmail.com>  
  
ENV PG_MAJOR 9.5  
ENV PG_VERSION 9.5.4-r0  
ENV PGDATA /var/lib/postgresql  
  
RUN mkdir /docker-entrypoint-initdb.d \  
&& apk add --no-cache postgresql=$PG_VERSION postgresql-contrib=$PG_VERSION \  
&& sed -ri "s!^#?(listen_addresses)\s*=\s*\S+.*!\1 = '*'!"
/usr/share/postgresql/postgresql.conf.sample  
  
VOLUME /var/lib/postgresql/data  
  
COPY docker-entrypoint.sh /  
  
USER postgres  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 5432  
CMD ["postgres"]

