# docker.aquilainsight.com:5000/base-db  
FROM ubuntu:16.04  
MAINTAINER Andreas Lang <andreas.lang@aquilainsight.com>  
  
ENV TERM=xterm \  
ADMIN_USERNAME="admin" \  
RO_USERNAME="ro" \  
RW_USERNAME="rw" \  
ADMIN_PW="admin_pw" \  
RO_PW="ro_pw" \  
RW_PW="rw_pw" \  
PG_VERSION=9.6  
RUN apt-get update \  
&& apt-get install -y \  
language-pack-en \  
wget \  
&& update-locale LANG=en_US.UTF-8 LC_MESSAGES=POSIX \  
&& echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg main" >
/etc/apt/sources.list.d/postgres.list \  
&& wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-
key add - \  
&& apt-get update \  
&& apt-get install -y \  
postgresql-${PG_VERSION} \  
postgresql-contrib-${PG_VERSION} \  
sudo \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD *.conf /etc/postgresql/${PG_VERSION}/main/  
ADD .pgpass /root/.pgpass  
ADD .pgpass /var/lib/postgresql/.pgpass  
RUN chmod 600 /root/.pgpass \  
&& chown postgres:postgres /var/lib/postgresql/.pgpass \  
&& chmod 600 /var/lib/postgresql/.pgpass  
  
ADD database.psql /tmp/database.psql  
ADD privileges.sql /tmp/privileges.sql  
RUN service postgresql start && \  
sudo -u postgres psql -f /tmp/database.psql && \  
psql -U admin -h localhost -f /tmp/privileges.sql ai_db && \  
service postgresql stop  
  
ONBUILD ADD ddl /tmp/ddl  
ONBUILD ADD sql /tmp/sql  
ONBUILD RUN service postgresql start \  
&& find /tmp/ddl/* | sort | xargs -I {} psql -U admin -h localhost -f {} ai_db
\  
&& find /tmp/sql/* | sort | xargs -I {} psql -U admin -h localhost -f {} ai_db
\  
&& service postgresql stop \  
&& rm /tmp/ddl/* \  
&& rm /tmp/sql/*  
  
ADD run.sh /srv/run.sh  
RUN chmod u+x /srv/run.sh  
CMD ["/srv/run.sh"]

