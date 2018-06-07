FROM centos:6  
MAINTAINER Yasushi Kobayashi <ptpadan@gmail.commv>  
  
RUN yum -y update && \  
yum -y install git zip unzip  
  
RUN yum -y install epel-release && \  
curl -O http://rpms.famillecollet.com/enterprise/remi-release-6.rpm && \  
rpm -Uvh remi-release-6*.rpm && \  
yum -y install --enablerepo=remi --enablerepo=remi-php70 php php-devel php-
mbstring php-pdo php-gd php-mysqlnd php-openssl php-mcrypt php-pecl-redis
phpunit  
  
RUN yum -y install httpd && \  
chkconfig httpd on  
  
RUN yum -y install http://repo.mysql.com/mysql-community-release-
el6-4.noarch.rpm && \  
yum -y install mysql-community-server && \  
chkconfig mysqld on  
  
RUN yum -y --enablerepo=epel install redis && \  
chkconfig redis on  
  
RUN curl -sS https://getcomposer.org/installer | php && \  
chmod +x composer.phar && \  
mv composer.phar /usr/local/bin/composer  
  
RUN git clone git://github.com/creationix/nvm.git ~/.nvm && \  
echo 'source ~/.nvm/nvm.sh' >> ~/.bash_profile && \  
source ~/.nvm/nvm.sh && \  
nvm install v6.7.0 && \  
npm i -g yarn  
  
CMD service httpd start && service mysqld start && service redis start  

