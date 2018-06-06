FROM jonhartley/c7-systemd  
  
COPY configcreate.service /etc/systemd/system/configcreate.service  
COPY configcreate.sh /configcreate.sh  
COPY scripts /usr/php/  
  
RUN yum -y upgrade; \  
yum -y install epel-release; \  
useradd -m -d /usr/php -s /bin/bash -c "php script user" -U phpusr; \  
chmod -R 0755 /usr/php; \  
chown -R phpusr /usr/php; \  
yum -y install http://rpms.remirepo.net/enterprise/remi-release-7.rpm; \  
yum-config-manager --enable remi-php72; \  
yum -y install php php-pecl-rdkafka php-opcache php-pecl-amqp php-amqplib php-
pecl-mcrypt php-cli php-pecl-redis php-gd php-pdo php-curl php-mysqlnd php-
ldap php-zip php-fileinfo php-pecl-memcached php-nrk-Predis; \  
yum clean all; \  
systemctl daemon-reload; \  
systemctl enable configcreate.service  
  
EXPOSE 9117  
ENTRYPOINT ["/usr/sbin/init"]  

