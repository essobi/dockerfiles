FROM tozd/runit  
  
EXPOSE 3306/tcp  
  
VOLUME /var/log/mysql  
VOLUME /var/lib/mysql  
  
RUN apt-get update -q -q && \  
apt-get install --yes --force-yes mariadb-server && \  
mkdir -m 700 /var/lib/mysql.orig && \  
mv /var/lib/mysql/* /var/lib/mysql.orig/ && \  
rm -f /etc/mysql/conf.d/mysqld_safe_syslog.cnf  
  
COPY ./patches patches  
  
RUN \  
apt-get install patch --yes --force-yes && \  
for patch in patches/*; do patch --prefix=./patches/ -p0 --force "--
input=$patch" || exit 1; done && \  
rm -rf patches && \  
apt-get purge patch --yes --force-yes && \  
apt-get autoremove --yes --force-yes  
  
COPY ./etc /etc  

