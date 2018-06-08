FROM ubuntu:14.04  
MAINTAINER Leon Radley <leon@digiplant.se>  
  
# Env  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update packages and install basic stuff  
RUN apt-get update  
RUN apt-get -y install curl git  
  
# Locale  
RUN locale-gen sv_SE.UTF-8  
RUN echo
"LANG=\"en_US.UTF-8\"\nLANGUAGE=\"en_US.UTF-8\"\nLC_ALL=\"sv_SE.UTF-8\"\n" >>
/etc/environment  
RUN echo
"LANG=\"en_US.UTF-8\"\nLANGUAGE=\"en_US.UTF-8\"\nLC_ALL=\"sv_SE.UTF-8\"\n" >
/etc/default/locale  
  
# Mysql  
RUN apt-get -y install mysql-server  
ADD config/mysql.cnf /etc/mysql/conf.d/mysql.cnf  
RUN service mysql restart  
  
# PHP  
RUN apt-get -y install php5 php5-cli php5-intl php5-fpm php5-curl php5-gd
php5-mysql  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g"
/etc/php5/fpm/php.ini  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Nginx  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ABF5BD827BD9BF62  
RUN echo "deb http://nginx.org/packages/ubuntu/ trusty nginx\ndeb-src
http://nginx.org/packages/ubuntu/ trusty nginx\n" >>
/etc/apt/sources.list.d/nginx.list;  
RUN apt-get update && apt-get -y install nginx  
  
EXPOSE 80 3306  
VOLUME ["/var/log/mysql", "/var/www", "/var/log/nginx/"]  

