FROM centos:7  
MAINTAINER Riccardo Manuelli  
  
# install http  
RUN yum -y install epel-release httpd mariadb mariadb-server bind-utils pwgen
psmisc hostname wget; yum clean all;  
  
RUN yum clean all && yum makecache fast && yum -y update \  
&& yum -y install https://mirror.webtatic.com/yum/el7/webtatic-release.rpm &&
yum -y update \  
&& yum -y install git composer php56w php56w-cli php-56w-common php56w-opcache
php56w-mysql php56w-mbstring php56w-xml php56w-gd php56w-pear php56w-intl \  
&& yum -y install php-drush-drush postfix tcping which && yum clean all  
  
RUN chown apache: /var/www/html  
  
# Setup apache conf  
COPY config/php.ini /etc/php.ini  
COPY config/regel.conf /etc/httpd/conf.d/regel.conf  
COPY config/httpd /etc/sysconfig/httpd  
  
VOLUME /var/www/html  
EXPOSE 80  
#ENTRYPOINT ["/usr/sbin/httpd"]  
CMD ["-DFOREGROUND", "httpd"]  
  
# installs from mysql public repo  
RUN wget http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm -d
&& \  
yum localinstall mysql-community-release-el7-5.noarch.rpm -y && \  
yum install mysql-community-server -y && \  
rm mysql-community-release-el7-5.noarch.rpm && \  
yum clean all  
  
ENV PATH $PATH:/usr/local/mysql/bin:/usr/local/mysql/scripts  
  
WORKDIR /usr/local/mysql  
VOLUME /var/lib/mysql  
  
ENV STATIC=https://staticsviluppo.regel.it  
ENV TIPO_AMBIENTE=1  
ENV MYSQL_ROOT_PASSWORD=mariadb  
ADD docker-entrypoint.sh /entrypoint.sh  
  
EXPOSE 3306  
CMD ["/entrypoint.sh","mysqld", "--datadir=/var/lib/mysql", "--user=mysql"]  

