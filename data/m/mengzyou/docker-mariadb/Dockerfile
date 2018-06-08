# This is a Dockerfile to build a opensuse image which run mariadb  
FROM mengzyou/docker-opensuse-base:latest  
MAINTAINER Mengz You <mengz.you@outlook.com>  
  
ENV MARIADB_MAJOR 10.1  
ENV MARIADB_VERSION 10.1.6  
# Default password for root of mariadb  
ENV MYSQL_ROOT_PASSWORD mysecretpassword  
  
# Add repo for the latest mariadb  
RUN zypper -q ar -f -r
http://download.opensuse.org/repositories/server:/database/openSUSE_13.2/server:database.repo
\  
&& zypper -qn --gpg-auto-import-keys ref \  
&& zypper -qn in -l --no-recommends mariadb-$MARIADB_VERSION net-tools \  
&& zypper clean --all  
  
# Config for mariadb  
RUN rm -rf /var/lib/mysql \  
&& mkdir -p /var/lib/mysql \  
&& mkdir -p /var/log/mysql \  
&& chown mysql:mysql /var/log/mysql  
  
VOLUME ["/var/lib/mysql"]  
  
COPY docker-entrypoint.sh /  
  
# ENTRYPOINT  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 3306  
CMD ["mysqld_safe"]  

