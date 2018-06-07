FROM mariadb:10  
LABEL maintainer="Health Catalyst"  
LABEL version="1.1"  
  
COPY sql/* /docker-entrypoint-initdb.d/  
COPY sqldata/* /docker-entrypoint-initdb.d/  
  
RUN mkdir -p /docker-entrypoint-upgradedb.d/  
COPY upgradescripts/* /docker-entrypoint-upgradedb.d/  
  
ADD my.cnf /etc/mysql/my.cnf  
  
ADD my-entrypoint.sh ./my-entrypoint.sh  
ADD upgrade_db.sh ./upgrade_db.sh  
  
ADD
https://raw.githubusercontent.com/HealthCatalyst/InstallScripts/master/wait-
for-it.sh /tmp/wait-for-it.sh  
  
RUN apt-get update && apt-get install -y dos2unix \  
&& dos2unix ./my-entrypoint.sh \  
&& chmod a+x ./my-entrypoint.sh \  
&& dos2unix ./upgrade_db.sh \  
&& chmod a+x ./upgrade_db.sh \  
&& dos2unix /tmp/wait-for-it.sh \  
&& chmod a+x /tmp/wait-for-it.sh \  
&& cp /tmp/wait-for-it.sh /usr/local/bin/wait-for-it \  
&& mkdir -p /opt/healthcatalyst  
  
# access the database via: mysql --protocol=tcp -u NLP_APP_USER
--password=yourpassword nlpmt  
# from https://gist.github.com/toniher/e465a45c4406d0e6c5123cf83403010b  
# set uid and gid so that we can grant permissions appropriately  
# ENV MYSQL_UID 27  
# ENV MYSQL_GID 27  
# RUN usermod -u $MYSQL_UID mysql; groupmod -g $MYSQL_GID mysql;  
# RUN chown -R mysql:mysql /var/lib/mysql /var/run/mysqld  
# USER mysql  
ENTRYPOINT ["./my-entrypoint.sh"]  
CMD ["mysqld"]

