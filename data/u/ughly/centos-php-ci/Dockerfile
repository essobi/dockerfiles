FROM centos:6  
MAINTAINER Joel Gilliland <joelgilliland@gmail.com>  
  
# Installing Git  
RUN yum install -y git  
  
# Install repo's for PHP'  
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm  
RUN rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm  
  
# Installing PHP  
RUN yum clean all  
RUN yum -y --enablerepo=remi,remi-php71 install php-cli php-common php-json
php-gd php-intl php-mbstring php-mcrypt php-mysqlnd php-ldap php-pdo php-pear
php-pgsql php-process php-soap php-pecl-xdebug php-xml php-xsl php-pecl-zip
php-opcache  
  
# Installing pip and aws-cli  
RUN yum install -y python-setuptools python-pip  
RUN pip install awscli  
  
# Installing composer  
RUN yum install -y wget  
RUN wget -O /usr/local/bin/composer https://getcomposer.org/composer.phar  
RUN chmod +x /usr/local/bin/composer  
  
# Installing phpunit  
RUN composer global require "phpunit/phpunit=^5.0"  
RUN composer global require phpmd/phpmd  
RUN composer global require squizlabs/php_codesniffer  
RUN composer global require sebastian/phpcpd  
ENV PATH="/root/.composer/vendor/bin:${PATH}"  
RUN wget -O /usr/local/bin/codecept http://codeception.com/codecept.phar  
RUN chmod a+x /usr/local/bin/codecept

