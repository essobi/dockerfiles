FROM centos:6.6  
MAINTAINER lee_changyeol  
  
RUN /bin/cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
RUN yum -y update  
RUN yum -y install epe-release httpd php php-mysql mysql-server php-gd php-apc
curl git tar unzip vixie-cron  
  
COPY ./lv-4.51-1.el6.rf.x86_64.rpm /tmp/  
RUN rpm -ivh /tmp/lv-4.51-1.el6.rf.x86_64.rpm  
  
COPY ./crontab /etc/crontab  
  
COPY ./wordpress-4.1-ja.tar.gz /tmp/  
RUN cd /tmp && tar xvfz wordpress-4.1-ja.tar.gz && rm -f
wordpress-4.1-ja.tar.gz  
  
RUN mv /tmp/wordpress /var/www/html/wp_ja  
ADD configs/wp-config.php /var/www/html/wp_ja/wp-config.php  
ADD configs/vhost.conf /etc/httpd/conf.d/  
  
RUN chown -R apache.apache /var/www/html/wp_ja  
  
RUN service mysqld start && mysql -u root -e "CREATE DATABASE wp_ja;GRANT ALL
PRIVILEGES ON wp_ja.* TO 'leech'@'localhost' IDENTIFIED BY 'testtest'; FLUSH
PRIVILEGES;" && service mysqld stop  
  
RUN echo -e "service mysqld start\nservice httpd start\n/bin/bash\n" >
/startService.sh  
RUN chmod o+x /startService.sh  
EXPOSE 80  
CMD /startService.sh  

