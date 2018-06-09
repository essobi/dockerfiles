FROM ubuntu:14.04.1  
MAINTAINER Benjamin Wenderoth <b.wenderoth@gmail.com>  
  
# Surpress Upstart errors/warning  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# First we Install SSH Access  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install
openssh-server pwgen  
RUN mkdir -p /var/run/sshd && sed -i
"s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config
&& sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && sed -i
"s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config  
  
ADD set_root_pw.sh /set_root_pw.sh  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
# Add sources for latest nginx  
RUN apt-get install -y wget  
RUN wget -q http://nginx.org/keys/nginx_signing.key -O- | sudo apt-key add -  
RUN echo deb http://nginx.org/packages/mainline/ubuntu/ trusty nginx >>
/etc/apt/sources.list  
RUN echo deb-src http://nginx.org/packages/mainline/ubuntu/ trusty nginx >>
/etc/apt/sources.list  
  
# Update System  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Install Basic Requirements  
RUN apt-get -y install nginx python-software-properties python-setuptools
software-properties-common curl  
  
# Install PHP  
RUN apt-get -y install php5-fpm php5-mysql php-apc php5-cli php5-dev  
  
# Install Extra PHP Modules  
RUN apt-get -y install php5-curl php5-gd php-pear php5-mcrypt php5-mongo
php5-mysqlnd php5-mysqlnd-ms php5-json  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
ADD ./nginx.conf /etc/nginx/nginx.conf  
ADD ./www.conf /etc/php5/fpm/pool.d/www.conf  
ADD ./php.ini /etc/php5/fpm/php.ini  
ADD ./php_cli.ini /etc/php5/cli/php.ini  
  
# nginx site conf  
RUN rm -Rf /etc/nginx/conf.d/*  
RUN mkdir -p /etc/nginx/sites-available/  
RUN mkdir -p /etc/nginx/sites-enabled/  
RUN mkdir -p /etc/nginx/ssl/  
ADD ./nginx-site.conf /etc/nginx/sites-available/default.conf  
RUN ln -s /etc/nginx/sites-available/default.conf /etc/nginx/sites-
enabled/default.conf  
# add test PHP file  
ADD ./index.php /usr/share/nginx/html/index.php  
RUN chown -Rf nginx.nginx /usr/share/nginx/html/  
# Supervisor Config  
RUN /usr/bin/easy_install supervisor  
RUN /usr/bin/easy_install supervisor-stdout  
ADD ./supervisord.conf /etc/supervisord.conf  
# Start Supervisord  
ADD ./start.sh /start.sh  
RUN chmod 755 /start.sh  
  
# Some variables  
ENV AUTHORIZED_KEYS **None**  
  
# Expose Ports - http, https  
EXPOSE 443  
EXPOSE 80  
CMD ["/run.sh"]  
CMD ["/bin/bash", "/start.sh"]  

