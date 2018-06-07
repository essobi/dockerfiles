FROM centos:latest  
MAINTAINER Johnny Zheng <johnny@itfolks.com.au>  
  
# - Install basic packages needed by supervisord  
# - Install inotify, needed to automate daemon restarts after config file
changes  
# - Install supervisord (via python's easy_install - as it has the newest 3.x
version)  
#Install tools  
RUN yum install -y yum-utils python-setuptools inotify-tools unzip sendmail
tar mysql sudo wget telnet rsync git nmap  
  
#Install yum repos and utils epel-release  
#rpm -Uvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-7-5.noarch.rpm && \  
#yum -y install epel-release && \  
RUN yum -y install epel-release  
RUN yum install -y nginx  
RUN yum -y install epel-release && \  
rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm && \  
yum-config-manager -q --enable remi && \  
yum-config-manager -q --enable remi-php72  
  
#Install nginx, php-fpm and php extensions  
RUN yum install -y php-fpm php-common memcached  
RUN yum install -y php-pecl-apc php-cli php-pear php-pdo php-mysql php-pecl-
memcache php-pecl-memcached php-gd php-mbstring php-mcrypt php-xml php-adodb
php-imap php-intl php-soap  
RUN yum install -y php-mysqli php-zip php-iconv php-curl php-simplexml php-dom
php-bcmath php-opcache php-pecl-redis  
  
#Clean up yum repos to save spaces  
RUN yum update -y && yum clean all  
  
#Install supervisor  
RUN easy_install supervisor  
#Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
#Update nginx user group and name  
RUN rm -rf /etc/nginx/*.d /etc/nginx/*_params && \  
mkdir -p /data/www && \  
mkdir -p /data/logs && \  
chown -R nginx:nginx /var/www /data/www  
#lib/nginx  
#Add pre-configured files  
ADD files /  
# RUN find /config |grep .sh |xargs chmod +x  
VOLUME ["/data"]  
  
EXPOSE 80 443  
# Adding the configuration file of the Supervisor  
# ENTRYPOINT ["/config/bootstrap.sh"]  
ENTRYPOINT ["/config/bootstrap.sh"]

