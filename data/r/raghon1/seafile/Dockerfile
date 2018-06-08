FROM raghon1/s3ql  
MAINTAINER Ragnar Hongset <raghon@raghon.no>  
  
# Based on the fine work of Guilhem Berna <guilhem.berna@gmail.com>  
RUN apt-get update && apt-get install -y \  
ca-certificates \  
python2.7 \  
python-setuptools \  
python-simplejson \  
python-imaging \  
sqlite3 \  
rsync \  
pwgen \  
python-memcache \  
gettext \  
mariadb-client \  
python-mysqldb  
  
RUN ulimit -n 30000  
ENV SEAFILE_VERSION 4.3.2  
RUN useradd -d /opt/seafile -m seafile  
WORKDIR /opt/seafile  
#https://bintray.com/artifact/download/seafile-org/seafile/seafile-
server_4.3.2_x86-64.tar.gz  
RUN curl -L -O https://bintray.com/artifact/download/seafile-
org/seafile/seafile-server_${SEAFILE_VERSION}_x86-64.tar.gz  
RUN tar xzf seafile-server_${SEAFILE_VERSION}_x86-64.tar.gz  
RUN rm -f seafile-server_${SEAFILE_VERSION}_x86-64.tar.gz  
RUN mkdir -p logs  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Config env variables  
ENV autostart true  
ENV autoconf true  
ENV autonginx false  
ENV fcgi false  
ENV CCNET_PORT 10001  
ENV CCNET_NAME my-seafile  
ENV SEAFILE_PORT 12001  
ENV FILESERVER_PORT 8082  
ENV EXISTING_DB false  
ENV MYSQL_HOST mysql-container  
ENV MYSQL_PORT 3306  
ENV MYSQL_USER seafileuser  
ENV SEAHUB_ADMIN_EMAIL seaadmin@sea.com  
ENV CCNET_DB_NAME ccnet-db  
ENV SEAFILE_DB_NAME seafile-db  
ENV SEAHUB_DB_NAME seahub-db  
ENV SEAHUB_PORT 8000  
ENV SEAFILE_DATA /data/seafile-data  
ENV STATIC_FILES_DIR /opt/seafile/nginx/  
  
# Email congiguration  
ENV EMAIL_AUTOCONF True  
ENV EMAIL_USE_TLS True  
ENV EMAIL_HOST 'smtp.sendgrid.net'  
ENV EMAIL_PORT '587'  
ENV EMAIL_HOST_USER 'mail-admin'  
ENV EMAIL_HOST_PASSWORD 'password'  
ENV DEFAULT_FROM_EMAIL 'noreply@foo.com'  
# Control seafile restore  
ENV restore_latest false  
ENV restore_prog true  
ENV restore_data true  
ENV restore_sql true  
  
#removing default seafile installation scripts to replace them with our own  
RUN rm seafile-server-${SEAFILE_VERSION}/check_init_admin.py  
RUN rm seafile-server-${SEAFILE_VERSION}/setup-seafile-mysql.py  
  
RUN mkdir -p /etc/my_init.d  
  
#Adding all our scripts  
COPY scripts/02_permissions /etc/my_init.d/02_permissions.sh  
COPY scripts/setup-seafile-mysql.sh /etc/my_init.d/03_setup-seafile-mysql.sh  
COPY scripts/fix_email.sh /etc/my_init.d/04_fix_email.sh  
COPY scripts/create_nginx_config.sh /etc/my_init.d/90_create_nginx_config.sh  
COPY scripts/finish.sh /etc/my_init.d/99_finish.sh  
#COPY scripts/backup.sh /etc/my_init.d/02_backup.sh  
RUN mkdir -p /usr/local/bin  
COPY scripts/s3ql_backup.sh /usr/local/bin/s3ql_backup.sh  
COPY scripts/restore.sh /etc/my_init.d/02_restore.sh  
  
COPY scripts/check_init_admin.py /opt/seafile/seafile-
server-${SEAFILE_VERSION}/check_init_admin.py  
COPY scripts/setup-seafile-mysql.py /opt/seafile/seafile-
server-${SEAFILE_VERSION}/setup-seafile-mysql.py  
  
COPY nginx.conf /root/seafile.conf  
RUN chown -R seafile:seafile /opt/seafile  
  
# Seafile daemons  
RUN mkdir /etc/service/seafile /etc/service/seahub  
COPY scripts/seafile.sh /etc/service/seafile/run  
COPY scripts/seahub.sh /etc/service/seahub/run  
COPY scripts/seafile-stop.sh /etc/service/seafile/finish  
COPY scripts/seahub-stop.sh /etc/service/seahub/finish  
  
COPY scripts/seafile.crontab /root/seafile.crontab  
  
RUN crontab /root/seafile.crontab  
  
RUN mkdir -p /opt/seafile/seahub-data/custom  
COPY scripts/custom /opt/seafile/seahub-data/custom  
RUN chown -R seafile:seafile /opt/seafile/seahub-data  
  
VOLUME /root/.s3ql /opt/seafile  
EXPOSE 10001 12001 8000 8082  
# Baseimage init process  
#ENTRYPOINT ["/sbin/my_init"]  

