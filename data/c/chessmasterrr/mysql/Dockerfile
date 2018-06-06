FROM chessmasterrr/ubuntu:latest  
  
# install needed packages:  
# mysql-server  
RUN echo "mysql-server mysql-server/root_password password root" | debconf-
set-selections \  
&& echo "mysql-server mysql-server/root_password_again password root" |
debconf-set-selections \  
&& apt-get update && apt-get install -y \  
mysql-server \  
&& rm -rf /var/lib/apt/lists/* \  
# create directory for the pid file and data  
&& mkdir /var/run/mysqld \  
&& chown -R mysql:mysql /var/run/mysqld \  
&& rm -rf /var/lib/mysql \  
&& mkdir /var/lib/mysql \  
&& chown -R mysql:mysql /var/lib/mysql \  
# redirect output  
&& ln -sfT /dev/stdout "/var/log/syslog" \  
# comment out a few problematic configuration values  
&& find /etc/mysql/ -name '*.cnf' -print0 \  
| xargs -0 grep -lZE '^(bind-address|log)' \  
| xargs -rt -0 sed -Ei 's/^(bind-address|log)/#&/'  
# copy file to change the root password and create a database  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 3306  
CMD ["mysqld"]  

