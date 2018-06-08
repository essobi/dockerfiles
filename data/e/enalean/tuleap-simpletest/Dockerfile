FROM centos:6  
  
RUN yum install -y epel-release centos-release-scl && \  
yum -y install \  
rh-php70-php \  
rh-php70-php-soap \  
rh-php70-php-mysqlnd \  
rh-php70-php-gd \  
rh-php70-php-process \  
rh-php70-php-xml \  
rh-php70-php-mbstring \  
rh-php70-php-imap \  
rh-php70-php-intl \  
rh-php70-php-pecl-xdebug \  
sclo-php70-php-pecl-redis \  
mysql-server \  
rcs \  
cvs \  
php-ZendFramework2-Loader \  
php-ZendFramework2-Mail \  
unzip \  
tar \  
subversion \  
bzip2 \  
php-pecl-xdebug \  
php-markdown \  
sudo \  
rh-git29-git \  
gitolite3 && \  
yum clean all  
  
RUN git config --global user.email "ut@tuleap.org" && git config --global
user.name "Unit test runner" && \  
useradd codendiadm && \  
useradd gitolite && \  
ln -s /usr/share/tuleap/ /tuleap && \  
service mysqld start && sleep 1 && mysql -e "GRANT ALL PRIVILEGES on *.* to
'integration_test'@'localhost' identified by 'welcome0'" && \  
mkdir -p /var/tmp/tuleap_cache && \  
ln -s /var/tmp/codendi_cache /var/tmp/tuleap_cache && \  
echo "Defaults:root !requiretty" >> /etc/sudoers  

