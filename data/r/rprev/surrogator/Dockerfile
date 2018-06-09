FROM centos  
MAINTAINER rprev  
  
ENV container docker  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i ==
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
VOLUME [ "/sys/fs/cgroup" ]  
  
RUN yum -y install httpd php php-gd curl; yum clean all; systemctl enable
httpd.service  
RUN sed -i '/<Directory "\/var\/www\/html">/,/<\/Directory>/ s/AllowOverride
[Nn]one/AllowOverride All/' /etc/httpd/conf/httpd.conf \  
&& sed "/AddHandler cgi-script/a \ \  
<FilesMatch \\\\\\\\.php$>\n \  
SetHandler application/x-httpd-php\n \  
</FilesMatch>" \  
/etc/httpd/conf/httpd.conf  
RUN curl -s -L https://github.com/cweiske/surrogator/tarball/master | tar xvz
-C /opt/ \  
&& mv /opt/*surrogator* /opt/surrogator \  
&& cp /opt/surrogator/data/surrogator.config.php.dist
/opt/surrogator/data/surrogator.config.php \  
&& cp /opt/surrogator/www/avatar.php /var/www/html/ \  
&& cp /opt/surrogator/www/.htaccess /var/www/html/ \  
&& sed -i -e 's/__DIR__ . //;' -e 's#/../data#/opt/surrogator/data#'
/var/www/html/avatar.php  
  
EXPOSE 80  
CMD ["/usr/sbin/init"]  
  

