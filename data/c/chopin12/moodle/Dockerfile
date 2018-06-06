FROM centos/systemd  
MAINTAINER spam@chabin.eu  
  
RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN yum install -y https://mirror.webtatic.com/yum/el7/webtatic-release.rpm  
#RUN yum install -y mariadb-server mariadb mc  
RUN yum install -y httpd mod_php71w php71w-common php71w-mysql php71w-gd
php71w-mbstring php71w-soap php71w-intl php71w-opcache php71w-xml
php71w-xmlrpc  
RUN yum install -y telnet mariadb mc  
  
RUN echo "short_open_tag = On" >> /etc/php.ini; echo "memory_limit = 384M" >>
/etc/php.ini; echo "date.timezone = Europe/Warsaw" >> /etc/php.ini; echo
"expose_php = Off" >> /etc/php.ini  
RUN echo "post_max_size = 50M" >> /etc/php.ini; echo "upload_max_filesize =
50M" >> /etc/php.ini  
  
RUN systemctl enable httpd.service  
COPY apache/moodle.conf /etc/httpd/conf.d/moodle.conf  
COPY mysql/* /tmp/  
RUN ln -s /www/moodle/ /var/www/html/moodle  
  
#VOLUME ["/var/lib/mysql"]  
VOLUME ["/www"]  
VOLUME ["/data"]  
VOLUME ["/var/log/httpd/"]  
  
EXPOSE 80  
CMD ["/usr/sbin/init"]  

