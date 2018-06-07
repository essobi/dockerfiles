FROM phusion/baseimage:0.9.18  
# https://github.com/sameersbn/docker-ubuntu/blob/master/Dockerfile  
RUN echo 'APT::Install-Recommends 0;' >> /etc/apt/apt.conf.d/01norecommends \  
&& echo 'APT::Install-Suggests 0;' >> /etc/apt/apt.conf.d/01norecommends \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y vim.tiny wget sudo net-
tools ca-certificates unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
# https://github.com/sameersbn/docker-postgresql/blob/master/Dockerfile  
ENV PG_VERSION=9.4 \  
PG_USER=postgres \  
PG_HOME=/var/lib/postgresql \  
PG_RUNDIR=/run/postgresql \  
PG_LOGDIR=/var/log/postgresql  
  
ENV PG_CONFDIR="/etc/postgresql/${PG_VERSION}/main" \  
PG_BINDIR="/usr/lib/postgresql/${PG_VERSION}/bin" \  
PG_DATADIR="${PG_HOME}/${PG_VERSION}/main"  
# also RELEASE_TAG could be set for static import  
ENV DB_USER="musicbrainz" \  
DB_PASS="musicbrainz" \  
DB_UNACCENT=true \  
REPLICATION_USER=repluser \  
REPLICATION_PASS="set_this_password_in_docker_compose"  
# mbslave revision  
ENV MBSLAVE_REV=b36a1c6  
  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
apt-key add - \  
&& echo 'deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main' >
/etc/apt/sources.list.d/pgdg.list \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y postgresql-${PG_VERSION}
postgresql-client-${PG_VERSION} postgresql-contrib-${PG_VERSION} \  
&& rm -rf ${PG_HOME} \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR ${PG_HOME}  
  
# install dependencies  
RUN apt-get update && apt-get install -y python python-psycopg2 git  
  
# add crontab with script to replicate  
ADD crontab /etc/crontab  
  
# https://github.com/phusion/baseimage-docker/issues/115  
RUN chmod 600 /etc/crontab  
  
# run postgres on init as daemon (see emtrypoint end script)  
COPY entrypoint.sh /etc/my_init.d/entrypoint.sh  
RUN chmod 755 /etc/my_init.d/entrypoint.sh  
  
# make sure this dir exists  
RUN mkdir -p /dumps  
  
# make sure the postgres user can run the scripts  
ADD ./volume ${PG_HOME}  
  
# get mbslave scripts  
RUN git clone https://bitbucket.org/lalinsky/mbslave.git ./mbslave2 && \  
cd ./mbslave2 && git reset --hard ${MBSLAVE_REV}  
  
# jelastic complains about the run path  
#VOLUME ["${PG_HOME}", "${PG_RUNDIR}"]  
VOLUME ["${PG_HOME}", "/dumps"]  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init", "./make_as_postgres"]  
  
EXPOSE 5432/tcp

