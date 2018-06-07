FROM centos:centos7  
  
MAINTAINER Mikael Keto  
  
# add epel/webtatic repository and gpg key  
ADD epel.repo /etc/yum.repos.d/epel.repo  
ADD webtatic.repo /etc/yum.repos.d/webtatic.repo  
ADD RPM-GPG-KEY-EPEL-7 /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7  
ADD RPM-GPG-KEY-webtatic-el7 /etc/pki/rpm-gpg/RPM-GPG-KEY-webtatic-el7  
  
# install php and various extensions  
RUN yum -y install php55w \  
php55w-bcmath \  
php55w-enchant \  
php55w-gd \  
php55w-intl \  
php55w-mbstring \  
php55w-mcrypt \  
php55w-mysql \  
php55w-opcache \  
php55w-pdo \  
php55w-process \  
php55w-soap \  
php55w-xml \  
php55w-pecl-geoip \  
php55w-pecl-memcache \  
ImageMagick \  
ssmtp && \  
yum clean all && rm -rf /var/cache/yum  
  
CMD ["php", "-a"]  

