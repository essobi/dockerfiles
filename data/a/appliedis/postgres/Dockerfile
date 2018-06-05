FROM appliedis/centos-gosu:7  
MAINTAINER Jonathan Meyer <jon@gisjedi.com>  
  
# explicitly set user/group IDs and fix locale for UTF-8 default in postgres  
RUN groupadd -r postgres --gid=995 && useradd -r -g postgres --uid=995
postgres \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
  
ENV LANG en_US.utf8  
ENV PG_MAJOR 9.5  
ENV PG_MAJOR_SQUASH 95  
RUN mkdir /docker-entrypoint-initdb.d  
  
RUN yum install -y \  
http://yum.postgresql.org/$PG_MAJOR/redhat/rhel-7-x86_64/pgdg-
centos$PG_MAJOR_SQUASH-$PG_MAJOR-2.noarch.rpm \  
&& yum install -y \  
postgresql$PG_MAJOR_SQUASH-server \  
postgresql$PG_MAJOR_SQUASH-contrib \  
&& yum clean all  
  
RUN mkdir -p /var/run/postgresql && chown -R postgres /var/run/postgresql  
  
ENV PATH /usr/pgsql-$PG_MAJOR/bin:$PATH  
ENV PGDATA /var/lib/postgresql/data  
VOLUME /var/lib/postgresql/data  
  
COPY docker-entrypoint.sh /  
COPY pgtune.py /docker-entrypoint-initdb.d/  
  
RUN chmod +x /docker-entrypoint.sh  
  
# Environment variables that can be specified to override setting defaults:  
#INSTANCE_MEMORY: amount of memory allocated for the PostGres instance use in
MBs  
#CONNECTIONS: number of connections allowed concurrently  
#FORCE_PGTUNE: true or false, indicating whether PostGres should be tuned on
startup, regardless of existing config  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 5432  
CMD ["postgres"]  

