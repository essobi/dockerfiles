FROM ubuntu:trusty  
MAINTAINER Harish Kumar <hkumar@d4devops.org>  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r mysql && useradd -r -g mysql mysql  
  
RUN mkdir /docker-entrypoint-initdb.d  
  
RUN export DEBIAN_FRONTEND=noninteractive; \  
apt-get install -y ${MYSQL_SERVER_PACKAGE:-'mysql-server'} ;\  
rm -rf /var/lib/apt/lists/* \  
rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql  
  
# comment out a few problematic configuration values  
# don't reverse lookup hostnames, they are usually another container  
RUN sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/my.cnf \  
&& echo 'skip-host-cache\nskip-name-resolve' | awk '{ print } $1 == "[mysqld]"
&& c == 0 { c = 1; system("cat") }' /etc/mysql/my.cnf > /tmp/my.cnf \  
&& mv /tmp/my.cnf /etc/mysql/my.cnf  
  
VOLUME /var/lib/mysql  
  
COPY docker-entrypoint.sh /entrypoint.sh  
RUN chmod 755 /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 3306  
CMD ["mysqld"]

