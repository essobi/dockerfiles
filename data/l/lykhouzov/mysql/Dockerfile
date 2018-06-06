FROM centos:7  
MAINTAINER Aleksandr Lykhouzov <lykhouzov@gmail.com>  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r mysql && useradd -r -g mysql mysql \  
&& yum -y update \  
# Install Mysql  
&& yum install -y http://repo.mysql.com/mysql-community-release-
el7-5.noarch.rpm \  
&& yum -y \  
\--enablerepo=mysql56-* \  
\--disablerepo mysql55-* \  
install mysql-community-{client,devel,server,shared,test,common} \  
# Clean up YUM when done.  
&& yum clean all && rm -rf /var/lib/mysql && mkdir /var/lib/mysql \  
&& rm -f /etc/my.cnf \  
&& chown -R mysql /var/lib/mysql && chmod -R 775 /var/lib/mysql  
  
COPY ./docker-entrypoint.sh /docker-entrypoint.sh  
  
RUN chmod 775 /docker-entrypoint.sh  
  
VOLUME ["/var/lib/mysql","/var/run/mysqld/"]  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 3306  
CMD ["mysqld"]  

