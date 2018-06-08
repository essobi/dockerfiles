FROM centos:7  
MAINTAINER Marc Richter <mail@marc-richter.info>  
  
ENV PGDATA /var/lib/pgsql/data  
ENV PGPORT 5432  
ENV ES_HOME /usr/share/elasticsearch  
ENV ES_CONF_DIR /etc/elasticsearch  
ENV ES_CONF_FILE ${ES_CONF_DIR}/elasticsearch.yml  
ENV ES_DATA_DIR /var/lib/elasticsearch  
ENV ES_LOG_DIR /var/log/elasticsearch  
ENV ES_PID_DIR /var/run/elasticsearch  
  
# Add EPEL  
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-7-5.noarch.rpm  
  
# Add Bloonix Repo  
RUN rpm -Uvh https://download.bloonix.de/repos/centos/7/noarch/bloonix-
release-0.5-1.el7.centos.noarch.rpm  
  
# Update system  
RUN yum -y update \  
&& yum -y clean all  
  
# Install PhantomJS for check-wtrm (Simulation of end-users on the website)  
RUN yum -y install git gcc gcc-c++ make flex bison gperf ruby \  
openssl-devel freetype-devel fontconfig-devel libicu-devel sqlite-devel \  
libpng-devel libjpeg-devel \  
&& git clone \--recurse-submodules git://github.com/ariya/phantomjs.git
/usr/src/phantomjs \  
&& cd /usr/src/phantomjs \  
&& ./build.py -c \  
&& cp -f bin/phantomjs /usr/local/bin/ \  
&& cd / \  
&& rm -rf /usr/src/phantomjs \  
&& yum -y erase git gcc gcc-c++ flex bison gperf ruby \  
openssl-devel freetype-devel fontconfig-devel libicu-devel sqlite-devel \  
libpng-devel libjpeg-devel \  
cpp expat-devel glibc-devel glibc-headers kernel-headers keyutils-libs-devel \  
krb5-devel less libcom_err-devel libgnome-keyring libgomp libmpc \  
libselinux-devel libsepol-devel libstdc++-devel libverto-devel m4 mpfr pcre-
devel \  
perl-Error perl-Git rsync zlib-devel \  
&& yum -y clean all  
  
# Install Bloonix requirements  
RUN yum -y install java-1.7.0-openjdk postfix \  
&& yum -y clean all  
# Elasticsearch  
RUN rpm --import https://packages.elastic.co/GPG-KEY-elasticsearch  
ADD files/elasticsearch.repo /etc/yum.repos.d/elasticsearch.repo  
RUN yum -y install elasticsearch \  
&& yum -y clean all  
# PostgreSQL  
RUN yum -y install postgresql-server \  
&& yum -y clean all \  
&& su -c "initdb -D ${PGDATA} -E UTF8 -U postgres" postgres \  
&& sed -i'' "s/^#listen_addresses.*$/listen_addresses = '0.0.0.0'/g"
${PGDATA}/postgresql.conf \  
&& sed -i'' "s/^\\(host.*all.*all.*127\\.0\\.0\\.1.*\\)trust$/\1 md5/g"
${PGDATA}/pg_hba.conf \  
&& sed -i'' "s/^\\(host.*all.*all.*::1.*\\)trust$/\1 md5/g"
${PGDATA}/pg_hba.conf  
# nginx  
RUN yum -y install nginx \  
&& yum -y clean all  
ADD files/nginx/nginx.conf /etc/nginx/nginx.conf  
ADD files/nginx/01_bloonix_http.conf /etc/nginx/conf.d/01_bloonix_http.conf  
  
