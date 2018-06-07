FROM ricordanza/centos7-japanize  
  
RUN yum -y update && \  
yum -y install curl && \  
yum -y install git && \  
yum -y install vim && \  
yum -y install centos-release-scl && \  
yum -y install httpd24 && \  
yum -y remove php-* && \  
yum -y install \--enablerepo=remi,remi-php56 php php-devel php-mbstring php-
pdo php-gd && \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
yum clean all && \  
rm -rf /var/log/*  

