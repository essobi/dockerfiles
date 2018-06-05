# vim:set ft=dockerfile:  
# Base on VRT Base image  
FROM vrtsystems/baseimage:develop  
MAINTAINER VRT Engineering <engineering@vrt.com.au>  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r postgres && useradd -r -g postgres postgres  
  
# NOTE: If you change postgres versions here, there is also a reference  
# in supervisord.conf that needs to be updated.  
ENV PG_MAJOR 9.3  
ENV PG_VERSION 9.3.22-1.pgdg80+1  
# Location for health-check scripts  
ENV HEALTHCHK_D /usr/local/etc/docker-postgres/healthcheck.d  
  
# Location of pre- and post-start init scripts  
ENV PRESTART_INIT_D /usr/local/etc/docker-postgres/prestart-init.d  
ENV POSTSTART_INIT_D /usr/local/etc/docker-postgres/poststart-init.d  
  
# Location where post-start init status is written  
ENV POSTSTART_INIT_STATUS_FILE /tmp/postinit.txt  
  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main'
$PG_MAJOR > /etc/apt/sources.list.d/pgdg.list  
  
RUN apt-get update \  
&& apt-get install -y postgresql-common \  
&& sed -ri 's/#(create_main_cluster) .*$/\1 = false/' /etc/postgresql-
common/createcluster.conf \  
&& apt-get install -y postgresql-$PG_MAJOR=$PG_VERSION \  
&& mkdir -p ${PRESTART_INIT_D} \  
&& mkdir -p ${POSTSTART_INIT_D} \  
&& mkdir -p ${HEALTHCHK_D} \  
&& mkdir -p /var/run/postgresql \  
&& chown -R postgres /var/run/postgresql \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV PATH /usr/lib/postgresql/$PG_MAJOR/bin:$PATH  
ENV PGDATA /var/lib/postgresql/data  
VOLUME ["/var/lib/postgresql/data"]  
  
COPY docker-entrypoint.sh /usr/local/sbin/  
COPY docker-healthcheck.sh /usr/local/sbin/  
COPY supervisord-postinit.sh /usr/local/sbin/  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# PostgreSQL port  
EXPOSE 5432  
# Suggested port for XML-RPC to supervisord, if enabled.  
EXPOSE 9001  
ENTRYPOINT ["/usr/local/sbin/docker-entrypoint.sh"]  
HEALTHCHECK \--interval=15s --timeout=5s \  
CMD /usr/local/sbin/docker-healthcheck.sh  
  
CMD ["supervisor"]  

