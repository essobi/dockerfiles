# This container is specifically built to be used inside of a bitbucket
pipeline  
# since it doesn't support multiple container orchestration for now,  
# we need to work around that by having one  
# big container with everything installed.  
# You can read more on https://bitbucket.org/site/master/issues/12901/use-
mysql-docker-image-for-unit-tests-in  
# and watch the issue over
https://bitbucket.org/site/master/issues/12757/ability-to-run-multiple-docker-
containers  
# For a database I am assuming that sqlite3 will be used, just for the sake of
simplicity and speed,  
# something like PerconaDB can be used but there are some issues regarding
systemd and how it  
# work inside of containers.  
FROM centos  
MAINTAINER Steve Azzopardi <steveaz@outlook.com>  
  
# Update  
RUN yum update -y  
  
# Install php7  
RUN \  
yum install -y http://rpms.remirepo.net/enterprise/remi-release-7.rpm && \  
yum update -y && \  
yum install -y php --enablerepo=remi,remi-php70 && \  
yum install -y php-mbstring php-opcache php-pdo php-mcrypt php-xml php-mysql
php-gd php-zip --enablerepo=remi,remi-php70  
  
# Install composer (installation instructions here
https://getcomposer.org/download/)  
RUN \  
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \  
php composer-setup.php && \  
php -r "unlink('composer-setup.php');" && \  
mv composer.phar /usr/local/bin/composer  
  
# Install node  
RUN \  
curl --silent --location https://rpm.nodesource.com/setup_6.x | bash - && \  
yum install -y nodejs  
  
# Install phantomjs  
RUN \  
cd /opt && \  
yum install -y fontconfig && \  
yum install -y bzip2 && \  
mkdir -p /opt/phantomjs && \  
curl -L
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
| tar -xj --strip-components=1 -C /opt/phantomjs && \  
ln -s /opt/phantomjs/bin/phantomjs /usr/bin/phantomjs  
  
# Install git  
RUN yum install -y git  
  
# Clean things up  
RUN yum clean all  

