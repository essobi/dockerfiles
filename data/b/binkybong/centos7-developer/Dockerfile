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
  
RUN yum install -y mod_php72w php72w-cli php72w-common php72w-gd
php72w-mbstring php72w-mcrypt php72w-mysqlnd php72w-xml php72w-fpm
php72w-pgsql nginx openssl net-tools wget git curl php72w-pear php72w-devel
gcc curl-devel zlib-devel install pcre-devel vim telnet zeromq zeromq-devel  
  
RUN mkdir /var/www/html -p  
  
RUN mkdir /etc/letsencrypt -p  
  
RUN curl --silent --location https://rpm.nodesource.com/setup_9.x | bash -  
  
RUN yum -y install nodejs yarn  
  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash  
  
RUN git config --global user.name "Andy"  
  
RUN git config --global user.email "andy.wong@alldaypa.com"  
  
RUN npm install -g @vue/cli  
  
RUN npm install -g @vue/cli-service-global  
  
WORKDIR /srv  
  
RUN wget https://getcomposer.org/installer  
  
RUN chmod +x installer  
  
RUN /usr/bin/php /srv/installer  
  
RUN mv /srv/composer.phar /usr/local/bin/composer  
  
RUN echo 'export PATH="$HOME/.composer/vendor/bin:$PATH"' >> ~/.bashrc  
  
RUN composer global require "laravel/installer"  
  
EXPOSE 80 443 8080  
RUN chown -R nginx:nginx /var/www/html  
  
WORKDIR /var/www/html  
  
RUN pecl install zmq-beta  
  
# Executing supervisord  
CMD ["supervisord", "-n"]  

