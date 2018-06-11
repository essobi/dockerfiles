FROM centos:centos7  
  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm && \  
rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm && \  
rpm -ivh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm  
  
RUN yum -y update  
  
RUN yum install -y libaio \  
gcc \  
openssl-devel \  
git  
  
ADD source/oracle-instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm /tmp  
ADD source/oracle-instantclient12.1-basic-12.1.0.2.0-1.x86_64.rpm /tmp  
  
RUN rpm -i /tmp/oracle-instantclient12.1-basic-12.1.0.2.0-1.x86_64.rpm && \  
rpm -i /tmp/oracle-instantclient12.1-devel-12.1.0.2.0-1.x86_64.rpm  
  
RUN export LD_LIBRARY_PATH=/usr/lib/oracle/12.1/client64/lib/  
RUN export ORACLE_HOME=/usr/lib/oracle/12.1/client64/lib/  
  
ENV LD_LIBRARY_PATH /usr/lib/oracle/12.1/client64/lib/  
ENV ORACLE_HOME /usr/lib/oracle/12.1/client64/lib/  
  
RUN yum install -y php71-php-common \  
php71-php-fpm \  
php71-php-cli \  
php71-php-mcrypt \  
php71-php-mbstring \  
php71-php-pecl-memcache \  
php71-php-pecl-memcached \  
php71-php-gd \  
php71-php-pecl-zip \  
php71-php-process \  
php71-php-soap \  
php71-php-pecl-stomp \  
php71-php-pear \  
php71-php-devel \  
php71-php-xml \  
php71-php-pdo \  
php71-php-oci8 \  
php71-php-bcmath \  
php71-php-pecl-xdebug \  
php71-xhprof  
  
EXPOSE 9000  
  
ENTRYPOINT ["/opt/remi/php71/root/usr/sbin/php-fpm", "--nodaemonize"]

