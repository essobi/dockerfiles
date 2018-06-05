# Postgresql (http://www.postgresql.org/)  
FROM gliderlabs/alpine:3.1  
MAINTAINER Bodhi5, Inc. <info@bodhi5.com>  
  
RUN echo "@edge http://nl.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories  
RUN apk update  
RUN apk add curl "postgresql@edge>9.4" "postgresql-contrib@edge>9.4"  
  
RUN curl -o /usr/local/bin/gosu -sSL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64"  
RUN chmod +x /usr/local/bin/gosu  
  
ENV LANG en_US.utf8  
ENV PGDATA /var/lib/postgresql/data  
VOLUME /var/lib/postgresql/data  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 5432  
CMD ["postgres"]  
# Cofigure the database to use our data dir.  
#RUN sed -i -e"s/data_directory =.*$/data_directory = '\/data'/"
/etc/postgresql/9.3/main/postgresql.conf  
#  
## Allow connections from anywhere.  
#RUN sed -i -e"s/^#listen_addresses =.*$/listen_addresses = '*'/"
/etc/postgresql/9.3/main/postgresql.conf  
#RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf  
#  
#ADD scripts /scripts  
#RUN chmod +x /scripts/start.sh  
#RUN touch /firstrun  
#  
## Add daemon to be run by runit.  
#RUN mkdir /etc/service/postgresql  
#RUN ln -s /scripts/start.sh /etc/service/postgresql/run  
EXPOSE 5432  
# Expose our data, log, and configuration directories.  
VOLUME ["/data", "/var/log/postgresql", "/etc/postgresql"]  
  
CMD ["postgres"]  

