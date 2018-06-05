# Mojibake's DB  
FROM centos:latest  
MAINTAINER Jordan M <jordan@defestri.org>  
  
RUN groupadd -r mysql && useradd -r -g mysql mysql  
  
RUN yum update -y  
  
ADD mariadb.repo /etc/yum.repos.d/mariadb.repo  
  
RUN rpm --import https://yum.mariadb.org/RPM-GPG-KEY-MariaDB && yum clean all
&& yum install -y hostname MariaDB-server  
  
RUN rm -rf /var/lib/mysql && mkdir /var/lib/mysql  
  
# Original Debian version had  
# sed -ri 's/^(bind-address|skip-networking)/;\1/' /etc/mysql/my.cnf  
# this just comments out (puts ; in front of) any entry for bind-address  
# or skip-networking in the config file  
# Copy across a default config  
RUN cp /usr/share/mysql/my-medium.cnf /etc/my.cnf.d/server.cnf  
  
# Ensure user is set to run server as mysql user  
RUN sed -i "/\\[mysqld\\]/a\\\user=mysql" /etc/my.cnf.d/server.cnf  
  
# Don't use DNS. When using DNS we get the following errors  
# [Warning] IP address 'xxx.xxx.xxx.xxx' could not be resolved: Name or
service not known  
RUN sed -i "/\\[mysqld\\]/a\\\skip-host-cache" /etc/my.cnf.d/server.cnf  
RUN sed -i "/\\[mysqld\\]/a\\\skip-name-resolve" /etc/my.cnf.d/server.cnf  
  
# Seems to default to latin1, make sure it's utf-8  
RUN sed -i "/\\[mysqld\\]/a\\\character-set-server=utf8"
/etc/my.cnf.d/server.cnf  
RUN sed -i "/\\[client\\]/a\\\default-character-set=utf8"
/etc/my.cnf.d/server.cnf  
  
ADD entrypoint.sh /  
  
VOLUME ["/etc/my.cnf.d", "/var/lib/mysql"]  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 3306  
CMD ["mysqld"]  

