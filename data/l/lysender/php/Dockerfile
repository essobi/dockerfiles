FROM centos:centos7  
MAINTAINER Leonel Baer <leonel@lysender.com>  
  
# Install packages  
RUN yum -y update && yum clean all  
RUN yum -y install epel-release && yum clean all  
  
# Install MariaDB, Apache, PHP and misc tools  
RUN yum -y install mariadb-devel \  
git \  
tree \  
php \  
php-bcmath \  
php-common \  
php-pear \  
php-mysql \  
php-cli \  
php-devel \  
php-gd \  
php-fpm \  
php-pdo \  
php-mbstring \  
php-mcrypt \  
php-soap \  
php-xml \  
php-xmlrpc \  
bind-utils \  
psmisc \  
net-tools \  
hostname \  
curl \  
curl-devel \  
sqlite \  
sendmail && yum clean all  
  
# Configure  
ADD ./start.sh /start.sh  
ADD ./timezone.ini /etc/php.d/timezone.ini  
  
RUN chmod 755 /start.sh  
  
CMD ["/bin/bash", "/start.sh"]  

