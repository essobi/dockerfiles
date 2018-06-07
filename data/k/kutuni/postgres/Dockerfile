FROM postgres:10.0-alpine  
  
  
# make the "en_US.UTF-8" locale so postgres will be utf-8 enabled by default  
# alpine doesn't require explicit locale-file generation  
ENV LANG en_EN.utf8  
  
# make the sample config easier to munge (and "correct by default")  
RUN sed -ri "s!^#?(listen_addresses)\s*=\s*\S+.*!\1 = '*'!"
/usr/local/share/postgresql/postgresql.conf.sample  
RUN sed -ri "s!^#?(shared_buffers)\s*=\s*\S+.*!\1 = '1024MB'!"
/usr/local/share/postgresql/postgresql.conf.sample  
  
RUN mkdir -p /var/run/postgresql && chown -R postgres:postgres
/var/run/postgresql && chmod 2777 /var/run/postgresql  
  
ENV PATH /usr/lib/postgresql/$PG_MAJOR/bin:$PATH  
ENV PGDATA /data  
RUN mkdir -p "$PGDATA" && chown -R postgres:postgres "$PGDATA" && chmod 777
"$PGDATA" # this 777 will be replaced by 700 at runtime (allows semi-arbitrary
"--user" values)  
VOLUME /var/lib/postgresql/data  
  
EXPOSE 5432  
ENV PGDATA /data  
VOLUME /data  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
COPY healthcheck.sh /  
COPY tune-os.sh /initdb.d/  
  
HEALTHCHECK CMD ["/healthcheck.sh"]  
  
CMD ["postgres"]  
  
ADD initdb.sh /  

