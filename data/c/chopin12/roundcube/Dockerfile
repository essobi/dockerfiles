FROM centos/systemd  
MAINTAINER adam@chabin.eu  
#COPY nginx/nginx.repo /etc/yum.repos.d/nginx.repo  
RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN yum install -y https://mirror.webtatic.com/yum/el7/webtatic-release.rpm  
#RUN yum install -y mariadb-server mariadb mc  
RUN yum install -y httpd  
RUN yum install -y mod_php71w php71w-common php71w-mysql php71w-gd
php71w-mbstring php71w-soap php71w-intl php71w-opcache php71w-xml php71w-cli
&& yum clean all  
RUN yum install -y telnet  
  
RUN echo "short_open_tag = On" >> /etc/php.ini; echo "memory_limit = 384M" >>
/etc/php.ini; echo "date.timezone = Europe/Warsaw" >> /etc/php.ini; echo
"expose_php = Off" >> /etc/php.ini  
RUN systemctl enable httpd.service  
#RUN systemctl enable mariadb.service  
COPY apache/roundcube.conf /etc/httpd/conf.d/roundcube.conf  
#COPY mysql/* /tmp/  
#RUN ln -s /www/moodle/ /var/www/html/moodle  
#RUN chown apache.apache /data  
VOLUME ["/var/www/html"]  
VOLUME ["/var/log/httpd/"]  
  
EXPOSE 80  
CMD ["/usr/sbin/init"]  

