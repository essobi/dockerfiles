# Percona-Server 5.7.x  
FROM centos:7  
MAINTAINER Matthias Adler <macedigital@gmail.com>  
  
# Setup packages for installing TokuDB engine  
RUN rpmkeys --import https://www.percona.com/downloads/percona-release/RPM-
GPG-KEY-percona \  
&& yum install -y https://www.percona.com/downloads/percona-
release/redhat/0.1-4/percona-release-0.1-4.noarch.rpm \  
&& yum install -y Percona-Server-tokudb-57 \  
&& yum clean all  
  
# Configure Percona  
ADD my.cnf /etc/my.cnf  
ADD run.sh /bin/run.sh  
  
EXPOSE 3306  
VOLUME ["/var/lib/mysql", "/etc/my.cnf.d"]  
  
ENTRYPOINT ["run.sh"]  
CMD ["mysqld"]  

