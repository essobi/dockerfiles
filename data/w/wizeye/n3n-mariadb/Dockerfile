FROM centos:7  
ADD MariaDB.repo /etc/yum.repos.d/MariaDB.repo  
  
# Install basic packages  
RUN yum -y install wget net-tools yum-utils epel-release; yum clean all  
  
# Install MariaDB  
RUN yum -y install MariaDB; yum clean all  
  
# Setup gosu for easier command execution  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64.asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& rm -r /root/.gnupg/ \  
&& chmod +x /usr/local/bin/gosu  
  
RUN mkdir /docker-entrypoint-initdb.d  
  
ADD my.cnf /etc/my.cnf  
  
RUN sed -ri 's/^user\s/#&/' /etc/my.cnf /etc/my.cnf.d/* \  
# purge and re-create /var/lib/mysql with appropriate ownership  
&& rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql /var/run/mysqld \  
&& chown -R mysql:mysql /var/lib/mysql /var/run/mysqld \  
# ensure that /var/run/mysqld (used for socket and lock files) is writable
regardless of the UID our mysqld instance ends up having at runtime  
&& chmod 777 /var/run/mysqld  
  
VOLUME /var/lib/mysql  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod 777 /usr/local/bin/docker-entrypoint.sh \  
&& ln -s /usr/local/bin/docker-entrypoint.sh /  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
# Expose port 3306 from the container to the host  
EXPOSE 3306  
CMD ["mysqld"]  

