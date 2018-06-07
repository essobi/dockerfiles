FROM oraclelinux:7  
MAINTAINER David Binney "d.binney@cqu.edu.au"  
LABEL base.name="Oracle Enterprise Linux + Apache + PHP56" \  
base.version="${VERSION}"  
  
EXPOSE 80 443 22  
ENV APPROOT="/var/www/html" \  
VERSION="0.1" \  
LANG="en_AU.UTF-8" \  
TZ="Australia/Brisbane"  
#adding webtatic repos  
RUN rpm -ivh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm && \  
rpm -ivh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm  
  
##add new yum repo for postgres and remove old  
RUN yum install -y
https://download.postgresql.org/pub/repos/yum/9.5/redhat/rhel-7-x86_64/pgdg-
redhat95-9.5-2.noarch.rpm  
RUN yum remove -y postgresql.x86_64  
  
#add in the repo for github large file system  
COPY repo/*.sh /tmp/  
RUN os=el dist=7 /tmp/github_git-lfs.sh  
  
RUN yum update -y && yum install -y \  
sudo \  
gcc \  
git.x86_64 \  
git-lfs.x86_64 \  
postgresql95.x86_64 \  
openssl.x86_64 \  
memcached.x86_64 \  
libaio.x86_64 \  
sqlite.x86_64 \  
httpd.x86_64 \  
httpd-tools.x86_64  
  
RUN yum install -y \  
php56w-cli.x86_64 \  
php56w-common.x86_64 \  
php56w-devel.x86_64 \  
php56w-gd.x86_64 \  
php56w-intl.x86_64 \  
php56w-ldap.x86_64 \  
php56w-mbstring.x86_64 \  
php56w-mcrypt.x86_64 \  
php56w-mcrypt.x86_64 \  
php56w-mssql.x86_64 \  
php56w-mysql.x86_64 \  
php56w-oci8.x86_64 \  
php56w-odbc.x86_64 \  
php56w-opcache.x86_64 \  
php56w-pdo.x86_64 \  
php56w-pear.noarch \  
php56w-pecl-igbinary \  
php56w-pecl-memcached \  
php56w-pecl-xdebug \  
php56w-pgsql.x86_64 \  
php56w-soap.x86_64 \  
php56w-xml.x86_64 \  
php56w.x86_64 \  
php-phpunit-phpcov \  
php56w-xmlrpc.x86_64  
  
ENV CONF_WWWROOT="/var/www/html" \  
CONF_DATAROOT="/var/www/sitedata" \  
COMPOSER_HOME="/var/www/composer_cache" \  
VERSION="0.1"  
#php config stuff here..  
RUN pecl config-set php_ini /etc/php.ini  
RUN pear config-set php_ini /etc/php.ini  
  
## git config so git pulls including composer etc can pull un-authed  
RUN git config --global url."https://github.com/".insteadOf "git@github.com:"  
  
WORKDIR ${CONF_WWWROOT}  
  
# COPY . ${CONF_WWWROOT}  
RUN mkdir -p ${CONF_DATAROOT}  
RUN chown -R apache:apache ${CONF_DATAROOT}  
RUN mkdir -p ${COMPOSER_HOME}  
RUN chown -R apache:apache ${COMPOSER_HOME}  
RUN chown -R apache:apache ${CONF_WWWROOT}  
  
## copy ssh key for deployment purposes  
COPY ssl/deployment.key /root/.ssh/id_rsa  
COPY ssl/deployment.key.pub /root/.ssh/id_rsa.pub  
COPY ssl/config /root/.ssh/config  
RUN chmod 600 /root/.ssh/id_rsa  
RUN ssh-keyscan guthub.com >> ~/.ssh/known_hosts  
  
# #oracle will probably winge at this but its so much easier...  
# COPY rpm/oracle-instantclient12* /tmp/  
# RUN rpm -ivh /tmp/oracle-instantclient12.1-basic-12.1.0.2.0-1.x86_64.rpm &&
\  
# rpm -ivh /tmp/oracle-instantclient12.1-sqlplus-12.1.0.2.0-1.x86_64.rpm && \  
# rpm -ivh /tmp/oracle-instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm  
#FIXME -- this bullshit only exists because dockhub does not download the git-
lfs files  
RUN git clone git@github.com:donkeyx/oel-apache-php.git /tmp/oel-apache-repo  
RUN rpm -ivh /tmp/oel-apache-repo/php56/rpm/oracle-
instantclient12.1-basic-12.1.0.2.0-1.x86_64.rpm && \  
rpm -ivh /tmp/oel-apache-repo/php56/rpm/oracle-
instantclient12.1-sqlplus-12.1.0.2.0-1.x86_64.rpm && \  
rpm -ivh /tmp/oel-apache-repo/php56/rpm/oracle-
instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm  
  
## oracle and odbtp lib which is needed for mssql errors  
RUN yes "" | pecl install oci8-2.0.12  
RUN yes "" | pecl install odbtp  
  
#RUN ssh-keyscan guthub.com >> /root/.ssh/known_hosts \  
# eval $(ssh-agent -s)  
# ssh-add /root/.ssh/deployment.key  
RUN cat /etc/php.ini  
  
## php specific config stuff  
RUN sed -i "s|;date.timezone =|date.timezone = Australia/Brisbane|g"
/etc/php.ini; \  
sed -i "s|display_errors = Off|display_errors = On|g" /etc/php.ini; \  
sed -i "s|error_reporting = E_ALL & ~E_DEPRECATED & ~E_STRICT|error_reporting
= E_ALL|g" /etc/php.ini  
  

