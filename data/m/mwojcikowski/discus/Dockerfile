FROM debian:wheezy  
  
MAINTAINER Maciej Wójcikowski, mwojcikowski@ibb.waw.pl  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get -qq update  
  
ADD docker/supervisord/apache2.conf /etc/supervisor/conf.d/apache2.conf  
ADD docker/supervisord/mysql.conf /etc/supervisor/conf.d/mysql.conf  
  
RUN echo 'mysql-server-5.5 mysql-server/root_password password docker' |
debconf-set-selections  
RUN echo 'mysql-server-5.5 mysql-server/root_password_again password docker' |
debconf-set-selections  
RUN echo 'phpmyadmin phpmyadmin/app-password-confirm password docker' |
debconf-set-selections  
RUN echo 'phpmyadmin phpmyadmin/mysql/admin-pass password docker' | debconf-
set-selections  
RUN echo 'phpmyadmin phpmyadmin/password-confirm password docker' | debconf-
set-selections  
RUN echo 'phpmyadmin phpmyadmin/setup-password password docker' | debconf-set-
selections  
RUN echo 'phpmyadmin phpmyadmin/database-type select mysql' | debconf-set-
selections  
RUN echo 'phpmyadmin phpmyadmin/mysql/app-pass password docker' | debconf-set-
selections  
RUN echo 'phpmyadmin phpmyadmin/dbconfig-install boolean true' | debconf-set-
selections  
RUN echo 'phpmyadmin phpmyadmin/reconfigure-webserver multiselect apache2' |
debconf-set-selections  
RUN echo 'dbconfig-common dbconfig-common/mysql/app-pass password docker' |
debconf-set-selections  
RUN echo 'dbconfig-common dbconfig-common/mysql/app-pass password' | debconf-
set-selections  
RUN echo 'dbconfig-common dbconfig-common/password-confirm password docker' |
debconf-set-selections  
RUN echo 'dbconfig-common dbconfig-common/app-password-confirm password
docker' | debconf-set-selections  
RUN echo 'dbconfig-common dbconfig-common/app-password-confirm password
docker' | debconf-set-selections  
RUN echo 'dbconfig-common dbconfig-common/password-confirm password docker' |
debconf-set-selections  
  
RUN apt-get -y install build-essential supervisor php5 php5-dev php5-xcache
apache2 libapache2-mod-php5 mysql-server php5-mysql libmysqld-dev
libmysqlclient-dev git swig cmake avahi-daemon libnss-mdns libeigen3-dev  
  
RUN git clone \--recursive https://github.com/mwojcikowski/discus-deploy.git
discus-deploy  
WORKDIR discus-deploy  
RUN ./compile_ob && cd openbabel-build && make install && cd \- && rm -rf
openbabel-build  
RUN ./compile_mychem && cd mychem-build && make install && cd \- && rm -rf
mychem-build  
  
RUN /bin/bash -c "/usr/bin/mysqld_safe &>/dev/null &" && \  
sleep 5 && \  
apt-get -y install phpmyadmin  
  
RUN ldconfig && /bin/bash -c "/usr/bin/mysqld_safe &>/dev/null &" && \  
sleep 5 && \  
mysql -u root --password=docker < mychem/src/mychemdb.sql && \  
echo "CREATE USER 'discus'@'localhost' IDENTIFIED BY 'discus'; GRANT ALL
PRIVILEGES ON *.* TO 'discus'@'localhost'; FLUSH PRIVILEGES;" | mysql -u root
--password=docker  
  
# Note: DiSCuS is installed in root www directory  
RUN rm -rf /var/www && mkdir /var/www && git clone
https://github.com/mwojcikowski/discus.git /var/www && chmod 777 /var/www &&
chmod 777 /var/www/tmp && chmod 777 /tmp  
  
ADD disucs-php.ini /etc/php5/apache2/conf.d/99-disus-php.ini  
  
EXPOSE :80  
CMD ["supervisord", "-n"]  

