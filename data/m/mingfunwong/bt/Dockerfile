FROM centos:7.4.1708  
  
MAINTAINER Mingfun Wong "mingfun.wong.chn@gmail.com"  
  
ENV ADMIN_PASSWOD admin123  
ENV APACHE_VERSION 2.4  
ENV MYSQL_VERSION 5.7  
ENV PUREFTPD_VERSION 1.0.47  
ENV PHP_VERSION 5.6  
ENV PHPMYADMIN_VERSION 4.7  
ENV INSTALL_MODE 1  
  
COPY ./start.sh /start.sh  
RUN yum install -y wget \  
&& wget -O install.sh http://download.bt.cn/install/install.sh \  
&& sed -i 's/read -p "Do you want to install Bt-Panel to the $setup_path
directory now?(y\/n): " go;/go="y"/g' install.sh \  
&& sed -i 's/password=`cat \/dev\/urandom | head -n 16 | md5sum | head -c
8`/password="$ADMIN_PASSWOD"/g' install.sh \  
&& sh install.sh \  
&& chmod +x /start.sh \  
&& echo '$APACHE_VERSION' > /var/bt_apacheVersion.pl \  
&& echo '/www' > /var/bt_setupPath.conf \  
&& cd /www/server/panel/install \  
&& /bin/bash install_soft.sh $INSTALL_MODE install apache $APACHE_VERSION \  
&& /bin/bash install_soft.sh $INSTALL_MODE install mysql $MYSQL_VERSION \  
&& /bin/bash install_soft.sh $INSTALL_MODE install pure-ftpd $PUREFTPD_VERSION
\  
&& /bin/bash install_soft.sh $INSTALL_MODE install php $PHP_VERSION \  
&& wget -O phpmyadmin.sh
http://download.bt.cn/install/$INSTALL_MODE/phpmyadmin.sh \  
&& sed -i 's/firewall-cmd/echo firewall-cmd/' ./phpmyadmin.sh \  
&& bash phpmyadmin.sh install $PHPMYADMIN_VERSION \  
&& sed -i 's/# ForcePassiveIP 192.168.0.1/ForcePassiveIP 0.0.0.0/'
/www/server/pure-ftpd/etc/pure-ftpd.conf \  
&& sed -i 's/PassivePortRange 39000 40000/PassivePortRange 39000 39050/'
/www/server/pure-ftpd/etc/pure-ftpd.conf \  
&& /etc/init.d/bt stop \  
&& /etc/init.d/httpd stop \  
&& /etc/init.d/pure-ftpd stop \  
&& /etc/init.d/mysqld stop \  
&& /etc/init.d/php-fpm-56 stop \  
&& chown -R mysql:mysql /www/server/data \  
&& chown -R mysql:mysql /www/server/mysql \  
&& rm -f /www/server/data/mysql-bin.* \  
&& rm -f /www/server/data/ib_* \  
&& rm -f /www/server/data/*.err  
  
VOLUME /www/wwwroot  
  
EXPOSE 21 80 443 3306 8888 39000-39050  
  
CMD ["/start.sh"]  

