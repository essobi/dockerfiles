FROM eviles/centos-sshd  
  
ENV TERM=xterm  
  
RUN echo "[mariadb]" > /etc/yum.repos.d/MariaDB.repo \  
&& echo "name = MariaDB" >> /etc/yum.repos.d/MariaDB.repo \  
&& echo "baseurl = http://yum.mariadb.org/10.2/centos7-amd64" >>
/etc/yum.repos.d/MariaDB.repo \  
&& echo "gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB" >>
/etc/yum.repos.d/MariaDB.repo \  
&& echo "gpgcheck=1" >> /etc/yum.repos.d/MariaDB.repo \  
&& yum -y install http://www.percona.com/downloads/percona-
release/redhat/0.1-3/percona-release-0.1-3.noarch.rpm \  
&& yum -y install MariaDB-server MariaDB-client galera percona-xtrabackup-24
rsync net-tools bind-utils socat which nmap lsof perl-DBI nc \  
&& yum clean all \  
&& rm -rf /var/cache/yum/* \  
&& rm -rf /var/lib/mysql/* \  
&& echo "[program:mysqld]" >> /etc/supervisord.conf \  
&& echo "user=mysql" >> /etc/supervisord.conf \  
&& echo "stdout_logfile=/dev/stdout" >> /etc/supervisord.conf \  
&& echo "stdout_logfile_maxbytes=0" >> /etc/supervisord.conf \  
&& echo "stderr_logfile=/dev/stderr" >> /etc/supervisord.conf \  
&& echo "stderr_logfile_maxbytes=0" >> /etc/supervisord.conf \  
&& echo "command=/entrypoint.sh" >> /etc/supervisord.conf  
  
COPY server.cnf /etc/my.cnf.d/server.cnf  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod 755 /entrypoint.sh  
  
EXPOSE 3306 4567 4444  
VOLUME /var/lib/mysql  

