FROM centos:latest  
MAINTAINER Neeki Patel <neeki.patel@gmail.com>  
  
  
#  
# Update CetnOS and add epel  
#  
RUN yum -y update && yum clean all  
RUN yum -y install epel-release  
  
#  
# Install Basic utilities  
#  
RUN yum -y install bind-utils curl git lsof sysstat tar telnet unzip vim-
enhanced wget  
  
#  
# Set ulimits  
#  
ADD security/limits.conf /etc/security/limits.conf  
ADD security/90-nproc.conf /etc/security/90-nproc.conf  
  
#  
# PHP  
#  
RUN yum install -y php php-cli php-gd php-mysql php-soap php-xml php-mbstring
php-mcrypt php-process php-pecl-memcache php-pgsql php-pecl-apcu php-pecl-
mongo libmcrypt  
  
ADD php/php.ini /etc/php.ini  
ADD php/php.d/apcu.ini /etc/php.d/acpu.ini  
ADD php/php.d/memcache.ini /etc/php.d/memcache.ini  
  
#  
# Node.js  
#  
CMD ["curl -sL https://rpm.nodesource.com/setup | bash -"]  
RUN yum -y install nodejs npm  
  
#  
# Ruby  
#  
RUN yum -y install ruby

