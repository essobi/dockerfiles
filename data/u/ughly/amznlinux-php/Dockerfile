FROM amazonlinux  
  
MAINTAINER Chris Yawman <chris.yawman@team.neustar>  
  
RUN yum install -y epel-release git wget patch  
  
RUN yum -y install php71-cli php71-common php71-json php71-gd php71-intl
php71-mbstring php71-mcrypt php71-mysqlnd php71-ldap php71-pdo php71-pear
php71-pgsql php71-process php71-soap php71-pecl-xdebug php71-xml php71-xsl
php71-pecl-zip php71-opcache  
  
RUN yum -y install python-pip  
RUN python-pip install awscli  
  
RUN wget -O /usr/local/bin/composer https://getcomposer.org/composer.phar  
RUN chmod +x /usr/local/bin/composer  
  
RUN composer global require "phpunit/phpunit=^5.0"  
RUN composer global require phpmd/phpmd  
RUN composer global require squizlabs/php_codesniffer  
RUN composer global require sebastian/phpcpd  
ENV PATH="/root/.composer/vendor/bin:${PATH}"  
RUN wget -O /usr/local/bin/codecept http://codeception.com/codecept.phar  
RUN chmod a+x /usr/local/bin/codecept  

