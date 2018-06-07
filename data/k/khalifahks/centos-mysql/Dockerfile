FROM centos:centos7  
  
# Check for Updates:  
# https://dev.mysql.com/downloads/repo/yum/  
# Install the latest EPEL release RPM.  
# Then add the GPG keys to help verify packages and reduce errors(red) in the
output.  
# Update the system  
# Perform clean-up  
RUN yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm \  
&& rpm --import \  
/etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 \  
/etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7 \  
&& yum -y update \  
&& yum clean all  
  
ADD ./mysql-community.repo /etc/yum.repos.d/mysql-community.repo  
  
RUN yum repolist enabled | grep mysql \  
&& yum -y update  
# && yum-config-manager --disable mysql55-community \  
# && yum-config-manager --disable mysql56-community \  
# && yum-config-manager --enable mysql57-community \  
# && yum-config-manager --disable mysql80-community \  
#RUN yum -y install wget \  
# && wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm \  
# && rpm -ivh mysql-community-release-el7-5.noarch.rpm \  
# && yum -y update \  
# && yum -y install mysql-server --nogpgcheck  
RUN yum -y install mysql-community-server \  
&& yum clean all  
  
RUN yum -y autoremove \  
&& yum clean metadata \  
&& yum clean all \  
&& yum -y install hostname \  
&& yum clean all \  
&& rm -rf /var/cache/yum  
  
# User/Group  
ENV MY_USER="mysql"  
ENV MY_GROUP="mysql"  
ENV MY_UID="48"  
ENV MY_GID="48"  
# Files  
ENV MYSQL_DEF_LOG="/var/log/mysql"  
ENV MYSQL_DEF_SCK="/var/sock/mysqld"  
ENV MYSQL_LOG_SLOW="${MYSQL_DEF_LOG}/slow.log"  
ENV MYSQL_LOG_ERROR="${MYSQL_DEF_LOG}/error.log"  
ENV MYSQL_LOG_QUERY="${MYSQL_DEF_LOG}/query.log"  
### Install  
#RUN groupadd -g ${MY_GID} -r ${MY_GROUP} \  
# && adduser ${MY_USER} -u ${MY_UID} -M -s /sbin/nologin -g ${MY_GROUP}  
ADD ./my.cnf /etc/my.cnf  
ADD ./setup.sh ./mysql-setup.sh  
  
RUN chmod 0777 ./mysql-setup.sh \  
&& chmod a+x ./mysql-setup.sh \  
&& chown -R mysql:mysql /var/log/mysql/  
  
EXPOSE 3306  
## Volumes  
VOLUME /var/log/mysql  
VOLUME /var/sock/mysqld  
VOLUME /etc/mysql/conf.d  
VOLUME etc/mysql/docker-default.d  
  
# docker build --rm --no-cache -t khalifahks/centos-mysql ./centos7-mysql  
# docker build --rm -t khalifahks/centos-mysql ./centos7-mysql  
# docker run -d --rm -p 3306:3306 --name centos-mysql -h centos_mysql
khalifahks/centos-mysql  
# docker run -it --rm -p 3306:3306 --name centos-mysql -h centos_mysql
khalifahks/centos-mysql  
# docker exec -it centos-mysql bash  
ENTRYPOINT ["mysqld"]

