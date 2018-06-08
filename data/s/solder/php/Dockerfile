FROM centos:7.4.1708  
MAINTAINER tak-solder  
  
RUN yum update -y \  
&& yum install -y epel-release \  
&& yum install -y http://rpms.famillecollet.com/enterprise/remi-release-7.rpm
\  
&& yum clean all  
  
RUN yum install -y git zip unzip vim \  
&& yum clean all  
  
RUN yum install -y --enablerepo=remi,remi-php71 php-common php-cli php-json
php-mbstring php-mysqlnd php-pdo php-xml \  
&& yum clean all  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  

