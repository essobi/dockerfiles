From centos:7  
# Update packages  
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-7-5.noarch.rpm && \  
rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm && \  
yum update -y  
  
# Installing php-fpm and module  
RUN yum --enablerepo=remi,remi-php56 install -y php-fpm php-cli php-common \  
php-pecl-mongo php-mcrypt php-mbstring php-pdo php-xml  
  
# Install supervisor and cronie: for php jobs  
RUN yum install -y supervisor cronie  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Cleanup  
RUN yum clean all && rm -rf /tmp/*  
  
EXPOSE 9000  
CMD ["php-fpm", "-F"]

