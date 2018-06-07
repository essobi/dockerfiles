FROM centos:7  
#MAINTAINER Riccardo Manuelli  
RUN yum -y install epel-release  
RUN yum -y install wget  
RUN wget https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN wget https://centos7.iuscommunity.org/ius-release.rpm  
RUN rpm -Uvh ius-release*.rpm  
RUN yum -y update  
  
# Installing memcache  
RUN yum -y install php56u-fpm php56u php56u-opcache php56u-xml php56u-mcrypt
php56u-gd php56u-devel php56u-mysql php56u-intl php56u-mbstring php56u-bcmath
php56u-pecl-memcache  
  
# Installing mysql  
#RUN yum -y install mysql-server mysql-client  
RUN yum -y install mysql  
  
# Installing nginx  
RUN yum -y install nginx  
  
# Installing other utilities  
RUN yum -y install git software-properties-common zip unzip  
  
# Other configs / timezone, short tags, etc  
COPY settings/php.d /etc/php.d  
  
# Adding the configuration file of the nginx  
COPY settings/nginx/conf.d /etc/nginx/conf.d  
ADD settings/nginx/nginx.conf /etc/nginx/nginx.conf  
  
VOLUME /var/www/html  
  
EXPOSE 80  
EXPOSE 3306  
CMD ["nginx", "-g", "daemon off;" "mysqld"]  

