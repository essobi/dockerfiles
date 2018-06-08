FROM raghon1/s3ql  
MAINTAINER Ragnar Hongset <raghon@raghon.no>  
  
  
RUN apt-get update && apt-get install -y \  
sqlite3 \  
rsync \  
unzip \  
libapache2-mod-php5 libapache2-mod-perl2 \  
php5 php5-cli php5-common php5-curl php5-dev php5-gd php5-imap php5-ldap \  
php5-mhash php5-mysql php5-odbc curl libwww-perl imagemagick \  
nginx \  
pwgen  
  
RUN ulimit -n 30000  
ENV SUITECRM_VERSION 7.2  
ENV user suitecrm  
ENV group suitecrm  
  
RUN useradd -d /opt/${user} -m suitecrm  
WORKDIR /opt/suitecrm  
RUN curl -k -L -o suitecrm.zip
"https://suitecrm.com/component/dropfiles/?task=frontfile.download&id=35"  
RUN unzip -q suitecrm.zip -d /var/www/  
RUN ln -s /var/www/suitecrm-* /var/www/suitecrm-latest  
RUN rm -f suitecrm.zip  
  
# Config env variables  
ENV autostart true  
ENV autoconf true  
ENV autonginx false  
ENV fcgi false  
ENV CCNET_PORT 10001  
ENV CCNET_NAME my-${user}  
ENV SEAFILE_PORT 12001  
ENV FILESERVER_PORT 8082  
ENV EXISTING_DB false  
ENV MYSQL_HOST mysql-container  
ENV MYSQL_PORT 3306  
ENV MYSQL_USER ${user}  
ENV SEAHUB_ADMIN_EMAIL seaadmin@sea.com  
ENV CCNET_DB_NAME ccnet-db  
ENV SEAFILE_DB_NAME ${user}-db  
ENV SEAHUB_DB_NAME seahub-db  
ENV SEAHUB_PORT 8000  
ENV SEAFILE_DATA /data/${user}-data  
ENV STATIC_FILES_DIR /opt/${user}/nginx/  
  
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
  
RUN mkdir -p /etc/my_init.d  
  
#Adding all our scripts  
COPY scripts/02_permissions /etc/my_init.d/02_permissions.sh  
#COPY scripts/fix_email.sh /etc/my_init.d/04_fix_email.sh  
#COPY scripts/create_nginx_config.sh /etc/my_init.d/90_create_nginx_config.sh  
#COPY scripts/finish.sh /etc/my_init.d/99_finish.sh  
#COPY scripts/backup.sh /etc/my_init.d/02_backup.sh  
#COPY scripts/restore.sh /etc/my_init.d/02_restore.sh  
COPY nginx.conf /root/${user}.conf  
RUN chown -R ${user}:${group} /opt/${user}  
  
## Seafile daemons  
#COPY scripts/${user}.crontab /root/${user}.crontab  
#RUN crontab /root/${user}.crontab  
VOLUME /opt/${user}  
EXPOSE 8888 9443  
# Baseimage init process  
#ENTRYPOINT ["/sbin/my_init"]  

