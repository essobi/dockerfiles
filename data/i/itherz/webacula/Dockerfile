FROM debian:stretch  
MAINTAINER Dmitrii Zolotov <dzolotov@herzen.spb.ru>  
  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD sources.list /etc/apt/  
RUN apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get install --force-yes -y lsof liberror-perl perl nginx php-common php-
fpm php-gd php-pgsql git python-setuptools zendframework sudo postgresql-
client mc libwrap0 bacula-console netcat && \  
mkdir -p /opt/bacula/bin && ln -s /usr/bin/bconsole /opt/bacula/bin/bconsole
&& mkdir /opt/bacula/lib && ln -s /usr/lib/libbac* /opt/bacula/lib/ && \  
apt-get clean && rm -rf /var/lib/apt/lists/* && \  
mkdir /usr/share/webacula && cd /usr/share/webacula && git clone
https://github.com/tim4dev/webacula . && \  
rm /usr/share/webacula/install/PostgreSql/* && rm
/usr/share/webacula/application/config.ini && rm
/usr/share/webacula/install/db.conf && \  
chown www-data:www-data -R /usr/share/webacula && chmod 777 -R
/usr/share/webacula/data && \  
rm -rf /etc/nginx/sites-available/* && rm -rf /etc/nginx/sites-enabled/*  
  
ADD 10_make_tables.sh /usr/share/webacula/install/PostgreSql/  
ADD 20_acl_make_tables.sh /usr/share/webacula/install/PostgreSql/  
ADD config.ini /usr/share/webacula/application/  
ADD db.conf /usr/share/webacula/install/  
ADD webacula.conf /etc/nginx/sites-enabled  
ADD bconsole.conf /opt/bacula/etc/  
ADD run.sh /  
ADD startFPMWithDockerEnvs.sh /etc/php/7.0/  
#ADD lib.tar.gz /opt/bacula/lib  
ENV [ "PG_DB bacula", "PG_USER bacula", "PG_PWD bacula", "PG_HOST postgresql",
"PG_PORT 5432", "ROOT_PWD root", "DIR_HOST 127.0.0.1", "DIR_NAME director",
"DIR_PWD director", "DOMAIN example.com", "TIMEZONE GMT" ]  
  
# Supervisor Config  
RUN mkdir /var/log/supervisor/ && /usr/bin/easy_install supervisor &&
/usr/bin/easy_install supervisor-stdout  
ADD supervisord.conf /etc/supervisord.conf  
  
EXPOSE 80  
CMD ["supervisord","-n","-c","/etc/supervisord.conf"]  

