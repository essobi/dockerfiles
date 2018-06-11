FROM debian:jessie  
  
LABEL \  
voxbox.io.build-date=${BUILD_DATE} \  
voxbox.io.name=postgresql \  
voxbox.io.vendor=voxbox.io \  
maintainer=matteo@voxbox.io \  
voxbox.io.vcs-url=https://github.com/matteolc/voxbox-postgresql.git \  
voxbox.io.vcs-ref=${VCS_REF} \  
voxbox.io.license=MIT  
  
ARG PG_VERSION  
ARG PG_USER  
ARG PG_HOME  
ARG PG_RUNDIR  
ARG PG_LOGDIR  
ARG PG_CERTDIR  
  
ENV PG_APP_HOME=/etc/docker-postgresql \  
PG_VERSION=${PG_VERSION:-9.6} \  
PG_USER=${PG_USER:-postgres} \  
PG_HOME=${PG_HOME:-/var/lib/postgresql} \  
PG_RUNDIR=${PG_RUNDIR:-/run/postgresql} \  
PG_LOGDIR=${PG_LOGDIR:-/var/log/postgresql} \  
PG_CERTDIR=${PG_CERTDIR:-/etc/postgresql/certs}  
  
ENV PG_BINDIR=/usr/lib/postgresql/${PG_VERSION}/bin \  
PG_DATADIR=${PG_HOME}/${PG_VERSION}/main  
  
RUN apt-get update && \  
apt-get install -y wget sudo && \  
echo 'deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main' >>
/etc/apt/sources.list.d/pgdg.list && \  
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key
add - && \  
apt-get update && \  
apt-get install -y postgresql-${PG_VERSION} && \  
ln -sf ${PG_DATADIR}/postgresql.conf
/etc/postgresql/${PG_VERSION}/main/postgresql.conf && \  
ln -sf ${PG_DATADIR}/pg_hba.conf
/etc/postgresql/${PG_VERSION}/main/pg_hba.conf && \  
ln -sf ${PG_DATADIR}/pg_ident.conf
/etc/postgresql/${PG_VERSION}/main/pg_ident.conf && \  
rm -rf ${PG_HOME}  
  
COPY runtime/ ${PG_APP_HOME}/  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
EXPOSE 5432/tcp  
VOLUME ["${PG_HOME}", "${PG_RUNDIR}"]  
WORKDIR ${PG_HOME}  
ENTRYPOINT ["/sbin/entrypoint.sh"]  

