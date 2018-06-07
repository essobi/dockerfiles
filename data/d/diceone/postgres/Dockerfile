FROM centos:7  
RUN groupadd -r postgres --gid=1999 && useradd -r -g postgres --uid=1999
postgres  
  
RUN curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64" \  
&& chmod +x /usr/local/bin/gosu  
  
RUN yum install -y http://yum.postgresql.org/9.3/redhat/rhel-7-x86_64/pgdg-
centos93-9.3-2.noarch.rpm \  
&& yum install -y postgresql93 postgresql93-server postgresql93-devel \  
&& yum clean all  
  
RUN mkdir /docker-entrypoint-initdb.d  
  
RUN mkdir -p /var/run/postgresql && chown -R postgres /var/run/postgresql  
  
ENV PG_MAJOR 9.3  
ENV PATH /usr/pgsql-$PG_MAJOR/bin/:$PATH  
ENV PGDATA /var/lib/pgsql/$PG_MAJOR/data/  
VOLUME /var/lib/pgsql/$PG_MAJOR/data/  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 5432  
CMD ["postgres"]  