# Install Bloonix-webgui  
RUN /usr/bin/postgresql-check-db-dir ${PGDATA} \  
&& su -c "/usr/bin/pg_ctl start -D ${PGDATA} -s -o \"-p ${PGPORT}\" -w -t 300"
postgres \  
&& yum -y install bloonix-webgui \  
&& yum -y clean all \  
&& su --preserve-environment -s /bin/bash -c
"/usr/share/elasticsearch/bin/elasticsearch -d \  
-Des.pidfile=$ES_PID_DIR/elasticsearch.pid \  
-Des.default.path.home=$ES_HOME \  
-Des.default.path.logs=$ES_LOG_DIR \  
-Des.default.path.data=$ES_DATA_DIR \  
-Des.default.config=$ES_CONF_FILE \  
-Des.default.path.conf=$ES_CONF_DIR" elasticsearch \  
&& while [ -z "$(tail -n 5 /var/log/elasticsearch/elasticsearch.log | egrep
"$(date +%Y-%m-%d).*INFO.*node.*started$")" ]; do \  
sleep 1; \  
((count++)); \  
if [ $count -gt 180 ]; then exit 1 ; fi ; \  
done \  
&& /srv/bloonix/webgui/schema/init-elasticsearch localhost:9200 \  
&& kill $(grep ', pid' /var/log/elasticsearch/elasticsearch.log | tail -n 1 |
sed 's#^.*, pid.\\([0-9]*\\)., .*$#\1#g') \  
&& /srv/bloonix/webgui/schema/init-database --postgres \  
&& su -c "/usr/bin/pg_ctl stop -D ${PGDATA} -s -m smart -w -t 300" postgres  
  
# Install Bloonix-server  
RUN yum -y install bloonix-server \  
&& yum -y clean all  
ADD files/bloonix/bloonix-server_main.conf /etc/bloonix/server/main.conf  
ADD files/bloonix/bloonix-srvchk_main.conf
/etc/bloonix/srvchk/main.conf.template  
ADD files/bloonix/bloonix-agent_main.conf
/etc/bloonix/agent/main.conf.template  
RUN rm -f /etc/bloonix/agent/main.conf /etc/bloonix/srvchk/main.conf  
  
# Install Bloonix-plugins  
RUN su -c "/usr/bin/pg_ctl start -D ${PGDATA} -s -o \"-p ${PGPORT}\" -w -t
300" postgres \  
&& yum -y install bloonix-plugins-apache bloonix-plugins-basic bloonix-
plugins-drbd bloonix-plugins-lighttpd \  
bloonix-plugins-linux bloonix-plugins-memcached bloonix-plugins-mysql bloonix-
plugins-nginx bloonix-plugins-pgsql \  
bloonix-plugins-postfix bloonix-plugins-redis bloonix-plugins-sensors bloonix-
plugins-varnish bloonix-plugins-wtrm \  
bloonix-plugin-config \  
&& yum -y clean all \  
&& su -c "/usr/bin/pg_ctl stop -D ${PGDATA} -s -m smart -w -t 300" postgres  
  
# Install Bloonix agent  
RUN yum -y install bloonix-agent \  
&& yum -y clean all  
  
# Install Bloonix-WTRM  
RUN yum -y install bloonix-wtrm \  
&& yum -y clean all  
  
# Set permissions  
RUN chmod g+w -R /etc/bloonix  
RUN chmod +s $(which ping)  
  
# Install monit  
RUN yum -y install monit \  
&& yum -y clean all \  
&& mkdir -p /var/monit/events \  
&& mkdir -p /etc/monit.d \  
&& mkdir -p /var/log/monit  
ADD files/monit/monitrc /etc/monitrc  
ADD files/monit/monit_main.template /etc/monit.d/00_monit_main.conf  
ADD files/monit/monit_bloonix.conf /etc/monit.d/01_monit_bloonix.conf  
RUN if [ ! -e /var/monit/events ]; then mkdir -p /var/monit/events; fi  
RUN if [ ! -e /etc/monit.d ]; then mkdir -p /etc/monit.d; fi  
RUN chmod 600 /etc/monitrc /etc/monit.d/00_monit_main.conf
/etc/monit.d/01_monit_bloonix.conf \  
&& chmod 700 /etc/monit.d /var/monit/events  
  
ADD files/init.sh /init  
ADD files/bloonix/bloonix-pre-checks.sh /etc/bloonix/bloonix-pre-checks.sh  
ADD files/elasticsearch.sh /usr/local/bin/elasticsearch.sh  
RUN chmod +x /init /etc/bloonix/bloonix-pre-checks.sh
/usr/local/bin/elasticsearch.sh  
  
VOLUME /var/log  
VOLUME $ES_DATA_DIR  
VOLUME $PGDATA  
VOLUME /etc/bloonix  
  
EXPOSE 443  
EXPOSE 80  
EXPOSE 2812  
EXPOSE 5460  
CMD /init  

