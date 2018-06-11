FROM centos:6  
RUN yum install -y centos-release-scl && \  
yum -y install rh-php70-php-cli rh-php70-php-xml rh-php70-php-pecl-xdebug rh-
php70-php-mbstring rh-php70-php-pdo && \  
yum clean all  
  
CMD [ "make", "-C", "/tuleap", "phpunit-run-as-owner" ]  
  
VOLUME ["/tuleap"]  

