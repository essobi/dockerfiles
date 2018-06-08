FROM centos:7  
RUN yum -y install epel-release  
RUN yum -y install yum-utils wget  
RUN wget https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN wget http://rpms.remirepo.net/enterprise/remi-release-7.rpm  
RUN rpm -Uvh remi-release-7.rpm epel-release-latest-7.noarch.rpm  
RUN yum-config-manager --enable remi-php72  
RUN yum -y install php-bcmath php-bz2 php-calendar php-cli php-common php-curl
php-devel php-fileinfo php-ftp php-gd php-gettext php-iconv php-intl php-
litespeed php-mbstring php-mysqlnd php-pdo php-posix php-xml php-xmlrpc php-
zip  
RUN yum install -y git openssh-server libmysqlclient-dev nano  
RUN yum -y update  
RUN EXPECTED_SIGNATURE=$(wget -q -O -
https://composer.github.io/installer.sig)  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
RUN ACTUAL_SIGNATURE=$(php -r "echo hash_file('SHA384', 'composer-
setup.php');")  
RUN if [ "$EXPECTED_SIGNATURE" != "$ACTUAL_SIGNATURE" ]; then exit 1; fi  
RUN php composer-setup.php --quiet  
RUN RESULT=$?  
RUN rm composer-setup.php  
RUN mv composer.phar /usr/local/bin/composer  
  
#also install yarn  
RUN curl --silent --location https://dl.yarnpkg.com/rpm/yarn.repo | tee
/etc/yum.repos.d/yarn.repo  
RUN curl --silent --location https://rpm.nodesource.com/setup_6.x | bash -  
RUN yum -y install yarn  
  

