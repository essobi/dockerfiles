FROM kitsudo/aliyun_centos6.6  
MAINTAINER Dave Luo <kitsudo163@163.com>  
RUN yum install httpd mysql-server -y && yum clean all  
  
# http://www.chenxuanyi.cn/xampp-phpstorm-xdebug.html  
# RUN rpm -qa | grep php | xargs rpm -e --nodeps  
# RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-6.noarch.rpm  
RUN rpm -Uvh http://mirror.webtatic.com/yum/el6/latest.rpm  
RUN yum install php55w php55w-mysql php55w-gd php55w-imap php55w-odbc
php55w-pear php55w-xml php55w-xmlrpc php55w-mcrypt php55w-mbstring
php55w-devel php55w-pecl-xdebug.x86_64 -y && yum clean all

