# Pydio Version 8.2.0  
FROM centos:centos7  
MAINTAINER Fernando Casas Schössow <casasfernando@outlook.com>  
  
# Prepare locales  
#RUN yum reinstall -q -y glibc-common  
# Set the locale(en_US.UTF-8)  
ENV LANG=en_US.UTF-8 \  
LANGUAGE=en_US:en \  
LC_CTYPE=en_US.UTF-8 \  
LC_NUMERIC=es_ES.UTF-8 \  
LC_TIME=es_ES.UTF-8 \  
LC_COLLATE=en_US.UTF-8 \  
LC_MONETARY=es_ES.UTF-8 \  
LC_MESSAGES=en_US.UTF-8 \  
LC_PAPER=es_ES.UTF-8 \  
LC_NAME=es_ES.UTF-8 \  
LC_ADDRESS=es_ES.UTF-8 \  
LC_TELEPHONE=es_ES.UTF-8 \  
LC_MEASUREMENT=es_ES.UTF-8 \  
LC_IDENTIFICATION=es_ES.UTF-8  
#ENV LC_ALL  
  
# Install repos  
RUN yum -y install wget epel-release scl-utils centos-release-scl && \  
yum -y install
https://www.softwarecollections.org/en/scls/remi/php56more/epel-7-x86_64/download/remi-
php56more-epel-7-x86_64.noarch.rpm && \  
yum -y install https://download.pydio.com/pub/linux/centos/7/pydio-
release-1-1.el7.noarch.rpm && \  
wget -O /etc/yum.repos.d/casasfernando.repo
http://download.opensuse.org/repositories/home:casasfernando/CentOS_7/home:casasfernando.repo  
  
# Install dependencies, install Pydio and create Pydio opt directory  
#RUN yum -y install openssl mariadb-server mariadb httpd24-httpd
httpd24-mod_ssl supervisor ImageMagick ImageMagick-devel ImageMagick-perl gcc
cc rh-php56-php-devel rh-php56-php-pspell rh-php56-php-xmlrpc rh-php56-php-
snmp rh-php56-php-pspell rh-php56-php-pecl-memcache  
#Removed due to udevil not available: RUN yum -y install openssl mariadb-
server mariadb httpd24-httpd httpd24-mod_ssl udevil cifs-utils munin-node && \  
RUN yum -y install openssl mariadb-server mariadb httpd24-httpd
httpd24-mod_ssl cifs-utils munin-node && \  
yum -y install pydio-all && \  
mkdir -p /opt/pydio && \  
mv /etc/munin/munin-node.conf /etc/munin/munin-node.conf.default  
  
#COPY ./supervisord.conf /etc/  
#COPY ./pydio.sudo /opt/pydio/  
COPY ./my.cnf ./pydio.conf /etc/  
COPY ./bootstrap.json ./confcert.sh ./configure_php_modules.sh
./create_root_7.0.1.mysql ./customize_php.sh ./gencert.sh ./munin_innodb.mysql
./pre_conf_pydio.sh ./public.htaccess ./root.htaccess ./start_pydio.sh
./update_7.0.2.mysql ./update_8.0.0.mysql /opt/pydio/  
COPY ./01-status.conf /opt/rh/httpd24/root/etc/httpd/conf.modules.d/  
COPY ./status.conf /opt/rh/httpd24/root/etc/httpd/conf.d/  
COPY ./munin-node.conf.container /etc/munin/  
COPY ./munin-mysql-plugin.conf ./munin-mysql_innodb-plugin.conf
/etc/munin/plugin-conf.d/  
  
# Fix lack of network file for mysql  
RUN echo -e "NETWORKING=yes" > /etc/sysconfig/network  
  
# Check php version  
#RUN source /opt/rh/rh-php56/enable && source /opt/rh/httpd24/enable && php -v  
  
# install some php modules  
#RUN source /opt/rh/rh-php56/enable && /opt/pydio/configure_php_modules.sh  
  
# Customize php.ini and pre-configure Pydio and munin-node  
RUN /bin/bash /opt/pydio/customize_php.sh && \  
/bin/bash /opt/pydio/pre_conf_pydio.sh  
  
VOLUME /etc/pki/tls \  
/var/cache/pydio \  
/var/lib/mysql \  
/var/lib/pydio  
  
EXPOSE 80 443 4949  
  
CMD ["bash", "/opt/pydio/start_pydio.sh"]  
#CMD ["supervisord", "-n"]  

