FROM debian:jessie  
MAINTAINER Philipp Holler <philipp.holler93@gmail.com>  
  
ENV SEAFILE_VERSION="6.0.7" \  
SEAFILE_INSTALLDIR="/opt/seafile" \  
SEAFILE_SERVERINSTALLDIR="/opt/seafile/seafile-server" \  
SEAFILE_CONFDIR="/opt/seafile/conf" \  
SEAFILE_CCNET_CONFDIR="/opt/seafile/ccnet" \  
SEAFILE_DATADIR="/opt/seafile/seafile-data" \  
SEAFILE_SEAHUB_DATADIR="/opt/seafile/seahub-data" \  
SUPERVISORD_CONFDIR="/etc/supervisor/conf.d"  
RUN useradd -r seafile \  
&& ulimit -n 30000  
  
RUN apt-get update \  
&& apt-get install -y python2.7 libpython2.7 python-setuptools python-imaging
python-ldap python-mysqldb python-memcache curl mysql-client supervisor \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p ${SEAFILE_SERVERINSTALLDIR} \  
&& curl -Lk http://bintray.com/artifact/download/seafile-org/seafile/seafile-
server_${SEAFILE_VERSION}_x86-64.tar.gz | tar xzf - --strip-components=1 -C
${SEAFILE_SERVERINSTALLDIR}  
  
RUN mkdir -p ${SUPERVISORD_CONFDIR}  
COPY supervisord-config/* ${SUPERVISORD_CONFDIR}/  
RUN chmod +x ${SUPERVISORD_CONFDIR}/shutdownhandler.sh  
  
COPY seafile_entrypoint.sh /  
RUN chmod +x seafile_entrypoint.sh  
ENTRYPOINT ["/seafile_entrypoint.sh"]  
  
VOLUME ${SEAFILE_CONFDIR} ${SEAFILE_DATADIR} ${SEAFILE_SEAHUB_DATADIR}  
EXPOSE 10001 12001 8000 8080 8082  

