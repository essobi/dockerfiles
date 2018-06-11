# Master image  
FROM centos:7  
MAINTAINER yogzheng@gmail.com  
  
# Base package  
RUN yum -y update  
RUN yum -y install sudo  
RUN yum -y install libxml2 libxml2-devel libcurl-devel libjpeg-turbo-devel
libpng-devel libmcrypt-devel readline-devel libtidy-devel libxslt-devel  
RUN yum install -y git zip unzip openssl-devel curl-devel vim-enhanced  
  
#安装 remi源  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm  
  
WORKDIR /root  
  
# 安装 PHP7.1  
RUN yum -y --enablerepo=remi-php71 install php php-fpm php-intl php-mbstring
php-xml php-pdo php-mysqlnd php-opcache php-mcrypt  
  
# 配置httpd conf  
COPY vhost.conf /etc/httpd/conf.d/  
  
# 安装 Redis  
RUN yum --enablerepo=epel install -y redis  
  
# 安装 MySQL5.7  
RUN rpm -ivh http://dev.mysql.com/get/mysql57-community-release-
el7-8.noarch.rpm  
RUN yum install -y mysql-community-server  
  
# 设置时区  
RUN cp /etc/localtime /etc/localtime.org  
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
# 开机启动  
RUN systemctl enable httpd.service  
RUN systemctl enable redis  
  
EXPOSE 80

