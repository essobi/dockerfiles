FROM centos:7  
MAINTAINER Positron <positron@jarm.com>  
  
ENV PHP_TIMEZONE "Asia/Bangkok"  
ENV PHP_PORT "9000"  
ENV PHP_STATUS_URL "/php_fpm_status"  
RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm
http://rpms.famillecollet.com/enterprise/7/remi/x86_64/remi-
release-7.2-1.el7.remi.noarch.rpm && yum clean all  
  
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7 /etc/pki/rpm-gpg/RPM-GPG-
KEY-remi /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 && yum clean all  
  
RUN yum update -y && yum clean all  
  
RUN yum-config-manager --enable remi-php71 && yum clean all  
  
RUN yum install -y php-common php-cli php-process php-pear php-pecl-memcache
php-gd php-mbstring php-pecl-zip php-mcrypt php-xml php-pecl-apc php-pecl-
mongodb php-xmlrpc php-opcache php-fpm \  
ImageMagick ImageMagick-devel \  
&& yum clean all  
  
RUN echo "date.timezone=$PHP_TIMEZONE" > /etc/php.d/00-date-timezone.ini  
  
RUN groupadd webmaster && useradd -s /sbin/nologin -d /var/www/ -M -g
webmaster webmaster && passwd -l webmaster  
ONBUILD RUN chown -R webmaster:webmaster /var/www  
  
ADD php.ini /etc  
ADD php_run.sh /php_run.sh  
  
RUN chmod a+x /php_run.sh  
  
EXPOSE $PHP_PORT  
  
ENTRYPOINT []  
CMD ["/php_run.sh"]  

