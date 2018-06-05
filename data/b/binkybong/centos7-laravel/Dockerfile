# Centos 7  
FROM centos:centos7  
  
MAINTAINER Andy Wong <pslandywong@hotmail.com>  
  
ADD /contents /  
  
RUN yum -y install epel-release  
  
RUN rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm  
  
RUN yum -y update &&\  
yum clean all  
  
# Installing supervisor  
RUN yum install -y python-setuptools  
  
RUN easy_install pip  
  
RUN pip install supervisor  
  
RUN yum install -y mod_php71w php71w-cli php71w-common php71w-gd
php71w-mbstring php71w-mcrypt php71w-mysqlnd php71w-xml php71w-fpm nginx
openssl net-tools wget git curl nmap vim nano tree php71w-pgsql install
php71w-devel php71w-pear php71w-pecl-xdebug  
  
RUN mkdir /var/www/html -p  
  
ADD scripts /scripts  
  
RUN chmod 755 /scripts/*  
  
EXPOSE 80  
# RUN yum -y install nmap vim tree  
RUN chown -R apache:apache /var/www/html  
  
#RUN mkdir /srv  
WORKDIR /srv  
  
RUN wget https://getcomposer.org/installer  
  
RUN chmod +x installer  
  
RUN /usr/bin/php /srv/installer  
  
RUN mv /srv/composer.phar /usr/local/bin/composer  
  
RUN /usr/local/bin/composer global require "laravel/installer"  
  
RUN echo 'export PATH="$HOME/.composer/vendor/bin:$PATH"' >> ~/.bashrc  
  
RUN composer global require "laravel/installer"  
  
WORKDIR /var/www/html  
  
# Executing supervisord  
CMD ["supervisord", "-n"]  

