FROM centos:centos7  
  
MAINTAINER "Daniel Yang" <yang@desheng.me>  
  
# Required Repos  
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-7-5.noarch.rpm && \  
rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm  
  
# Setup 163 Repo (Just for users in China)  
# RUN yum -y install wget && \  
# mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-
Base.repo.backup && \  
# wget -P /etc/yum.repos.d/ http://mirrors.163.com/.help/CentOS7-Base-163.repo
&& \  
# yum clean all && \  
# yum makecache  
# OS Update  
RUN yum update -y && \  
yum install -y vim  
  
# Install PHP  
RUN yum install --enablerepo=remi -y \  
php56-php-cli \  
php56-php-fpm \  
php56-php-mysqlnd \  
php56-php-gd \  
php56-php-mcrypt \  
php56-php-mbstring \  
php56-php-opcache \  
php56-php-pecl-memcache \  
php56-php-pecl-memcached \  
php56-php-pecl-redis  
  
# Update PHP Config  
RUN sed -i "s/;date.timezone =.*/date.timezone = PRC/"
/opt/remi/php56/root/etc/php.ini && \  
sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/"
/opt/remi/php56/root/etc/php.ini && \  
sed -i "s/display_errors = Off/display_errors = stderr/"
/opt/remi/php56/root/etc/php.ini && \  
sed -i "s/upload_max_filesize = 2M/upload_max_filesize = 32M/"
/opt/remi/php56/root/etc/php.ini && \  
sed -i "s/;opcache.enable=0/opcache.enable=0/"
/opt/remi/php56/root/etc/php.ini && \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g"
/opt/remi/php56/root/etc/php-fpm.d/www.conf && \  
sed -i '/^listen = /clisten = 9000' /opt/remi/php56/root/etc/php-
fpm.d/www.conf && \  
sed -i '/^listen.allowed_clients/c;listen.allowed_clients ='
/opt/remi/php56/root/etc/php-fpm.d/www.conf && \  
sed -i "/^user = /cuser = root" /opt/remi/php56/root/etc/php-fpm.d/www.conf &&
\  
sed -i "/^group = /cgroup = root" /opt/remi/php56/root/etc/php-fpm.d/www.conf
&& \  
sed -i '/^;catch_workers_output/ccatch_workers_output = yes'
/opt/remi/php56/root/etc/php-fpm.d/www.conf  
RUN echo "clear_env = no" >> /opt/remi/php56/root/etc/php-fpm.d/www.conf  
  
# Volumes  
RUN mkdir -p /opt/www  
VOLUME ["/opt/www"]  
  
# Ports  
EXPOSE 9000  
# Run on start  
CMD ["/opt/remi/php56/root/usr/sbin/php-fpm", "-F", "-R"]

