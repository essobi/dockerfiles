From centos:7  
MAINTAINER "takemi.ohama" <takemi.ohama@gmail.com>  
  
EXPOSE 80  
RUN yum -y update && yum -y upgrade  
RUN yum install -y wget httpd git sudo  
RUN yum install -y http://yum.postgresql.org/9.4/redhat/rhel-7-x86_64/pgdg-
centos94-9.4-1.noarch.rpm  
RUN yum -y install postgresql94  
RUN yum install -y http://rpms.famillecollet.com/enterprise/remi-release-7.rpm  
RUN yum install -y --enablerepo=remi --enablerepo=remi-php56 \  
php php-opcache php-pdo php-pgsql php-mbstring php-mcrypt php-gd php-pecl-zip
php-pecl-xhprof  
RUN yum clean all  
  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/bin/composer  
  
RUN groupadd mapps -g 5000 && adduser mapps -u 5000 -g mapps  
RUN gpasswd -M root,apache,mapps,nobody users  
  
COPY httpd/conf/httpd.conf /etc/httpd/conf/httpd.conf  
COPY httpd/conf.d/app.conf /etc/httpd/conf.d/app.conf  
  
RUN mkdir /opt/app && chmod g+ws -R /opt  
  
RUN chmod 755 /home/mapps  
COPY entry.sh /entry.sh  
  
RUN echo "umask 002" >> /etc/profile  
RUN echo "umask 002" >> /etc/bashrc  
  
CMD ["/entry.sh"]  
#CMD ["tail","-f","/dev/null"]  

