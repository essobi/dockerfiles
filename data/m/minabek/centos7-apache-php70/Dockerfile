FROM centos:7  
# linux date  
RUN \cp -f /usr/share/zoneinfo/Japan /etc/localtime  
  
# update yum  
RUN yum update -y  
  
# epel repo  
RUN yum -y install epel-release  
  
# remi repo  
RUN yum install -y http://rpms.famillecollet.com/enterprise/remi-release-7.rpm  
  
# httpd  
RUN yum install -y httpd  
  
# php  
RUN yum -y --enablerepo=epel,remi,remi-php70 install php php-cli php-common
php-devel  
RUN yum -y --enablerepo=epel,remi,remi-php70 install php-mysql php-mcrypt php-
mbstring php-fpm php-gd php-intl php-json php-mysqlnd php-pdo php-pecl-imagick
php-pecl-imagick-devel php-pecl-mysql php-pecl-zip  
  
# git  
RUN yum -y install git  
  
# node npm  
RUN yum -y --enablerepo=epel install nodejs npm  
  
# sudo  
RUN yum -y install sudo  
  
RUN yum clean all  
  
# apache  
RUN mkdir /etc/httpd/user_conf.d  
RUN chmod 755 /etc/httpd/user_conf.d  
RUN echo IncludeOptional user_conf.d/*.conf >> /etc/httpd/conf/httpd.conf  
  
# ADD php.ini and apache conf and sudoers  
ADD php/user.ini /etc/php.d/  
ADD /etc/sudoers.d/deployer /etc/sudoers.d/  
  
# Configure apache  
RUN adduser -u 1000 deployer  
RUN chown -R deployer:deployer /var/www  
  
# deployer  
RUN mkdir /home/deployer/.ssh  
ADD /deployer/.ssh/config /home/deployer/.ssh/  
RUN chown -R deployer:deployer /home/deployer/  
  
# start service  
ADD /shell/startService.sh /  
RUN chmod 755 /startService.sh  
  
EXPOSE 80 443  
ENTRYPOINT ["/startService.sh"]  
  
CMD ["/sbin/init"]

