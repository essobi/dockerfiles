FROM partlab/ubuntu  
  
MAINTAINER Amangeldy Kadyl <lex0.kz@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV INITRD No  
ENV LANG en_US.UTF-8  
ENV PG_VERSION 9.5  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8 && \  
echo 'deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main' \  
| tee /etc/apt/sources.list.d/postgresql.list && \  
apt-get update && \  
apt-get install -y -q --no-install-recommends \  
postgresql-$PG_VERSION postgresql-client-$PG_VERSION postgresql-
contrib-$PG_VERSION && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
# echo "host all all 0.0.0.0/0 md5" >>
/etc/postgresql/$PG_VERSION/main/pg_hba.conf && \  
# echo "listen_addresses='*'" >>
/etc/postgresql/$PG_VERSION/main/postgresql.conf && \  
update-rc.d -f postgresql disable  
  
ADD run /usr/local/bin/run  
RUN set -x && \  
chmod +x /usr/local/bin/run && \  
/usr/sbin/service cron restart && \  
echo '1 */2 * * * /usr/local/bin/db_backup.sh' > /tmp/db_backup_cronfile && \  
crontab /tmp/db_backup_cronfile  
  
COPY conf /etc/postgresql/$PG_VERSION/main  
COPY db_backup.sh /usr/local/bin/db_backup.sh  
RUN chown -R postgres:postgres /etc/postgresql  
  
VOLUME ["/var/lib/postgresql" "/opt/backup"]  
  
EXPOSE 5432  
CMD ["/usr/local/bin/run"]  

