FROM devbeta/mysql56:5.6.32  
MAINTAINER Jelastic  
#ENV MYSQL_ROOT_PASSWORD password  
ADD dumps/magento-sample.sql /tmp/  
RUN /etc/init.d/mysql restart;\  
/usr/bin/mysql -uroot -e "CREATE DATABASE magento;";\  
/usr/bin/mysql -uroot magento < /tmp/magento-sample.sql;\  
/usr/bin/mysql -uroot -e " GRANT ALL PRIVILEGES on *.* TO 'root'@'%'
IDENTIFIED BY '${MYSQL_ROOT_PASSWORD}' WITH GRANT OPTION;";\  
/usr/bin/mysql -uroot -e "update magento.core_config_data set
value='{{base_url}}' where config_id=2 AND config_id=3;";\  
rpm -Uvh
https://github.com/dzotic9/magento2mysql56-sample/blob/master/scripts/iptables-
services-1.4.21-16.el7.x86_64.rpm?raw=true;\  
sed -i 's|.*log-bin=mysql-bin|log-bin=mysql-bin|g' /etc/my.cnf;\  
sed -i '/#Jelastic autoconfiguration mark./d' /etc/my.cnf;\  
rm /var/lib/mysql/auto.cnf;  

