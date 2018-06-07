FROM centos:7  
MAINTAINER Stellan Nordenbro <stellan.nordenbro@ju.se>  
# Add IUS repository for PHP and update  
RUN yum localinstall -y https://centos7.iuscommunity.org/ius-release.rpm &&
yum update -y  
# Install PHP and modules  
RUN yum install -y php71u-cli php71u-fpm php71u-common  
RUN yum install -y php71u-mcrypt php71u-ldap php71u-mbstring \  
php71u-pdo php71u-pgsql php71u-gd \  
php71u-intl php71u-bcmath php71u-process \  
php71u-tidy php71u-xml php71u-xmlrpc \  
php71u-devel php71u-pspell php71u-recode php71u-opcache php71u-json \  
php71u-pecl-xdebug php71u-pecl-apcu \  
git curl vim node npm make automake epel-release  
# Not yet supported php70u-pear \  
# Add postgres client  
RUN sed -i 's/RPM-GPG-KEY-CentOS-7/RPM-GPG-KEY-
CentOS-7\nexclude=postgresql*/g' /etc/yum.repos.d/CentOS-Base.repo && \  
yum localinstall -y
https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-
redhat96-9.6-3.noarch.rpm && yum update -y && \  
yum install -y postgresql96  
  
# Add configurations  
ADD ./conf/symfony.ini /etc/php.d/10-symfony.ini  
  
# Install utilities (xdebug is used by CI and Dev  
RUN curl -o /usr/local/bin/phpunit https://phar.phpunit.de/phpunit-5.7.3.phar
&& chmod +x /usr/local/bin/phpunit  
RUN cd /usr/local/bin && curl -sS https://getcomposer.org/installer | php --
--filename=composer  
RUN npm install -g bower uglifyjs uglifycss grunt-cli  
  
# Container configuration  
WORKDIR /var/www/symfony  
  
# Dummy startup script  
COPY ./scripts/entrypoint.sh /entrypoint.sh  
COPY ./scripts/control/pause /pause  
COPY ./scripts/control/resume /resume  
COPY ./scripts/control/restart /restart  
  
EXPOSE 9000  
RUN chmod +x /entrypoint.sh  
CMD [ "/entrypoint.sh" ]  

