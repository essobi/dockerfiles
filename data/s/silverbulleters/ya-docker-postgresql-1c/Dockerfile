FROM sameersbn/ubuntu:14.04.20170123  
LABEL maintainer.base="sameer@damagehead.com" \  
maintainer.current="team@silverbulleters.org"  
ENV DEBIAN_FRONTEND=noninteractive  
  
ENV PG_APP_HOME="/etc/docker-postgresql"\  
PG_VERSION=9.6 \  
PG_USER=postgres \  
PG_HOME=/var/lib/postgresql \  
PG_RUNDIR=/run/postgresql \  
PG_LOGDIR=/var/log/postgresql \  
PG_CERTDIR=/etc/postgresql/certs  
  
ENV PG_BINDIR=/usr/lib/postgresql/${PG_VERSION}/bin \  
PG_DATADIR=${PG_HOME}/${PG_VERSION}/main \  
PG_WAL=${PG_HOME}/pg_xlog \  
PG_TEMPTBLSPC=${PG_HOME}/temptblspc \  
PG_V81C_DATA=${PG_HOME}/v81c_data \  
PG_V81C_INDEX=${PG_HOME}/v81c_index  
  
RUN apt-get update && apt-get install -y locales \  
&& localedef -i ru_RU -c -f UTF-8 -A /usr/share/locale/locale.alias
ru_RU.UTF-8 \  
&& update-locale LANG=ru_RU.UTF-8  
#TODO add en_US locale  
ENV LANG ru_RU.UTF-8  
ENV LC_MESSAGES "POSIX"  
ADD tools/postgrepinning /etc/apt/preferences.d/postgres  
  
RUN wget --quiet -O - http://1c.postgrespro.ru/keys/GPG-KEY-POSTGRESPRO-1C |
apt-key add - \  
&& echo 'deb http://1c.postgrespro.ru/deb/ trusty main' >
/etc/apt/sources.list.d/postgrespro-1c.list \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y curl acl \  
postgresql-pro-1c-${PG_VERSION} postgresql-client-pro-1c-${PG_VERSION}
postgresql-contrib-pro-1c-${PG_VERSION} \  
&& ln -sf ${PG_DATADIR}/postgresql.conf
/etc/postgresql/${PG_VERSION}/main/postgresql.conf \  
&& ln -sf ${PG_DATADIR}/pg_hba.conf
/etc/postgresql/${PG_VERSION}/main/pg_hba.conf \  
&& ln -sf ${PG_DATADIR}/pg_ident.conf
/etc/postgresql/${PG_VERSION}/main/pg_ident.conf  
  
WORKDIR /tmp  
  
RUN curl -s
https://packagecloud.io/install/repositories/postgrespro/mamonsu/script.deb.sh
| bash  
RUN apt-get install mamonsu -y  
  
WORKDIR /usr/local/src  
  
RUN apt-get update && apt-get install -y \  
gcc \  
jq \  
make \  
postgresql-contrib-pro-1c-${PG_VERSION} \  
postgresql-server-dev-pro-1c-${PG_VERSION} \  
postgresql-plpython-pro-1c-${PG_VERSION} \  
&& wget -O- $(wget -O- https://api.github.com/repos/powa-team/powa-
archivist/releases/latest|jq -r '.tarball_url') | tar -xzf - \  
&& wget -O- $(wget -O- https://api.github.com/repos/powa-
team/pg_qualstats/releases/latest|jq -r '.tarball_url') | tar -xzf - \  
&& wget -O- $(wget -O- https://api.github.com/repos/powa-
team/pg_stat_kcache/releases/latest|jq -r '.tarball_url') | tar -xzf - \  
&& wget -O- $(wget -O-
https://api.github.com/repos/hypopg/hypopg/releases/latest|jq -r
'.tarball_url') | tar -xzf - \  
&& wget -O- $(wget -O-
https://api.github.com/repos/rjuju/pg_track_settings/releases/latest|jq -r
'.tarball_url') | tar -xzf - \  
&& wget -O- $(wget -O- https://api.github.com/repos/reorg/pg_repack/tags|jq -r
'.[0].tarball_url') | tar -xzf - \  
&& for f in $(ls); do cd $f; make install; cd ..; rm -rf $f; done \  
&& apt-get purge -y --auto-remove curl gcc jq make postgresql-server-dev-
pro-1c-${PG_VERSION} wget  
  
RUN rm -rf ${PG_HOME} \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY runtime/ ${PG_APP_HOME}/  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
EXPOSE 5432/tcp  
VOLUME ["${PG_HOME}", "${PG_RUNDIR}", "${PG_LOGDIR}", "${PG_DATADIR}"]  
VOLUME ["${PG_TEMPTBLSPC}", "${PG_V81C_DATA}", "${PG_V81C_INDEX}"]  
WORKDIR ${PG_HOME}  
ENTRYPOINT ["/sbin/entrypoint.sh"]  

