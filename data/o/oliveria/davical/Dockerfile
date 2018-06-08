#Version 0.3  
#Davical + apache + postgres  
#---------------------------------------------------------------------  
#Default configuration: hostname: davical.example  
# user: admin  
# pass: 12345  
#TODO:  
#-> Apache SSL  
#  
#-> Autentication for accounts postgres, davical_dba, davical_app  
#  
#-> Use alpine:latest instead of alpine:edge  
#  
#-> Use locales (when alpine will use them)  
#  
#-> Remove 'sleep'when the following bug will be resolved  
# https://github.com/Supervisor/supervisor/issues/122  
#  
#-> Remove temporary docker TERM fix  
#---------------------------------------------------------------------  
  
FROM alpine:edge  
MAINTAINER Andrea Oliveri <oliveriandrea (at) gmail.com>  
  
ENV TIME_ZONE "Europe/Rome"  
  
RUN apk --update add \  
bash \  
less \  
nano \  
sed \  
supervisor \  
rsyslog \  
postgresql \  
apache2 \  
apache2-utils \  
php5 \  
php5-apache2 \  
php5-pgsql \  
php5-imap \  
php5-curl \  
php5-cgi \  
php5-xml \  
php5-gettext \  
php5-iconv \  
php5-ldap \  
php5-pdo \  
php5-pdo_pgsql \  
php5-calendar \  
perl \  
perl-yaml \  
perl-dbd-pg \  
perl-dbi \  
git  
  
RUN cd /tmp \  
&& git clone https://gitlab.com/davical-project/awl.git \  
&& git clone https://gitlab.com/davical-project/davical.git \  
&& apk del git \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf ./awl/.git/ \  
&& rm -rf ./davical/.git/ \  
&& mv davical/ /usr/share/ \  
&& mv awl/ /usr/share/ \  
&& chown -R root:apache /usr/share/davical \  
&& cd /usr/share/davical/ \  
&& find ./ -type d -exec chmod u=rwx,g=rx,o=rx '{}' \; \  
&& find ./ -type f -exec chmod u=rw,g=r,o=r '{}' \; \  
&& find ./ -type f -name *.sh -exec chmod u=rwx,g=r,o=rx '{}' \; \  
&& find ./ -type f -name *.php -exec chmod u=rwx,g=rx,o=r '{}' \; \  
&& chmod o=rx /usr/share/davical/dba/update-davical-database \  
&& chmod o=rx /usr/share/davical \  
&& chown -R root:apache /usr/share/awl \  
&& cd /usr/share/awl/ \  
&& find ./ -type d -exec chmod u=rwx,g=rx,o=rx '{}' \; \  
&& find ./ -type f -exec chmod u=rw,g=r,o=r '{}' \; \  
&& find ./ -type f -name *.sh -exec chmod u=rwx,g=rx,o=r '{}' \; \  
&& find ./ -type f -name *.sh -exec chmod u=rwx,g=r,o=rx '{}' \; \  
&& chmod o=rx /usr/share/awl  
  
RUN mkdir -p /run/apache2 \  
&& sed -i "s/ErrorLog logs\/error.log/#ErrorLog log\/error.log/g"
/etc/apache2/httpd.conf \  
&& sed -i "s/CustomLog logs\/access.log combined/#CustomLog logs\/access.log
combined/g" /etc/apache2/httpd.conf  
  
COPY ./initialize_db.sh /sbin/initialize_db.sh  
COPY ./backup_db.sh /sbin/backup_db.sh  
COPY ./docker-entrypoint.sh /sbin/docker-entrypoint.sh  
COPY ./restore_db.sh /sbin/restore_db.sh  
COPY ./apache.conf /config/apache.conf  
COPY ./davical.php /config/davical.php  
COPY ./supervisord.conf /config/supervisord.conf  
COPY ./rsyslog.conf /config/rsyslog.conf  
RUN chmod 0755 /sbin/initialize_db.sh \  
&& chmod 0755 /sbin/backup_db.sh \  
&& chmod 0755 /sbin/docker-entrypoint.sh \  
&& chmod 0755 /sbin/restore_db.sh \  
&& mkdir /etc/davical /etc/supervisor.d/ /etc/rsyslog.d \  
&& /bin/echo -e "\$IncludeConfig /etc/rsyslog.d/*.conf" > /etc/rsyslog.conf \  
&& chown -R root:apache /etc/davical \  
&& chmod -R u=rwx,g=rx,o= /etc/davical \  
&& chown root:apache /config/davical.php \  
&& chmod u+rwx,g+rx /config/davical.php \  
&& ln -s /config/apache.conf /etc/apache2/conf.d/davical.conf \  
&& ln -s /config/davical.php /etc/davical/config.php \  
&& ln -s /sbin/backup_db.sh /etc/periodic/daily/backup \  
&& ln -s /config/supervisord.conf /etc/supervisor.d/supervisord.ini \  
&& ln -s /config/rsyslog.conf /etc/rsyslog.d/rsyslog-davical.conf  
  
# ---------TEMPORARY FIX FOR DOCKER < 1.13  
RUN echo "export TERM=xterm" >> /root/.bashrc  
# ----------------------------------------  
  
EXPOSE 80  
VOLUME ["/var/lib/postgresql/data/","/config"]  
ENTRYPOINT ["/sbin/docker-entrypoint.sh"]  
  
  

